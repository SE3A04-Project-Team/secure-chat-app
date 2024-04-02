import {ScrollView, Text, View} from "react-native";
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
        <View className="flex-1 min-h-screen bg-accent justify-start">
            <View className="flex-1 flex-row justify-between items-center content-center px-8">
                <IconButton icon={<Icon name="arrow-left" size={32} color="white"/>}/>
                <Text className="text-white text-xl font-extrabold text-center">{chat.name}</Text>
                <IconButton icon={<Icon name="gear" size={32} color="white"/>} onPress={() => setModalVisible(true)}/>
            </View>
            <View className="bg-primary rounded-t-3xl h-4/5">
                <ScrollView className="p-2">
                    <View className="flex flex-col justify-center items-center">
                        {
                            chatMessages.map((message) => (
                                <>
                                    {
                                        message.senderID === currentUserID ?
                                            <View key={message.messageID} className="bg-primary p-4 my-2 rounded-full w-3/4 self-end">
                                                <Text className="text-white">{message.message}</Text>
                                            </View>
                                            :
                                            <View key={message.messageID} className="bg-secondary p-4 my-2 rounded-full w-3/4 self-start">
                                                <Text className="text-black">{message.message}</Text>
                                            </View>
                                    }
                                </>
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
