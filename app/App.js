import {NavigationContainer} from '@react-navigation/native';
import {createNativeStackNavigator} from '@react-navigation/native-stack';
import UserLoginScreen from "./screens/UserLoginScreen";
import ChatSelectionScreen from "./screens/ChatSelectionScreen";
import ChatScreen from "./screens/ChatScreen";
import ContactScreen from "./screens/ContactScreen";
import ProfileScreen from "./screens/ProfileScreen";
import AdminLoginScreen from "./screens/AdminLoginScreen";

const Stack = createNativeStackNavigator();

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
    return (
        <NavigationContainer>
            <AllScreens/>
        </NavigationContainer>
    );
};
