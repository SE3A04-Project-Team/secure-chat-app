"""
Communicates with firebase

@Author: Aidan Froggatt
@Date: 2024-04-07

"""
from headers.MessageDatabase import MessageDatabase

from flask import Flask, jsonify, request
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime
import json


class FirebaseMessageDatabase(MessageDatabase):
    def __init__(self) -> None:
        cred = credentials.Certificate("backend/firebase.json")
        firebase_admin.initialize_app(cred)




    def create_room(self, room: dict) -> dict:
        """
        room should have the following fields:
        userIds - list of user_Ids

        """
        # Get data from the request body
        user_ids = room.get('userIds')
        
        # Validate request data
        if not user_ids:
            return "error: Missing required data"

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

        return f"message: Room {room_name} created successfully"
    

    def get_rooms(self, user_id: str) -> list[str, list[str]]:
           
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

            rooms = {
                "rooms": rooms_data
            }
            print(json.dumps(rooms))
            return json.dumps(rooms)
        


    def join_room(user_id: str, room_id: str):
        # TODO: Implement this function
        pass
        

    def leave_room(self, user_id: str, room_id: str):
        # TODO: Implement this function
        pass



    def get_message_history(self, room_id: str) -> dict:
        
        room_ref = firestore.client().collection('rooms').document(room_id)
        room_data = room_ref.get().to_dict()
        if room_data is None:
            return "error: Room not found"
        
        # Fetch all messages for the room
        messages_ref = room_ref.collection('messages').order_by('timestamp', direction=firestore.Query.ASCENDING).stream()
        if not messages_ref:
            return "no messages"
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
        
        return chat_screen_data
    
  
    def store_message(self, room_id: str, user_id, message_content: str, timestamp: int):
        
        # Validate request data
        if not room_id or not user_id or not message_content or not timestamp:
            return "error: Missing required data"

        # Construct message data
        message_data = {
            'timestamp': timestamp,
            'content': message_content,
            'sender': firestore.client().collection('users').document(user_id)
        }
        
        # Add message to the room's messages subcollection
        room_ref = firestore.client().collection('rooms').document(room_id)
        room_ref.collection('messages').add(message_data)

        return "message: Message sent successfully"



    def create_user(self, user: dict) -> dict:
        
        # Get data from the request body
        name = user.get('name')
        password = user.get('password')
        email = user.get('email')
        
        # Validate request data
        if not name or not password or not email:
            return jsonify({"error": "Missing required data"}), 400

        # Check if the user with the provided email already exists
        users_ref = firestore.client().collection('users')
        query = users_ref.where('email', '==', email).limit(1)
        existing_users = query.stream()
        if any(existing_users):
            return jsonify({"error": "User with this email already exists"}), 409

        # Create the user document
        user_data = {
            'name': name,
            'password': password,
            'email': email
        }
        user_ref = users_ref.document()
        user_ref.set(user_data)

        return jsonify({"message": "User created successfully"})

    def get_user(self, user_id: str) -> dict:
        
        user_ref = firestore.client().collection('users').document(user_id)
        user_data = user_ref.get().to_dict()
        if user_data is None:
            return jsonify({"error": "User not found"}), 404
        
        return jsonify(user_data)

    def delete_user(self, user_id: str) -> dict:
        
        # Validate request data
        if not user_id:
            return jsonify({"error": "Missing user ID"}), 400

        # Delete the user document
        user_ref = firestore.client().collection('users').document(user_id)
        user_ref.delete()

        return jsonify({"message": "User deleted successfully"}), 200



    def add_contact(self, user_id: str, contact_id: str):
        
        # Validate request data
        if not user_id or not contact_id:
            return jsonify({"error": "Missing required data"}), 400
        
        if user_id == contact_id:
            return jsonify({"error": "Both user IDs are the same"}), 400

        # Check if the contact already exists for user_id
        user1_contacts_ref = firestore.client().collection('users').document(user_id).collection('contacts')
        contact_query = user1_contacts_ref.where('userId', '==', contact_id).limit(1)
        existing_contacts = contact_query.stream()
        if any(existing_contacts):
            return jsonify({"message": "Contact already exists"}), 200

        # Add contact for user_id
        user1_contact_data = {
            'userId': contact_id,
            'userRef': firestore.client().collection('users').document(contact_id)
        }
        user1_contacts_ref.add(user1_contact_data)

        # Check if the contact already exists for contact_id
        user2_contacts_ref = firestore.client().collection('users').document(contact_id).collection('contacts')
        contact_query = user2_contacts_ref.where('userId', '==', user_id).limit(1)
        existing_contacts = contact_query.stream()
        if any(existing_contacts):
            return jsonify({"message": "Contact already exists"}), 200

        # Add contact for contact_id
        user2_contact_data = {
            'userId': user_id,
            'userRef': firestore.client().collection('users').document(user_id)
        }
        user2_contacts_ref.add(user2_contact_data)

        return jsonify({"message": "Contact added successfully"}), 201
    

    def remove_contact(self, user_id: str, contact_id: str):
        
        # Validate request data
        if not user_id or not contact_id:
            return jsonify({"error": "Missing required data"}), 400
        
        if user_id == contact_id:
            return jsonify({"error": "Both user IDs are the same"}), 400

        # Remove contact for user_id
        user1_contacts_ref = firestore.client().collection('users').document(user_id).collection('contacts')
        contact_query = user1_contacts_ref.where('userId', '==', contact_id).limit(1)
        existing_contacts = list(contact_query.stream())
        if existing_contacts:
            user1_contacts_ref.document(existing_contacts[0].id).delete()

        # Remove contact for contact_id
        user2_contacts_ref = firestore.client().collection('users').document(contact_id).collection('contacts')
        contact_query = user2_contacts_ref.where('userId', '==', user_id).limit(1)
        existing_contacts = list(contact_query.stream())
        if existing_contacts:
            user2_contacts_ref.document(existing_contacts[0].id).delete()

        return jsonify({"message": "Contact removed successfully"}), 200

    def get_contacts(self, user_id: str):
        # TODO: Implement this function
        pass

    def get_chat_selection(self, user_id: str):
        
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
        
        return chat_selection_data