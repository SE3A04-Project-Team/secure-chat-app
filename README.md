# Secure Chat Application Instructions

- View backend for instructions on how to run the backend server.
- View frontend-user for instructions on how to run the user frontend.
- View frontend-admin for instructions on how to run the admin frontend.

## Corresponding Files For each Feature
**Key Distribution Center:**

In the backend folder:
* headers\KeyDistributionManager.py
* src\AESKeyDistributionCenter.py
* headers\KeyGenerator.py
* src\AESKeyGenerator.py
* headers\KeyStorage.py
* src\KeyStorageFirebase.py

**Mediated Authentication Protocol:**

In the backend folder:
* headers\AuthenticationManager.py
* src\KerberosAuthServer.py
* src\KerberosServerAuthManager.py
* src\KerberosTicketServer.py

In the frontend-user:
* screens\UserLoginScreen.jsx

**Symmetric Key Crypto-System:**

In the backend folder:
* headers\EncryptionFunction.py
* src\AESEncryptionFunction.py
* src\FernetEncryptionFunction.py
* src\NoneEncryptor.py
* headers\EncryptionKey.py
* headers\Serializer.py
* src\PythonSerializer.py
* src\JSONSerializer.py

**Chat History Log:**

In the backend folder:
* headers\MessageDatabase.py
* src\FirebaseMessageDatabase.py

In the frontend-user folder:
* screens\ChatScreen.jsx

## Contributors - T03 Group 8
- [Aidan Froggatt](https://github.com/aidanfroggatt)
- [Rosa Chen](https://github.com/rosachen3)
- [Kyle McMaster](https://github.com/KyleJMcMaster)
- [Daniel Franze-Da Silva](https://github.com/DanielFD04)
- [Edward Gao](https://github.com/edwarddgao)


## Instructions for Running the App (Frontend) from a General User Account

### Technologies
![React Native](https://img.shields.io/badge/-React%20Native-61DAFB?logo=react&logoColor=white&style=flat)
![Nativewind CSS](https://img.shields.io/badge/-Nativewind%20CSS-000000?logo=tailwind-css&logoColor=white&style=flat)
![Expo](https://img.shields.io/badge/-Expo-000020?logo=expo&logoColor=white&style=flat)
![Node.js](https://img.shields.io/badge/-Node.js-339933?logo=node.js&logoColor=white&style=flat)

### File Structure Overview
```
├── assets
│   ├── Contains images used in the app
├── components
│   ├── Contains reusable components such as buttons, text inputs, etc.
├── screens
│   ├── Contains the main screens of the app such as the login screen, chat screen, etc.
```

### Setup
- NOTE: This app is designed to be run on a mobile device
- IMPORTANT! The backend server must be running before the app is started
- IMPORTANT! Update the server_url in the .env environment variables file to the IP address of the backend server 
- Install [Node.js](https://nodejs.org/en/)
- Install Expo Go on mobile phone

### Usage
- Clone the reposit ry
- Run `npm install` in the \frontend-user directory
- Run `npx expo start` in the \frontend-user directory
- Scan the QR code with Expo Go (Android) or the Camera app (iOS)

## Instructions for Running the Backend of the App



