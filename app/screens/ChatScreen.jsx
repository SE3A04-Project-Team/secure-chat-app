import {SafeAreaView, ScrollView, Text, TextInput, View} from "react-native";
import Icon from "react-native-vector-icons/FontAwesome";
import SlidingModal from "../components/SlidingModal";
import {useState} from "react";
import TextButton from "../components/TextButton";
import IconButton from "../components/IconButton";
import InitialIcon from "../components/InitialIcon";

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
            <SafeAreaView className="bg-gray-100">
                <View className="flex-row justify-between items-start content-center p-4 ">
                    <IconButton icon={<Icon name="arrow-left" size={32} color="#86efac"/>} onPress={() => navigation.goBack()}/>
                    <View className="flex flex-col justify-center items-center">
                        <InitialIcon name={chat.name}/>
                        <Text className="text-black text-md text-center">{chat.name}</Text>
                    </View>
                    <IconButton icon={<Icon name="gear" size={32} color="#86efac"/>} onPress={() => setModalVisible(true)}/>
                </View>
            </SafeAreaView>
            <View className="bg-primary rounded-t-3xl flex-grow">
                <ScrollView className="p-2">
                    <View className="flex flex-col justify-center items-center">
                        {
                            chatMessages.map((message) => (
                                <View
                                    key={message.messageID}
                                    className={`p-4 my-2 rounded-2xl max-w-3/4 ${message.senderID === currentUserID ? 'bg-green-300 self-end' : 'bg-gray-200 self-start'}`}
                                >
                                    <Text
                                        className={`text-primary text-md font-normal ${message.senderID === currentUserID ? 'text-white' : 'text-black'}`}
                                    >{message.message}</Text>
                                </View>
                            ))
                        }
                    </View>
                </ScrollView>
            </View>
            {/*TODO: Fix message input field, it currently gets covered by keyboard*/}
            <SafeAreaView className="flex flex-col z-40 w-full bg-gray-100">
                <View className="flex flex-row justify-between items-center content-center px-4 pt-2">
                    <TextInput
                        placeholder="Message"
                        className="flex-grow p-3 mx-2 bg-white border-2 border-gray-300 rounded-full"
                    />
                </View>
            </SafeAreaView>
            <SlidingModal modalVisible={modalVisible} setModalVisible={setModalVisible}>
                <View className="m-8">
                    <TextButton onPress={() => handleLeaveChat} title="Leave Chat"/>
                </View>
            </SlidingModal>
        </View>
    );
};

export default ChatScreen;
