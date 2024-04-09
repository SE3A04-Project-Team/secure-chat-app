import React, {useState, useContext} from 'react';
import {UserContext} from '../contexts/UserContext';
import {
    Keyboard,
    KeyboardAvoidingView,
    Platform,
    SafeAreaView,
    Text,
    TextInput,
    TouchableWithoutFeedback,
    View
} from 'react-native';
import TextButton from '../components/TextButton';
import axios from "axios";

const UserLoginScreen = ({navigation}) => {

    // Server URL
    const SERVER_URL = process.env.SERVER_URL;

    const { loginUser } = useContext(UserContext);

    // Login credentials
    const [formData, setFormData] = useState({
        email: '',
        password: '',
    });

    // Handle login input field change
    const handleInputChange = (name, value) => {
        setFormData({
            ...formData,
            [name]: value,
        });
    };

    // Handle login button press
    const handleLogin = () => {
        // TODO: Add login logic here
        // Here you can perform login logic using formData
        // For example, you can send formData to your backend for authentication
        const auth = async () => {
            try {
                const response = await axios.post(`${SERVER_URL}/message_server/auth`, {
                    email: formData.email,
                    password: formData.password,
                });
                console.log(response.data);
                return response.data; // Returning data for further processing if needed
            } catch (error) {
                console.error('Error:', error);
            }
        }

        if (loginUser(formData.email, formData.password)) {
            // After successful login, you can navigate to the next screen
            navigation.navigate("ChatSelectionScreen");
        } else {
            // Handle login failure
            console.log("Login failed");
        }
    };

    return (
        <KeyboardAvoidingView
            style={{ flex: 1 }}
            behavior={Platform.OS === "ios" ? "padding" : "height"}
        >
        <TouchableWithoutFeedback onPress={Keyboard.dismiss}>
            <View className="flex-1 bg-accent justify-end">
                <SafeAreaView className="flex-1 flex-col justify-evenly items-center content-center">
                    <Text className="text-primary text-6xl font-bold text-center">Chat App</Text>
                </SafeAreaView>
                <SafeAreaView className="bg-white rounded-t-3xl">
                    <View className="flex justify-center p-8 gap-y-8">
                        <Text className="text-secondary font-bold text-4xl text-center">User Login</Text>
                        <View className="flex flex-col gap-y-2">
                            <TextInput
                                className="p-4 text-secondary rounded-2xl bg-input_field"
                                placeholder="Email"
                                value={formData.email}
                                onChangeText={(text) => handleInputChange('email', text)}
                            />
                            <TextInput
                                className="p-4 text-secondary rounded-2xl bg-input_field"
                                placeholder="Password"
                                value={formData.password}
                                onChangeText={(text) => handleInputChange('password', text)}
                            />
                        </View>
                        <View className="">
                            <TextButton onPress={handleLogin} title={"Login"} testID="login-button"/>
                        </View>
                    </View>
                </SafeAreaView>
            </View>
        </TouchableWithoutFeedback>
        </KeyboardAvoidingView>
    );
};

export default UserLoginScreen;
