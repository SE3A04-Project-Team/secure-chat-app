import CryptoJS from 'react-native-crypto-js';

// Validate key length
const validateKeyLength = (key) => {
    if (key.length !== 32) {
        throw new Error('AES 256 key must be 32 bytes');
    }
};

// Encryption function
const encryptAES = (plainText, key) => {
    validateKeyLength(key);
    return CryptoJS.AES.encrypt(plainText, key).toString();
};

// Decryption function
const decryptAES = (cipherText, key) => {
    validateKeyLength(key);
    return CryptoJS.AES.decrypt(cipherText, key).toString(CryptoJS.enc.Utf8);
};

// Export both functions
export { encryptAES, decryptAES };
