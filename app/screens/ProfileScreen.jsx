import {SafeAreaView, Text, View} from "react-native";
import Icon from "react-native-vector-icons/FontAwesome";
import TextButton from "../components/TextButton";
import IconButton from "../components/IconButton";

const ProfileScreen = ({navigation}) => {

    // Sample profile data
    const profileData = {
        name: 'John Doe',
        email: 'johndoe@gmail.com',
        phone: '+1234567890',
    }; //TODO: Query current user profile data from backend

    const handleLogout = () => {
        //TODO: add logic to logout user, clear session, etc.

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
                <Icon name="user" size={96} color="white"/>
            </View>
            <View className="bg-primary rounded-t-3xl h-3/5 p-7 gap-y-4 flex flex-col">
                <Text className="text-secondary font-bold text-4xl text-center">{profileData.name}</Text>
                <View className="flex flex-col flex-grow">
                    {
                        Object.keys(profileData).map((key, index) => (
                            <View key={index} className="flex flex-col justify-between border-b border-gray-200 py-4">
                                <Text className="text-secondary font-light text-lg">{key}</Text>
                                <Text className="text-secondary font-semibold text-lg">{profileData[key]}</Text>
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
