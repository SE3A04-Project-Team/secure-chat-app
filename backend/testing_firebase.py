from flask import Flask, jsonify, request
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime

app = Flask(__name__)

# Initialize Firebase Admin SDK
cred = credentials.Certificate("./firebase.json")
firebase_admin.initialize_app(cred)



# ********************************************************************************************************************
# GET requests

# Function to recursively fetch data from Firestore
def get_data_with_subcollections(doc_ref):
    data = doc_ref.to_dict()
    for key, value in data.items():
        if isinstance(value, firestore.DocumentReference):
            data[key] = get_data_with_subcollections(value.get())
        elif isinstance(value, list) and value and isinstance(value[0], firestore.DocumentReference):
            data[key] = [get_data_with_subcollections(ref.get()) for ref in value]
    return data

# Function to fetch data from Firestore, including subcollections
def get_collection_data(collection_ref):
    collection_data = []
    for doc in collection_ref.stream():
        doc_data = get_data_with_subcollections(doc)
        subcollections = doc.reference.collections()
        subcollection_data = {subcollection.id: [get_data_with_subcollections(subdoc) for subdoc in subcollection.stream()] for subcollection in subcollections}
        doc_data['subcollections'] = subcollection_data
        collection_data.append(doc_data)
    return collection_data

# Route to fetch data from Firestore, takes collection name, returns JSON
@app.route('/collection/<collection_name>', methods=['GET'])
def get_data(collection_name):
    collection_ref = firestore.client().collection(collection_name)
    collection_data = get_collection_data(collection_ref)
    return jsonify(collection_data)

# Route to fetch data of rooms a user is in
@app.route('/user_rooms', methods=['GET'])
def get_user_rooms():
    user_id = request.args.get('userId')  # Get user ID from request parameters
    user_ref = firestore.client().collection('users').document(user_id)
    user_data = user_ref.get().to_dict()
    if user_data is None:
        return jsonify({"error": "User not found"}), 404
    
    rooms_ref = user_ref.collection('rooms').stream()
    rooms_data = []
    for room_ref in rooms_ref:
        room_data = room_ref.to_dict()
        room_doc = room_data['room'].get().to_dict()  # Fetch data from referenced room document
        rooms_data.append(room_doc)  # Append full room data
    return jsonify(rooms_data)

# Route to fetch the most recent message from a room
@app.route('/room_recent_message', methods=['GET'])
def get_room_recent_message():
    room_id = request.args.get('roomId')  # Get room ID from request parameters
    room_ref = firestore.client().collection('rooms').document(room_id)
    room_data = room_ref.get().to_dict()
    if room_data is None:
        return jsonify({"error": "Room not found"}), 404
    
    # Query the messages subcollection for the most recent message
    messages_ref = room_ref.collection('messages').order_by('timestamp', direction=firestore.Query.DESCENDING).limit(1)
    recent_messages = messages_ref.stream()
    if not recent_messages:
        return jsonify({"error": "No messages in the room"}), 404
    
    # Extract data from the most recent message document
    recent_message_data = None
    for msg in recent_messages:
        recent_message_data = msg.to_dict()
        # Fetch data from the referenced sender document
        sender_ref = recent_message_data['sender']
        sender_data = sender_ref.get().to_dict()
        recent_message_data['sender'] = sender_data
    
    return jsonify(recent_message_data)

# Route to fetch data for chat selection
@app.route('/data/chat_selection', methods=['GET'])
def get_chat_selection():
    user_id = request.args.get('userId')  # Get user ID from request parameters
    user_ref = firestore.client().collection('users').document(user_id)
    user_data = user_ref.get().to_dict()
    if user_data is None:
        return jsonify({"error": "User not found"}), 404
    
    rooms_ref = user_ref.collection('rooms').stream()
    chat_selection_data = []
    for room_ref in rooms_ref:
        room_data = room_ref.to_dict()
        room_doc = room_data['room']
        
        # Fetch the most recent message for the room
        messages_ref = room_doc.collection('messages').order_by('timestamp', direction=firestore.Query.DESCENDING).limit(1)
        recent_messages = messages_ref.stream()
        
        recent_message_data = None
        for msg in recent_messages:
            recent_message_data = msg.to_dict()
        
        # Append room data along with the most recent message content and timestamp
        chat_selection_data.append({
            'room_id': room_doc.id,
            'room_name': room_doc.get().to_dict()['name'],
            'recent_message': {
                'content': recent_message_data['content'] if recent_message_data else None,
                'timestamp': recent_message_data['timestamp'] if recent_message_data else None
            }
        })
    
    return jsonify(chat_selection_data)

