import {SafeAreaView, ScrollView, Text, View} from "react-native";
import Icon from "react-native-vector-icons/FontAwesome";
import SlidingModal from "../components/SlidingModal";
import {useState} from "react";
import TextButton from "../components/TextButton";
import IconButton from "../components/IconButton";

const ChatScreen = ({route, navigation}) => {
    // Specific chat id and name passed as route params
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

    const [modalVisible, setModalVisible] = useState(false);

    const handleLeaveChat = () => {
        // TODO: Implement leave chat functionality
    }

    return (
        <View className="flex-1 min-h-screen bg-primary justify-start">
            <View className="flex-1 flex-row justify-between items-center content-center px-8">
                <IconButton icon={<Icon name="arrow-left" size={32} color="black"/>} onPress={() => navigation.goBack()}/>
                <Text className="text-secondary text-xl font-extrabold text-center">{chat.name}</Text>
                <IconButton icon={<Icon name="gear" size={32} color="black"/>} onPress={() => setModalVisible(true)}/>
            </View>
            <View className="bg-primary rounded-t-3xl h-4/5">
                <ScrollView className="p-2">
                    <View className="flex flex-col justify-center items-center">
                        {
                            chatMessages.map((message) => (
                                <View
                                    key={message.messageID}
                                    className={`p-4 my-2 rounded-full max-w-3/4 ${message.senderID === currentUserID ? 'bg-gray-700 self-end' : 'bg-indigo-700 self-start'}`}
                                >
                                    <Text className="text-primary text-md font-medium">{message.message}</Text>
                                </View>
                            ))
                        }
                    </View>
                </ScrollView>
            </View>
            <SlidingModal modalVisible={modalVisible} setModalVisible={setModalVisible}>
                <View className="m-8">
                    <TextButton onPress={() => handleLeaveChat} title="Leave Chat"/>
                </View>
            </SlidingModal>
        </View>
    );
};

export default ChatScreen;
