import {SafeAreaView, ScrollView, Text, TouchableOpacity, View} from "react-native";
import Icon from 'react-native-vector-icons/FontAwesome';

const ChatSelectionScreen = ({ navigation }) => {

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

    return (
        <SafeAreaView className="flex-1 items-center justify-start">
            <Text className="flex text-4xl font-bold py-4">Chat Selection</Text>
            <ScrollView className="flex w-full">
                <View className="flex flex-col gap-y-2 w-full justify-center items-center">
                    {
                        chatData.map((chat) => (
                            <TouchableOpacity key={chat.id} className="flex flex-row w-full p-4 content-center items-center">
                                <View className="w-10 h-10 rounded-full border-2 border-black flex justify-center items-center bg-black">
                                    <Text className="text-xl font-bold text-white">{getInitials(chat.name)}</Text>
                                </View>
                                <Text className="flex-grow text-lg mx-2">{chat.name}</Text>
                                <Icon name="angle-right" size={24} color="black" className="self-end"/>
                            </TouchableOpacity>
                        ))
                    }
                </View>
            </ScrollView>
        </SafeAreaView>
    );
};

export default ChatSelectionScreen;
