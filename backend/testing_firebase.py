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
@app.route('/data/<collection_name>', methods=['GET'])
def get_data(collection_name):
    collection_ref = firestore.client().collection(collection_name)
    collection_data = get_collection_data(collection_ref)
    return jsonify(collection_data)

if __name__ == '__main__':
    app.run(debug=True)
