from flask import Flask, jsonify, request
import firebase_admin
from firebase_admin import credentials, firestore

app = Flask(__name__)

# Initialize Firebase Admin SDK
cred = credentials.Certificate("./firebase.json")
firebase_admin.initialize_app(cred)

# fetch all data fpr a given collection
@app.route('/data/<collection_name>', methods=['GET'])
def get_data(collection_name):
    docs = firestore.client().collection(collection_name).get()
    return jsonify([doc.to_dict() for doc in docs])


if __name__ == '__main__':
    app.run(debug=True)
