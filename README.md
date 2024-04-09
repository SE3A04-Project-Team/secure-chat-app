# Secure Chat App
## Table of Contents
- [Description](#description)
- [Technologies](#technologies)
- [Key Features](#key-features)
- [Project Planning](#project-planning)
- [Contributors](#contributors)
- [Instructions](#instructions)
## Description


## Technologies
![React Native](https://img.shields.io/badge/-React%20Native-61DAFB?logo=react&logoColor=white&style=flat)
![Nativewind CSS](https://img.shields.io/badge/-Nativewind%20CSS-000000?logo=tailwind-css&logoColor=white&style=flat)
![Expo](https://img.shields.io/badge/-Expo-000020?logo=expo&logoColor=white&style=flat)
![Node.js](https://img.shields.io/badge/-Node.js-339933?logo=node.js&logoColor=white&style=flat)
![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white&style=flat)
![Flask](https://img.shields.io/badge/-Flask-000000?logo=flask&logoColor=white&style=flat)
![Firebase](https://img.shields.io/badge/-Firebase-FFCA28?logo=firebase&logoColor=white&style=flat)
## Key Features
- ### Kerberos Authentication Protocol
  The Kerberos Authentication Protocol is used to authenticate users before they can send messages. The protocol uses a Ticket Granting Server to issue tickets to users, which are then used to authenticate the user to the Key Distribution Center.
- ### AES Encryption
  The application uses the Advanced Encryption Standard (AES) to encrypt and decrypt messages between users. The AES algorithm is a symmetric key encryption algorithm that is used to secure the messages sent between users.
- ### Key Distribution Center
  The Key Distribution Center is responsible for generating and distributing symmetric keys to users. The keys are used to encrypt and decrypt messages between users.
- ### Real-Time Chat
  The application allows users to send and receive messages in real-time. Users can send messages to other users and view the messages they have received.
- ### Chat History Log
  The application stores a history of messages sent and received by users. Users can view their chat history and see the messages they have sent and received.
- ### Group Chat
  The application allows users to create and join group chats. Users can send messages to multiple users in a group chat and view the messages sent by other users in the group.

---

## Project Planning
All project planning documents can be found in the project planning directory

---

## Instructions
### Running the App (Frontend) for User Account
#### Setup
- NOTE: This app is designed to be run on a mobile device
- IMPORTANT! The backend server must be running before the app is started
- IMPORTANT! Update the server_url in the .env environment variables file to the IP address of the backend server 
- Install [Node.js](https://nodejs.org/en/)
- Install Expo Go on mobile phone
#### Usage
- Clone the reposit ry
- Run `npm install` in the \frontend-user directory
- Run `npx expo start` in the \frontend-user directory
- Scan the QR code with Expo Go (Android) or the Camera app (iOS)
### Running the Server (Backend) of the App
#### From EXE
Run `start_server.exe`
Obtain IP and port printed by program to include in front end .env
Ensure listed port is open on machine firewall
#### from source
Run `python3 backend/start_server.py` from project root
Obtain IP and port printed by program to include in front end .env
Ensure listed port is open on machine firewall
- View backend for instructions on how to run the backend server.
- View frontend-user for instructions on how to run the user frontend.
- View frontend-admin for instructions on how to run the admin frontend.

---

## Corresponding Files For each Feature
### Key Distribution Center
#### In the backend folder
* headers\KeyDistributionManager.py
* src\AESKeyDistributionCenter.py
* headers\KeyGenerator.py
* src\AESKeyGenerator.py
* headers\KeyStorage.py
* src\KeyStorageFirebase.py
### Mediated Authentication Protocol
#### In the backend folder
* headers\AuthenticationManager.py
* src\KerberosAuthServer.py
* src\KerberosServerAuthManager.py
* src\KerberosTicketServer.py
#### In the frontend-user
* screens\UserLoginScreen.jsx
### Symmetric Key Crypto-System
#### In the backend folder
* headers\EncryptionFunction.py
* src\AESEncryptionFunction.py
* src\FernetEncryptionFunction.py
* src\NoneEncryptor.py
* headers\EncryptionKey.py
* headers\Serializer.py
* src\PythonSerializer.py
* src\JSONSerializer.py
### Chat History Log
#### In the backend folder
* headers\MessageDatabase.py
* src\FirebaseMessageDatabase.py
#### In the frontend-user folder
* screens\ChatScreen.jsx

--- 

## Contributors
- ### [Aidan Froggatt](https://github.com/aidanfroggatt)
- ### [Rosa Chen](https://github.com/rosachen3)
- ### [Kyle McMaster](https://github.com/KyleJMcMaster)
- ### [Daniel Franze-Da Silva](https://github.com/DanielFD04)
