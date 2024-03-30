import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import LoginScreen from "./screens/LoginScreen";
import ChatSelectionScreen from "./screens/ChatSelectionScreen";

const Stack = createNativeStackNavigator();

export default function App() {
    return (
        <NavigationContainer>
            <Stack.Navigator screenOptions={{headerShown: false}}>
                <Stack.Screen name="Login" component={LoginScreen}/>
                <Stack.Screen name="ChatSelectionScreen" component={ChatSelectionScreen}/>
            </Stack.Navigator>
        </NavigationContainer>
    );
};
