import {View, Text, SafeAreaView, ScrollView, Button, TouchableOpacity} from "react-native";
import Icon from "react-native-vector-icons/FontAwesome";

const ChatScreen = ({route, navigation}) => {
    const {chat} = route.params;

    // Sample chat messages data
    const chatMessages = [
        {
            messageID: 1,
            senderID: 1,
            message: 'Hello, how are you?',
        },
        {
            messageID: 2,
            senderID: 2,
            message: 'I am good, thank you!',
        },
        {
            messageID: 3,
            senderID: 1,
            message: 'That\'s great to hear!',
        },
    ]; // TODO: Query chat messages from backend using chat.id

    // Sample current user ID, this is used for determining the message sender for styling
    const currentUserID = 1; // TODO: Get the current user's ID from the authentication context

    return (
        <SafeAreaView>
            <View className="flex flex-row justify-between items-center content-center gap-4 mb-8">
                <TouchableOpacity className="p-4">
                    <Icon name="arrow-left" size={24} color="black"/>
                </TouchableOpacity>
                <Text className="flex-grow font-bold text-xl">{chat.name}</Text>
                <TouchableOpacity className="px-4">
                    <Icon name="gear" size={24} color="black"/>
                </TouchableOpacity>
            </View>
            <ScrollView className="p-2">
                <View className="flex flex-col gap-y-4 justify-center items-center">
                    {
                        chatMessages.map((message) => (
                            <View key={message.messageID} className={message.senderID === currentUserID ? "bg-blue-500 p-2 rounded-lg w-3/4 self-end" : "bg-gray-300 p-2 rounded-lg w-3/4 self-start"}>
                                <Text className={message.senderID === currentUserID ? "text-white" : "text-black"}>{message.message}</Text>
                            </View>
                        ))
                    }
                </View>
            </ScrollView>
        </SafeAreaView>
    );
};

export default ChatScreen;
