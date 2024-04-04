import {NavigationContainer} from '@react-navigation/native';
import {createNativeStackNavigator} from '@react-navigation/native-stack';
import UserLoginScreen from "./screens/UserLoginScreen";
import ChatSelectionScreen from "./screens/ChatSelectionScreen";
import ChatScreen from "./screens/ChatScreen";
import ContactScreen from "./screens/ContactScreen";
import ProfileScreen from "./screens/ProfileScreen";
import GenerateReportScreen from "./screens/GenerateReportScreen";
import io from 'socket.io-client';
import {useEffect} from "react";

const Stack = createNativeStackNavigator();
const SERVER_URL = 'http://flask-address:port'; // Update with your server URL

export default function App() {

    useEffect(() => {
        const socket = io(SERVER_URL);

        socket.on('connect', () => {
            console.log('Connected to server!');
        });

        socket.io.on('disconnect', () => {
            console.log('Disconnected from server!');
        });

        return () => {
            socket.disconnect();
        };
    }, []);

    return (
        <NavigationContainer>
            <Stack.Navigator screenOptions={{headerShown: false}}>
                <Stack.Screen name="UserLoginScreen" component={UserLoginScreen}/>
                <Stack.Screen name="ChatSelectionScreen" component={ChatSelectionScreen}/>
                <Stack.Screen name="ChatScreen" component={ChatScreen}/>
                <Stack.Screen name="ContactScreen" component={ContactScreen}/>
                <Stack.Screen name="ProfileScreen" component={ProfileScreen}/>
                <Stack.Screen name="GenerateReportScreen" component={GenerateReportScreen}/>
            </Stack.Navigator>
        </NavigationContainer>
    );
};
