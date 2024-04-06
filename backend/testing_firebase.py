from flask import Flask, jsonify, request
import firebase_admin
from firebase_admin import credentials, firestore

app = Flask(__name__)

# Initialize Firebase Admin SDK
cred = credentials.Certificate("./firebase.json")
firebase_admin.initialize_app(cred)

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

if __name__ == '__main__':
    app.run(debug=True)
