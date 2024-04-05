import {
    Keyboard,
    KeyboardAvoidingView,
    Platform,
    SafeAreaView,
    ScrollView,
    Text,
    TextInput,
    TouchableWithoutFeedback,
    View
} from "react-native";
import Icon from "react-native-vector-icons/FontAwesome";
import SlidingModal from "../components/SlidingModal";
import {useEffect, useRef, useState} from "react";
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
            senderID: 2,
            message: 'Ayo!',
        },
        {
            messageID: 4,
            senderID: 2,
            message: 'How are you doing?',
        },
        {
            messageID: 5,
            senderID: 1,
            message: 'I am doing well, thank you!\nTesting multiline message.',
        },
        {
            messageID: 6,
            senderID: 2,
            message: 'Good to hear!',
        },
        {
            messageID: 7,
            senderID: 1,
            message: 'Hi there!',
        },
        {
            messageID: 8,
            senderID: 2,
            message: 'Hello!',
        },
        {
            messageID: 9,
            senderID: 1,
            message: 'How are you doing?',
        },
        {
            messageID: 10,
            senderID: 2,
            message: 'I am doing well, thank you!',
        },
        {
            messageID: 11,
            senderID: 1,
            message: 'Good to hear!',
        },
        {
            messageID: 12,
            senderID: 2,
            message: 'Hi there!',
        },
        {
            messageID: 13,
            senderID: 1,
            message: 'Hello!',
        },
        {
            messageID: 14,
            senderID: 2,
            message: 'How are you doing?',
        },
        {
            messageID: 15,
            senderID: 1,
            message: 'I am doing well, thank you!',
        },
        {
            messageID: 16,
            senderID: 2,
            message: 'Good to hear!',
        },
        {
            messageID: 17,
            senderID: 1,
            message: 'Hi there!',
        },
        {
            messageID: 18,
            senderID: 2,
            message: 'Hello!',
        },
        {
            messageID: 19,
            senderID: 1,
            message: 'How are you doing?',
        },
        {
            messageID: 20,
            senderID: 2,
            message: 'I am doing well, thank you!',
        },
        {
            messageID: 21,
            senderID: 1,
            message: 'Good to hear!',
        },
        {
            messageID: 22,
            senderID: 2,
            message: 'Hi there!',
        },
        {
            messageID: 23,
            senderID: 1,
            message: 'Hello!',
        },
        {
            messageID: 24,
            senderID: 2,
            message: 'How are you doing?',
        },
        {
            messageID: 25,
            senderID: 1,
            message: 'I am doing well, thank you!',
        },
        {
            messageID: 26,
            senderID: 2,
            message: 'Good to hear!',
        },
        {
            messageID: 27,
            senderID: 1,
            message: 'Hi there!',
        },
        {
            messageID: 28,
            senderID: 2,
            message: 'Hello!',
        },
        {
            messageID: 29,
            senderID: 1,
            message: 'How are you doing?',
        },
        {
            messageID: 30,
            senderID: 2,
            message: 'I am doing well, thank you!',
        },
        {
            messageID: 31,
            senderID: 1,
            message: 'Good to hear!',
        },
    ]; // TODO: Query chat messages from backend using chat.id

    // Sample current user ID
    const currentUserID = 1; // TODO: Get the current user's ID from the authentication context

    // Modal visibility state
    const [modalVisible, setModalVisible] = useState(false);

    // Message input state
    const [message, setMessage] = useState('');

    // Function to handle leaving the chat
    const handleLeaveChat = () => {
        // TODO: Implement leave chat functionality
    }

    // Function to handle sending a message
    const handleSendMessage = () => {
        // TODO: Implement send message functionality

        // Clear the message input after sending the message
        setMessage('');
    }

    // ScrollView starts with most recent messages (at the bottom)
    const scrollViewRef = useRef(null);
    useEffect(() => {
        // Scrolls to the bottom of the ScrollView when it's initially rendered
        if (scrollViewRef.current) {
            scrollViewRef.current.scrollToEnd({ animated: false });
        }
    }, []);


    return (
        <KeyboardAvoidingView
            style={{ flex: 1 }}
            behavior={Platform.OS === "ios" ? "padding" : "height"}
        >
            <View className="flex-1 bg-primary justify-start">
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
                <ScrollView
                    className="px-3"
                    ref={scrollViewRef}
                    onLayout={() => {
                        // Scrolls to the bottom of the ScrollView when it's initially rendered
                        scrollViewRef.current.scrollToEnd({ animated: false });
                    }}
                >
                    <View className="flex flex-col items-center">
                        {
                            chatMessages.map((message) => (
                                <View
                                    key={message.messageID}
                                    className={`py-2 px-3 my-2 rounded-2xl max-w-3/4 ${message.senderID === currentUserID ? 'bg-green-300 self-end' : 'bg-gray-200 self-start'}`}
                                >
                                    <Text
                                        className={`text-primary text-md font-normal ${message.senderID === currentUserID ? 'text-white' : 'text-black'}`}
                                    >{message.message}</Text>
                                </View>
                            ))
                        }
                    </View>
                </ScrollView>
                <SafeAreaView className="flex flex-row justify-between items-center content-center bg-gray-100">
                    <View className="flex flex-row justify justify-between flex-grow p-3 mx-6 my-2 bg-white border border-gray-300 rounded-3xl max-w-full">
                        <TextInput
                            placeholder="Message"
                            multiline={true}
                            className="flex-1 text-black text-md bg-transparent pr-8"
                            value={message}
                            onChangeText={(text) => setMessage(text)}
                        />
                        <View className="absolute right-4 bottom-1/2">
                            {
                                !(message === '') &&
                                <IconButton
                                    icon={<Icon name="send" size={24} color="#86efac" />}
                                    onPress={handleSendMessage}
                                />
                            }
                        </View>
                    </View>
                </SafeAreaView>
                <SlidingModal modalVisible={modalVisible} setModalVisible={setModalVisible} height={0.3}>
                    <View className="flex flex-col p-8">
                        <TextButton title="Generate Report Screen" onPress={() => navigation.navigate("GenerateReportScreen")}/>
                        <TextButton onPress={() => handleLeaveChat} title="Leave Chat"/>
                    </View>
                </SlidingModal>
            </View>
        </KeyboardAvoidingView>
    );
};

export default ChatScreen;
