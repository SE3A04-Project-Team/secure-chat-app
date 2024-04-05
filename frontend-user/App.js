import {NavigationContainer} from '@react-navigation/native';
import {createNativeStackNavigator} from '@react-navigation/native-stack';
import UserLoginScreen from "./screens/UserLoginScreen";
import ChatSelectionScreen from "./screens/ChatSelectionScreen";
import ChatScreen from "./screens/ChatScreen";
import ContactScreen from "./screens/ContactScreen";
import ProfileScreen from "./screens/ProfileScreen";
import axios from "axios";
import {decryptAES, encryptAES} from "./utils/encryptionUtils";

const Stack = createNativeStackNavigator();
const SERVER_URL = process.env.SERVER_URL

export default function App() {

    const testServer = async () => {
        try {
            const response = await axios.post(`${SERVER_URL}/message_server/auth`, {
                key1: 'value1',
                key2: 'value2',
            });
            console.log(response.data);
            return response.data; // Returning data for further processing if needed
        } catch (error) {
            console.error('Error:', error);
        }
    };

    testServer();

    const testMessage = "Hello, World!"
    const testKey = "12345678901234567890123456789012"
    const encryptedMessage = encryptAES(testMessage, testKey);
    console.log(`Encrypted message: ${encryptedMessage}`);
    const decryptedMessage = decryptAES(encryptedMessage, testKey);
    console.log(`Decrypted message: ${decryptedMessage}`);

    return (
        <NavigationContainer>
            <Stack.Navigator screenOptions={{headerShown: false}}>
                <Stack.Screen name="UserLoginScreen" component={UserLoginScreen}/>
                <Stack.Screen name="ChatSelectionScreen" component={ChatSelectionScreen}/>
                <Stack.Screen name="ChatScreen" component={ChatScreen}/>
                <Stack.Screen name="ContactScreen" component={ContactScreen}/>
                <Stack.Screen name="ProfileScreen" component={ProfileScreen}/>
            </Stack.Navigator>
        </NavigationContainer>
    );
};
