import {KeyboardAvoidingView, Platform, SafeAreaView, ScrollView, Text, TextInput, View} from "react-native";
import Icon from "react-native-vector-icons/FontAwesome";
import SlidingModal from "../components/SlidingModal";
import {useEffect, useRef, useState} from "react";
import TextButton from "../components/TextButton";
import IconButton from "../components/IconButton";
import InitialIcon from "../components/InitialIcon";
import axios from "axios";
import {encryptAES} from "../utils/encryptionUtils";

const ChatScreen = ({route, navigation}) => {
    // Server URL
    const serverUrl = process.env.EXPO_PUBLIC_SERVER_URL;
    // Specific chat id and name passed as route params, used to fetch chat messages
    const {room_id, room_name} = route.params;
    // Sample current user ID
    const currentUserID = '1fPITEfiegat5F0xwXR9';
    // Sample key for encryption
    const key = '12345678901234567890123456789012';


    const [chatInfo, setChatInfo] = useState({
        room_id: "",
        room_name: "",
        messages: [
          {
            content: "",
            sender: {
              name: { name: "" },
              userID: ""
            },
            timestamp: 0
          }
        ]
      });

    // Fetch chat messages data from the server
    useEffect(() => {
        const getRoomData = async () => {
            try {
                const response = await axios.post(`${serverUrl}/message_server/message_history`, {
                    roomID: room_id,
                });
                console.log(response.data);
                setChatInfo(response.data);
                return response.data; // Returning data for further processing if needed
            } catch (error) {
                console.error('Error:', error);
            }
        }
        getRoomData();
    } , [])

    // Sample chat messages data
    const chatMessages = [
        {
            messageID: 1,
            senderID: 1,
            message: 'Hello, how are you?',
            timeStamp: '2024-04-03T18:25:43.511Z', // ISO 8601 format
        },
        {
            messageID: 2,
            senderID: 2,
            message: 'I am good, thank you!',
            timeStamp: '2024-04-01T18:25:43.511Z', // ISO 8601 format
        },
        {
            messageID: 3,
            senderID: 2,
            message: 'Ayo!',
            timeStamp: '2024-04-03T18:25:43.511Z', // ISO 8601 format
        },
        {
            messageID: 4,
            senderID: 2,
            message: 'How are you doing?',
            timeStamp: '2024-04-03T18:25:43.511Z', // ISO 8601 format
        },
        {
            messageID: 5,
            senderID: 1,
            message: 'I am doing well, thank you!\nTesting multiline message.',
            timeStamp: '2024-04-03T18:25:43.511Z', // ISO 8601 format
        },
        {
            messageID: 6,
            senderID: 2,
            message: 'Good to hear!',
            timeStamp: '2024-04-01T18:25:43.511Z', // ISO 8601 format
        },
        {
            messageID: 7,
            senderID: 1,
            message: 'Hi there!',
            timeStamp: '2024-03-07T18:25:43.511Z', // ISO 8601 format
        },
        {
            messageID: 8,
            senderID: 2,
            message: 'Hello!',
            timeStamp: '2024-03-07T18:25:43.511Z', // ISO 8601 format
        },
        {
            messageID: 9,
            senderID: 1,
            message: 'How are you doing?',
            timeStamp: '2024-03-07T18:25:43.511Z', // ISO 8601 format
        },
        {
            messageID: 10,
            senderID: 2,
            message: 'I am doing well, thank you!',
            timeStamp: '2024-03-07T18:25:43.511Z', // ISO 8601 format
        },
        {
            messageID: 11,
            senderID: 1,
            message: 'Good to hear!',
            timeStamp: '2024-03-07T18:25:43.511Z', // ISO 8601 format
        },
        {
            messageID: 12,
            senderID: 2,
            message: 'Hi there!',
            timeStamp: '2024-03-07T18:25:43.511Z', // ISO 8601 format
        },
        {
            messageID: 13,
            senderID: 1,
            message: 'Hello!',
            timeStamp: '2024-03-07T18:25:43.511Z', // ISO 8601 format
        },
        {
            messageID: 14,
            senderID: 2,
            message: 'How are you doing?',
            timeStamp: '2024-03-07T18:25:43.511Z', // ISO 8601 format
        },
        {
            messageID: 15,
            senderID: 1,
            message: 'I am doing well, thank you!',
            timeStamp: '2024-03-07T18:25:43.511Z', // ISO 8601 format
        },
        {
            messageID: 16,
            senderID: 2,
            message: 'Good to hear!',
            timeStamp: '2024-03-07T18:25:43.511Z', // ISO 8601 format
        },
        {
            messageID: 17,
            senderID: 1,
            message: 'Hi there!',
            timeStamp: '2024-03-07T18:25:43.511Z', // ISO 8601 format
        },
        {
            messageID: 18,
            senderID: 2,
            message: 'Hello!',
            timeStamp: '2024-03-07T18:25:43.511Z', // ISO 8601 format
        },
        {
            messageID: 19,
            senderID: 1,
            message: 'How are you doing?',
            timeStamp: '2024-03-07T18:25:43.511Z', // ISO 8601 format
        },
        {
            messageID: 20,
            senderID: 2,
            message: 'I am doing well, thank you!',
            timeStamp: '2024-03-07T18:25:43.511Z', // ISO 8601 format
        },
        {
            messageID: 21,
            senderID: 1,
            message: 'Good to hear!',
            timeStamp: '2024-03-07T18:25:43.511Z', // ISO 8601 format
        },
        {
            messageID: 22,
            senderID: 2,
            message: 'Hi there!',
            timeStamp: '2024-03-07T18:25:43.511Z', // ISO 8601 format
        },
        {
            messageID: 23,
            senderID: 1,
            message: 'Hello!',
            timeStamp: '2024-03-07T18:25:43.511Z', // ISO 8601 format
        },
        {
            messageID: 24,
            senderID: 2,
            message: 'How are you doing?',
            timeStamp: '2024-03-07T18:25:43.511Z', // ISO 8601 format
        },
        {
            messageID: 25,
            senderID: 1,
            message: 'I am doing well, thank you!',
            timeStamp: '2024-03-07T18:25:43.511Z', // ISO 8601 format
        },
        {
            messageID: 26,
            senderID: 2,
            message: 'Good to hear!',
            timeStamp: '2024-03-07T18:25:43.511Z', // ISO 8601 format
        },
        {
            messageID: 27,
            senderID: 1,
            message: 'Hi there!',
            timeStamp: '2024-03-07T18:25:43.511Z', // ISO 8601 format
        },
        {
            messageID: 28,
            senderID: 2,
            message: 'Hello!',
            timeStamp: '2024-03-07T18:25:43.511Z', // ISO 8601 format
        },
        {
            messageID: 29,
            senderID: 1,
            message: 'How are you doing?',
            timeStamp: '2024-03-07T18:25:43.511Z', // ISO 8601 format
        },
        {
            messageID: 30,
            senderID: 2,
            message: 'I am doing well, thank you!',
            timeStamp: '2024-03-07T18:25:43.511Z', // ISO 8601 format
        },
        {
            messageID: 31,
            senderID: 1,
            message: 'Good to hear!',
            timeStamp: '2024-03-07T18:25:43.511Z', // ISO 8601 format
        },
    ];

    // Modal visibility state
    const [modalVisible, setModalVisible] = useState(false);

    // Message input state
    const [message, setMessage] = useState('');

    // Function to handle leaving the chat
    const handleLeaveChat = () => {
        // TODO: Implement leave chat functionality

        // Navigate back to the chat selection screen
        navigation.goBack();
    }

    // Function to handle sending a message
    const handleSendMessage = () => {
        // Encrypt the message using AES encryption
        setMessage(encryptAES(message, key));

        // Send the message to the server
        const sendMessage = async () => {
            try {
                const response = await axios.post(`${SERVER_URL}/sendMessage`, {
                    userId: currentUserID,
                    roomId: chat.roomID,
                    message: message,
                });
                console.log(response.data);
                return response.data;
            } catch (error) {
                console.error('Error:', error);
            }
        }
        // Call the sendMessage function
        sendMessage();
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
                            <InitialIcon name={room_name}/>
                            <Text className="text-black text-md text-center">{room_name}</Text>
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
                    <View className="flex flex-col items-center mb-3">
                        {chatInfo.messages.map((message, index) => (
                            <View
                                key={index} // You can use index as key if messageID is not unique
                                className={`flex flex-col max-w-3/4 ${message.sender.userID === currentUserID ? 'self-end' : 'self-start'} ${index > 0 && chatInfo.messages[index - 1].sender.userID === message.sender.userID ? 'mt-0.5' : 'mt-3'}`}
                            >
                                <View
                                className={`flex py-2 px-3 rounded-2xl max-w-fit ${message.sender.userID === currentUserID ? 'bg-green-300' : 'bg-gray-200'}`}
                                >
                                <Text
                                    className={`text-primary text-md font-normal ${message.sender.userID === currentUserID ? 'text-white' : 'text-black'}`}
                                >
                                    {message.content}
                                </Text>
                                </View>
                                {/* Uncomment below section when timeStamp is available */}
                                {/* <Text className={`text-gray-500 text-xs mt-0.5 ${message.sender.userID === currentUserID ? 'self-end' : 'self-start'}`}>
                                    {message.timestamp}
                                    </Text> */}
                            </View>
                            ))
                        }
                    </View>

                </ScrollView>
                <SafeAreaView className="flex-row justify-between items-center content-center bg-gray-100">
                    <View className="flex-row justify-between flex-grow mx-6 my-2 bg-white border border-gray-300 rounded-3xl max-h-40">
                        <TextInput
                            placeholder="Message"
                            multiline={true}
                            className="flex-1 text-black text-md bg-transparent mr-8 p-4"
                            value={message}
                            onChangeText={(text) => setMessage(text)}
                        />
                        {
                            !(message === '') &&
                            <IconButton
                                icon={<Icon name="send" size={20} color="#FFFFFF"/>}
                                onPress={handleSendMessage}
                                opacityStyle={"p-2 bg-accent rounded-full"}
                                containerStyle={"flex justify-end p-1.5"}
                            />
                        }
                    </View>
                </SafeAreaView>
                <SlidingModal modalVisible={modalVisible} setModalVisible={setModalVisible}>
                    <SafeAreaView className="flex flex-col m-8 justify-start h-full">
                        <TextButton onPress={handleLeaveChat} title="Leave Chat"/>
                    </SafeAreaView>
                </SlidingModal>
            </View>
        </KeyboardAvoidingView>
    );
};

export default ChatScreen;
