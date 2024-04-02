import {View, Text, SafeAreaView, ScrollView} from "react-native";
import Icon from "react-native-vector-icons/FontAwesome";
import SlidingModal from "../components/SlidingModal";
import {useState} from "react";
import TextButton from "../components/TextButton";
import IconButton from "../components/IconButton";

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

    const [modalVisible, setModalVisible] = useState(false);

    const handleLeaveChat = () => {
        // TODO: Implement leave chat functionality
    }

    return (
        <SafeAreaView>
            <View className="flex flex-row justify-between items-center content-center mb-8 px-6">
                <IconButton icon={<Icon name="arrow-left" size={24} color="black"/>}/>
                <Text className="flex-grow font-bold text-xl ml-4">{chat.name}</Text>
                <IconButton icon={<Icon name="gear" size={24} color="black"/>} onPress={() => setModalVisible(true)}/>
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
            <SlidingModal modalVisible={modalVisible} setModalVisible={setModalVisible}>
                <View className="m-8">
                    <TextButton onPress={() => handleLeaveChat} title="Leave Chat"/>
                </View>
            </SlidingModal>
        </SafeAreaView>
    );
};

export default ChatScreen;
