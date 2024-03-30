import React, {useState} from 'react';
import {SafeAreaView, Text, TextInput, View} from 'react-native';
import TextButton from '../components/TextButton';

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
        <SafeAreaView testID="login-page" className="flex-1 bg-primary">
            <View className="flex-1 flex justify-center my-4">
                <Text className="text-secondary font-bold text-4xl text-center">Login</Text>
                <View className="flex flex-col gap-y-2 m-7">
                    <TextInput
                        className="p-4 text-secondary rounded-2xl"
                        placeholder="Email"
                        keyboardType="email-address"
                        value={formData.email}
                        onChangeText={(text) => handleInputChange('email', text)}
                    />
                    <TextInput
                        className="p-4 text-secondary rounded-2xl"
                        placeholder="Password"
                        secureTextEntry={true}
                        value={formData.password}
                        onChangeText={(text) => handleInputChange('password', text)}
                    />
                </View>
                <View className="space-y-4 mx-7">
                    <TextButton onPress={handleLogin} title={"Login"} testID="login-button"/>
                </View>
            </View>
        </SafeAreaView>
    );
};

export default LoginScreen;