# Route to fetch data for a chat screen
@app.route('/data/chat_screen', methods=['GET'])
def get_chat_screen():
    room_id = request.args.get('roomId')  # Get room ID from request parameters
    room_ref = firestore.client().collection('rooms').document(room_id)
    room_data = room_ref.get().to_dict()
    if room_data is None:
        return jsonify({"error": "Room not found"}), 404
    
    # Fetch all messages for the room
    messages_ref = room_ref.collection('messages').order_by('timestamp', direction=firestore.Query.ASCENDING).stream()
    messages_data = []
    for msg in messages_ref:
        msg_data = msg.to_dict()
        # Fetch data from the referenced sender document
        sender_ref = msg_data['sender']
        sender_data = sender_ref.get().to_dict()
        msg_data['sender'] = sender_data
        messages_data.append(msg_data)
    
    # Construct the response data
    chat_screen_data = {
        'room_id': room_id,
        'room_name': room_data.get('name'),
        'messages': messages_data
    }
    
    return jsonify(chat_screen_data)

# Route to fetch user profile data
@app.route('/data/profile', methods=['GET'])
def get_user_profile():
    user_id = request.args.get('userId')  # Get user ID from request parameters
    user_ref = firestore.client().collection('users').document(user_id)
    user_data = user_ref.get().to_dict()
    if user_data is None:
        return jsonify({"error": "User not found"}), 404
    
    return jsonify(user_data)

# ********************************************************************************************************************
# POST requests

# Route to send a message to a room
# body format: {"roomId": "room_id", "userId": "user_id", "messageContent": "message_content"}
@app.route('/send_message', methods=['POST'])
def send_message():
    # Get data from the request body
    data = request.json
    room_id = data.get('roomId')
    user_id = data.get('userId')
    message_content = data.get('messageContent')
    
    # Validate request data
    if not room_id or not user_id or not message_content:
        return jsonify({"error": "Missing required data"}), 400

    # Construct message data
    message_data = {
        'timestamp': datetime.now(),
        'content': message_content,
        'sender': firestore.client().collection('users').document(user_id)
    }
    
    # Add message to the room's messages subcollection
    room_ref = firestore.client().collection('rooms').document(room_id)
    room_ref.collection('messages').add(message_data)

    return jsonify({"message": "Message sent successfully"})

# Route to create a new room
@app.route('/create_room', methods=['POST'])
def create_room():
    # Get data from the request body
    data = request.json
    user_ids = data.get('userIds')
    
    # Validate request data
    if not user_ids:
        return jsonify({"error": "Missing required data"}), 400

    # Retrieve user names
    user_names = []
    for user_id in user_ids:
        user_ref = firestore.client().collection('users').document(user_id)
        user_data = user_ref.get().to_dict()
        if user_data:
            user_names.append(user_data.get('name', ''))
    
    # Construct the room name
    room_name = ", ".join(user_names)  # Combining user names
    
    # Create the room document
    room_ref = firestore.client().collection('rooms').document()
    room_data = {'name': room_name}  # Room name as a combination of user names
    room_ref.set(room_data)

    # Add references to users in the room's 'users' subcollection
    users_collection_ref = room_ref.collection('users')
    for user_id in user_ids:
        user_ref = firestore.client().collection('users').document(user_id)
        users_collection_ref.add({'user': user_ref})

        # Add the newly created room as a reference to the user's 'rooms' subcollection
        user_rooms_ref = user_ref.collection('rooms')
        user_rooms_ref.add({'room': room_ref})

    return jsonify({"message": "Room created successfully"})

if __name__ == '__main__':
    app.run(debug=True)
