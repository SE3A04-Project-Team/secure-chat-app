import {KeyboardAvoidingView, Platform, SafeAreaView, ScrollView, Text, TextInput, View} from "react-native";
import Icon from "react-native-vector-icons/FontAwesome";
import SlidingModal from "../components/SlidingModal";
import {useEffect, useRef, useState} from "react";
import TextButton from "../components/TextButton";
import IconButton from "../components/IconButton";
import InitialIcon from "../components/InitialIcon";
import axios from "axios";
import {encryptAES} from "../utils/encryptionUtils";
import {formatPythonTimeString, pythonTime} from "../utils/dateUtils";
import io from "socket.io-client";

const ChatScreen = ({route, navigation}) => {
    // Server URL
    const serverUrl = process.env.EXPO_PUBLIC_SERVER_URL;
    // Specific chat id and name passed as route params, used to fetch chat messages
    const {room_id, room_name} = route.params;
    // Sample current user ID
    const currentUserID = '1fPITEfiegat5F0xwXR9';
    // Sample key for encryption
    const key = '12345678901234567890123456789012';
    // Modal visibility state
    const [modalVisible, setModalVisible] = useState(false);
    // Message input state
    const [message, setMessage] = useState('');
    // Chat messages state
    const [chatMessages, setchatMessages] = useState(
        // {messages: [{
        //     content: "",
        //     sender: "",
        //     timestamp: 0
        // }]}
        null
    );

    // Connect to the socket server when the component mounts
    const socketRef = useRef(null);
    useEffect(() => {
        socketRef.current = io(serverUrl);
        // Listen for incoming messages
        socketRef.current.on('receive_message', (newMessage) => {
            setchatMessages(prevState => ({
                ...prevState,
                messages: [...prevState.messages, newMessage]
            }));
        });
        // Disconnect from the socket server when the component unmounts
        return () => {if (socketRef.current) {socketRef.current.disconnect()}};
    }, []);

    // Fetch chat messages data from the server
    useEffect(() => {
        const getRoomData = async () => {
            try {
                const response = await axios.post(`${serverUrl}/message_server/message_history`, {
                    roomID: room_id,
                });
                setchatMessages(response.data);
                return response.data; // Returning data for further processing if needed
            } catch (error) {console.error('Error:', error)}
        }
        getRoomData();
    } , [])

    // Send a message to the server socket
    const handleSendMessage = () => {
        if (socketRef.current) {
            // Encrypt the message using AES encryption
            // const encryptedMessage = encryptAES(message, key);
            // Emit the message to the server
            socketRef.current.emit('send_message', currentUserID, room_id, pythonTime(), message);
            // Clear the message input after sending the message
            setMessage('');
        }
    };

    // Function to handle leaving the chat
    const handleLeaveChat = () => {
        // TODO: Implement leave chat functionality
        // Navigate back to the chat selection screen
        navigation.goBack();
    }

    // ScrollView starts with most recent messages (at the bottom)
    const scrollViewRef = useRef(null);
    const scrollToBottom = () => {if (scrollViewRef.current) {scrollViewRef.current.scrollToEnd({ animated: true })}};

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
                            <Text numberOfLines={1} ellipsizeMode="tail" className="text-black text-md text-center">{room_name}</Text>
                        </View>
                        <IconButton icon={<Icon name="gear" size={32} color="#86efac"/>} onPress={() => setModalVisible(true)}/>
                    </View>
                </SafeAreaView>
                <ScrollView
                    className="px-3"
                    ref={scrollViewRef}
                    onContentSizeChange={scrollToBottom}
                    onLayout={() => {scrollViewRef.current.scrollToEnd({ animated: false })}}
                >
                    <View className="flex flex-col items-center mb-3">
                        {chatMessages &&
                            chatMessages.messages.map((message, index) => (
                                <View
                                    key={index} // You can use index as key if messageID is not unique
                                    className={`flex flex-col max-w-3/4 ${message.sender === currentUserID ? 'self-end' : 'self-start'} ${index > 0 && chatMessages.messages[index - 1].sender.userID === message.sender ? 'mt-0.5' : 'mt-3'}`}
                                >
                                    <View className={`flex py-2 px-3 rounded-2xl max-w-fit ${message.sender === currentUserID ? 'bg-green-300' : 'bg-gray-200'}`}>
                                        <Text className={`text-primary text-md font-normal ${message.sender === currentUserID ? 'text-white' : 'text-black'}`}>
                                            {message.content}
                                        </Text>
                                    </View>
                                    <Text className={`text-gray-500 text-xs mt-0.5 ${message.sender === currentUserID ? 'self-end' : 'self-start'}`}>
                                        {formatPythonTimeString(message.timestamp)}
                                    </Text>
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
                        {!(message === '') &&
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
