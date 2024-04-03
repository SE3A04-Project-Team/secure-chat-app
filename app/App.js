import {NavigationContainer} from '@react-navigation/native';
import {createNativeStackNavigator} from '@react-navigation/native-stack';
import UserLoginScreen from "./screens/UserLoginScreen";
import ChatSelectionScreen from "./screens/ChatSelectionScreen";
import ChatScreen from "./screens/ChatScreen";
import ContactScreen from "./screens/ContactScreen";
import ProfileScreen from "./screens/ProfileScreen";
import AdminLoginScreen from "./screens/AdminLoginScreen";
import {useEffect} from "react";
import {io} from "socket.io-client";

const Stack = createNativeStackNavigator();

const SERVER_URL = 'http://172.17.103.238:5000'; // Replace with your server's IP address

// Navigation stack for authenticated users
const AuthenticatedApp = () => {
    return (
        <Stack.Navigator screenOptions={{headerShown: false}}>
            <Stack.Screen name="ChatSelectionScreen" component={ChatSelectionScreen}/>
            <Stack.Screen name="ChatScreen" component={ChatScreen}/>
            <Stack.Screen name="ContactScreen" component={ContactScreen}/>
            <Stack.Screen name="ProfileScreen" component={ProfileScreen}/>
        </Stack.Navigator>
    );
};

// Navigation stack for unauthenticated users
const UnauthenticatedApp = () => {
    return (
        <Stack.Navigator screenOptions={{headerShown: false}}>
            <Stack.Screen name="UserLoginScreen" component={UserLoginScreen}/>
            <Stack.Screen name="AdminLoginScreen" component={AdminLoginScreen}/>
        </Stack.Navigator>
    );
};

// Testing stack for all screens
const AllScreens = () => {
    return (
        <Stack.Navigator screenOptions={{headerShown: false}}>
            <Stack.Screen name="UserLoginScreen" component={UserLoginScreen}/>
            <Stack.Screen name="ChatSelectionScreen" component={ChatSelectionScreen}/>
            <Stack.Screen name="ChatScreen" component={ChatScreen}/>
            <Stack.Screen name="ContactScreen" component={ContactScreen}/>
            <Stack.Screen name="ProfileScreen" component={ProfileScreen}/>
            <Stack.Screen name="AdminLoginScreen" component={AdminLoginScreen}/>
        </Stack.Navigator>
    );
};

export default function App() {
    useEffect(() => {
        console.log('Connecting to server...');

        const socket = io(SERVER_URL);

        socket.on('connect', () => {
            console.log('Connected to server');
        });

        socket.on('message', (data) => {
            console.log('Message from server:', data);
        });

        return () => {
            socket.disconnect();
        };
    }, []);
    return (
        <NavigationContainer>
            <AllScreens/>
        </NavigationContainer>
    );
};
