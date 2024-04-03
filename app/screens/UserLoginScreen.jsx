import React, {useState} from 'react';
import {SafeAreaView, Text, TextInput, TouchableOpacity, View} from 'react-native';
import TextButton from '../components/TextButton';
import Icon from "react-native-vector-icons/FontAwesome";

const UserLoginScreen = ({navigation}) => {

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
        <View className="flex-1 min-h-screen bg-accent justify-end">
            <View className="flex-1 flex-row justify-evenly items-center content-center">
                <Icon name="lock" size={64} color="white"/>
                <Text className="text-primary text-6xl font-bold text-center">Chat App</Text>
                <TextButton title="Generate Report Screen" onPress={() => navigation.navigate("GenerateReportScreen")}/>
            </View>
            <SafeAreaView className="bg-white rounded-t-3xl">
                <View className="flex justify-center py-8 gap-y-8">
                    <Text className="text-secondary font-bold text-4xl text-center py-4">User Login</Text>
                    <View className="flex flex-col gap-y-2 m-7">
                        <TextInput
                            className="p-4 text-secondary rounded-2xl bg-input_field"
                            placeholder="Email"
                            keyboardType="email-address"
                            value={formData.email}
                            onChangeText={(text) => handleInputChange('email', text)}
                        />
                        <TextInput
                            className="p-4 text-secondary rounded-2xl bg-input_field"
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
                        <TouchableOpacity onPress={() => navigation.navigate("AdminLoginScreen")}>
                            <Text className="text-accent">Login here</Text>
                        </TouchableOpacity>
                    </View>
                </View>
            </SafeAreaView>
        </View>
    );
};

export default UserLoginScreen;
