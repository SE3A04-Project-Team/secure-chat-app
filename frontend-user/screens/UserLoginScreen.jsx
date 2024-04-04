import React, {useEffect, useState} from 'react';
import {
    SafeAreaView,
    Text,
    TextInput,
    View,
    KeyboardAvoidingView,
    Platform,
    TouchableWithoutFeedback, Keyboard
} from 'react-native';
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

    const [isKeyboardVisible, setKeyboardVisible] = useState(false);

    useEffect(() => {
        const keyboardDidShowListener = Keyboard.addListener(
            'keyboardDidShow',
            () => {
                setKeyboardVisible(true); // Keyboard is visible
            }
        );
        const keyboardDidHideListener = Keyboard.addListener(
            'keyboardDidHide',
            () => {
                setKeyboardVisible(false); // Keyboard is hidden
            }
        );

        // Cleanup function
        return () => {
            keyboardDidShowListener.remove();
            keyboardDidHideListener.remove();
        };
    }, []);

    return (
        <KeyboardAvoidingView
            style={{ flex: 1 }}
            behavior={Platform.OS === "ios" ? "padding" : "height"}
        >
        <TouchableWithoutFeedback onPress={Keyboard.dismiss}>
        <View className="flex-1 bg-accent justify-end">
            {
                !isKeyboardVisible &&
                <View className="flex-1 flex-col justify-evenly items-center content-center">
                    <Text className="text-primary text-6xl font-bold text-center">Chat App</Text>
                    {/*<TextButton title="Generate Report Screen" onPress={() => navigation.navigate("GenerateReportScreen")}/>*/}
                </View>
            }
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
                </View>
            </SafeAreaView>
        </View>
        </TouchableWithoutFeedback>
        </KeyboardAvoidingView>
    );
};

export default UserLoginScreen;
