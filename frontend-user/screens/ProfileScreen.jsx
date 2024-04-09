import {SafeAreaView, Text, View} from "react-native";
import Icon from "react-native-vector-icons/FontAwesome";
import TextButton from "../components/TextButton";
import IconButton from "../components/IconButton";
import axios from "axios";
import React, {useContext} from "react";
import {UserContext} from "../contexts/UserContext";

const ProfileScreen = ({navigation}) => {
    const {user, logoutUser} = useContext(UserContext);
    const SERVER_URL = process.env.SERVER_URL
    const getProfileData = async () => {
        try {
            const response = await axios.get(`${SERVER_URL}/data/profile`, {
                params: {
                    userID: user.id
                }
            });
            console.log(response.data);
            return response.data; // Returning data for further processing if needed
        } catch (error) {
            console.error('Error:', error);
        }
    }

    const handleLogout = () => {
        //TODO: add logic to logout user, clear session, etc.
        logoutUser();
        // Navigate to UserLoginScreen
        navigation.navigate('UserLoginScreen');
    }

    return (
        <View className="flex-1 min-h-screen bg-accent justify-start">
            <SafeAreaView className="">
                <View className="flex-row justify-between items-center content-center p-8">
                    <IconButton icon={<Icon name="arrow-left" size={32} color="white"/>} onPress={() => navigation.goBack()}/>
                </View>
            </SafeAreaView>
            <View className="flex-1 flex-row justify-center items-center content-center">
                <Icon name="user-o" size={96} color="white"/>
            </View>
            <View className="bg-primary rounded-t-3xl h-3/5 p-7 gap-y-4 flex flex-col">
                <Text className="text-secondary font-bold text-4xl text-center">{user.name}</Text>
                <View className="flex flex-col flex-grow">
                    {
                        Object.keys(user).map((key, index) => (
                            <View key={index}>
                                {key !== 'password' &&
                                <View className="flex flex-col justify-between border-b border-gray-200 py-4">
                                    <Text className="text-secondary font-light text-lg">{key}</Text>
                                    <Text className="text-secondary font-semibold text-lg">{user[key]}</Text>
                                </View>
                                }
                            </View>
                        ))
                    }
                </View>
                <TextButton onPress={handleLogout} title="Logout"/>
            </View>
        </View>
    );
};

export default ProfileScreen;
