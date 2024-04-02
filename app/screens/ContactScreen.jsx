import {ScrollView, Text, TouchableOpacity, View} from "react-native";
import Icon from "react-native-vector-icons/FontAwesome";

const ContactScreen = () => {

    const contactData = {

    }

    return (
        <View className="flex-1 min-h-screen bg-accent justify-start">
            <View className="flex-1 flex-row justify-between items-center content-center px-8">
                <Icon name="plus" size={32} color="white"/>
                <Text className="text-white text-xl font-extrabold text-center">Home</Text>
                <Icon name="user" size={32} color="white"/>
            </View>
            <View className="bg-primary rounded-t-3xl h-4/5">
                <ScrollView className="p-2">
                    <View className="flex flex-col gap-y-2 justify-center items-center">
                        {
                            contactData.map((chat) => (
                                <TouchableOpacity key={chat.id} onPress={() => handleChatSelection(chat)} className="flex flex-row w-full p-4 content-center items-center">
                                    <View className="w-10 h-10 rounded-full flex justify-center items-center bg-black">
                                        <Text className="text-xl font-bold text-white">{getInitials(chat.name)}</Text>
                                    </View>
                                    <Text className="flex-grow text-lg mx-2">{chat.name}</Text>
                                    <Icon name="angle-right" size={24} color="black" className="self-end"/>
                                </TouchableOpacity>
                            ))
                        }
                    </View>
                </ScrollView>
            </View>
        </View>
    )
}

export default ContactScreen;
