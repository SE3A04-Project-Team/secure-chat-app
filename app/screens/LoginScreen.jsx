import React, {useState} from 'react';
import {SafeAreaView, Text, TextInput, TouchableOpacity, View} from 'react-native';
import TextButton from '../components/TextButton';
import Icon from "react-native-vector-icons/FontAwesome";

const LoginScreen = ({navigation}) => {

    const [formData, setFormData] = useState({
        email: '',
        password: '',
    });

    const handleInputChange = (name, value) => {
        setFormData({
            ...formData,
            [name]: value,
        });
    };

    const handleLogin = () => {
        // Here you can perform login logic using formData
        // For example, you can send formData to your backend for authentication
        // After successful login, you can navigate to the next screen
        navigation.navigate("ChatSelectionScreen");
    };

    return (
        <View className="flex-1 min-h-screen bg-green-300 justify-end">
            <View className="flex-1 flex-row justify-center items-center content-center gap-x-4">
                <Icon name="lock" size={64} color="white" className="self-end"/>
                <Text className="text-white text-6xl font-bold text-center py-4">Chat App</Text>
            </View>
            <SafeAreaView testID="login-page" className="bg-white rounded-t-3xl">
                <View className="flex justify-center py-8 gap-y-8">
                    <Text className="text-secondary font-bold text-4xl text-center py-4">User Login</Text>
                    <View className="flex flex-col gap-y-2 m-7">
                        <TextInput
                            className="p-4 text-secondary rounded-2xl bg-gray-100"
                            placeholder="Email"
                            keyboardType="email-address"
                            value={formData.email}
                            onChangeText={(text) => handleInputChange('email', text)}
                        />
                        <TextInput
                            className="p-4 text-secondary rounded-2xl bg-gray-100"
                            placeholder="Password"
                            secureTextEntry={true}
                            value={formData.password}
                            onChangeText={(text) => handleInputChange('password', text)}
                        />
                    </View>
                    <View className="space-y-4 mx-7">
                        <TextButton onPress={handleLogin} title={"Login"} testID="login-button"/>
                    </View>
                    <View className="flex flex-row justify-center text-lg font-semibold">
                        <Text>Admin Member? </Text>
                        <TouchableOpacity>
                            <Text className="text-green-300">Login here</Text>
                        </TouchableOpacity>
                    </View>
                </View>
            </SafeAreaView>
        </View>
    );
};

export default LoginScreen;
