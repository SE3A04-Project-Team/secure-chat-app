import {Text, View} from "react-native";
import Icon from "react-native-vector-icons/FontAwesome";

const ProfileScreen = ({navigation}) => {

    // Sample profile data
    const profileData = {
        name: 'John Doe',
        email: 'johndoe@gmail.com',
        phone: '+1234567890',
    }; //TODO: Query current user profile data from backend

    return (
        <View className="flex-1 min-h-screen bg-accent justify-start">
            <View className="flex-1 flex-row justify-center items-center content-center">
                <Icon name="user" size={96} color="white"/>
            </View>
            <View className="bg-primary rounded-t-3xl h-3/5">
                {
                    Object.keys(profileData).map((key, index) => (
                        <View key={index} className="flex flex-col justify-between p-4 border-b border-gray-200">
                            <Text className="text-secondary font-light text-lg">{key}</Text>
                            <Text className="text-secondary font-semibold text-lg">{profileData[key]}</Text>
                        </View>
                    ))
                }
            </View>
        </View>
    );
};

export default ProfileScreen;
