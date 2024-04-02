import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import LoginScreen from "./screens/LoginScreen";
import ChatSelectionScreen from "./screens/ChatSelectionScreen";
import ChatScreen from "./screens/ChatScreen";
import ContactScreen from "./screens/ContactScreen";

const Stack = createNativeStackNavigator();

export default function App() {
    return (
        <NavigationContainer>
            <Stack.Navigator screenOptions={{headerShown: false}}>
                <Stack.Screen name="Login" component={LoginScreen}/>
                <Stack.Screen name="ChatSelectionScreen" component={ChatSelectionScreen}/>
                <Stack.Screen name="ChatScreen" component={ChatScreen}/>
                <Stack.Screen name="ContactScreen" component={ContactScreen}/>
            </Stack.Navigator>
        </NavigationContainer>
    );
};
