import {SafeAreaView, ScrollView, Text, TouchableOpacity, View} from "react-native";
import Icon from 'react-native-vector-icons/FontAwesome';

const ChatSelectionScreen = ({ navigation }) => {

    // TODO: Query chat data (only name and id) from backend

    // Sample JSON data for chat selection
    const chatData = [
        {
            id: 1,
            name: 'John Doe',
        },
        {
            id: 2,
            name: 'Jane Doe',
        },
        {
            id: 3,
            name: 'Alice',
        },
        {
            id: 4,
            name: 'Bob',
        },
        {
            id: 5,
            name: 'Charlie',
        },
        {
            id: 6,
            name: 'David',
        },
        {
            id: 7,
            name: 'Eve',
        },
        {
            id: 8,
            name: 'Frank',
        },
        {
            id: 9,
            name: 'Grace',
        },
        {
            id: 10,
            name: 'Henry',
        },
        {
            id: 11,
            name: 'Ivy',
        },
        {
            id: 12,
            name: 'Jack',
        },
        {
            id: 13,
            name: 'Katie',
        },
        {
            id: 14,
            name: 'Liam',
        },
        {
            id: 15,
            name: 'Mia',
        }
    ];

    const getInitials = (name) => {
        const nameArray = name.split(" ");
        return nameArray.map(word => word[0]).join("").toUpperCase();
    };

    const handleChatSelection = (chat) => {
        // Handle chat selection logic here
        // For example, you can navigate to the chat screen
        navigation.navigate("ChatScreen", { chat });
    }

    return (
        <View className="flex-1 min-h-screen bg-green-300 justify-start">
            <View className="flex-1 flex-row justify-between items-center content-center px-8">
                <Icon name="plus" size={32} color="white"/>
                <Text className="text-white text-xl font-extrabold text-center">Home</Text>
                <Icon name="user" size={32} color="white"/>
            </View>
            <View className="bg-white rounded-t-3xl h-4/5">
                <ScrollView className="p-2">
                    <View className="flex flex-col gap-y-2 justify-center items-center">
                        {
                            chatData.map((chat) => (
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
    );
};

export default ChatSelectionScreen;
