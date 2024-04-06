import {NavigationContainer} from '@react-navigation/native';
import {createNativeStackNavigator} from '@react-navigation/native-stack';
import UserLoginScreen from "./screens/UserLoginScreen";
import ChatSelectionScreen from "./screens/ChatSelectionScreen";
import ChatScreen from "./screens/ChatScreen";
import ContactScreen from "./screens/ContactScreen";
import ProfileScreen from "./screens/ProfileScreen";
import axios from "axios";
import React, {useEffect} from "react";
import io from "socket.io-client";

const Stack = createNativeStackNavigator();

export default function App() {

    const serverUrl = process.env.EXPO_PUBLIC_SERVER_URL;

    // Sample code to connect to the socket server
    // useEffect(() => {

    //     // Connect to the socket server
    //     const socket = io(SERVER_URL);

    //     // Emit the 'join_room' event with message 'Hello, World!'
    //     socket.emit('join_room', { roomId: 'your-room-id', message: 'Hello, World!' });

    //     // Cleanup the socket connection when component unmounts
    //     return () => {
    //         socket.disconnect();
    //     };
    // }, []);

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
