import {SafeAreaView, ScrollView, Text, TouchableOpacity, View, FlatList} from "react-native";
import Icon from 'react-native-vector-icons/FontAwesome';
import IconButton from "../components/IconButton";
import {formatDate} from "../utils/dateUtils";
import InitialIcon from "../components/InitialIcon";
import {useEffect, useState} from "react";
import SlidingModal from "../components/SlidingModal";
import axios from "axios";
import BouncyCheckbox from "react-native-bouncy-checkbox";
import TextButton from "../components/TextButton";


const ChatSelectionScreen = ({ navigation }) => {

    const serverUrl = process.env.EXPO_PUBLIC_SERVER_URL;
    const currentUserId = '1fPITEfiegat5F0xwXR9'; // User ID for which chats are to be fetched
    useEffect(() => {
        const getRoomsData = async () => {
            try {
                const response = await axios.get(`${serverUrl}/data/chat_selection`, {
                    params: {
                        userId: currentUserId, // User ID for which chats are to be fetched
                    }
                    });
                console.log(response.data);
                return response.data; // Returning data for further processing if needed
            } catch (error) {
                console.error('Error:', error);
            }
        };

        getRoomsData();

    }, []);


    // Sample JSON data for chat selection
    const chatData = [
        {
            id: 1,
            name: 'John Doe',
            timeOfLastMessage: '2024-04-03T18:25:43.511Z', // ISO 8601 format
            lastMessage: 'Hello, how are you?',
        },
        {
            id: 2,
            name: 'Jane Doe',
            timeOfLastMessage: '2024-02-21T14:25:43.511Z',
            lastMessage: 'I am good, thank you!',
        },
        {
            id: 3,
            name: 'Alice',
            timeOfLastMessage: '2024-04-02T13:25:43.511Z',
            lastMessage: 'That\'s great to hear!',
        },
        {
            id: 4,
            name: 'Bob',
            timeOfLastMessage: '2024-03-27T19:25:43.511Z',
            lastMessage: 'How are you doing?',
        },
        {
            id: 5,
            name: 'Charlie',
            timeOfLastMessage: '2024-03-27T17:25:43.511Z',
            lastMessage: 'I am doing well, thank you!',
        },
        {
            id: 6,
            name: 'David',
            timeOfLastMessage: '2024-03-27T15:25:43.511Z',
            lastMessage: 'Good to hear!',
        },
        {
            id: 7,
            name: 'Eve',
            timeOfLastMessage: '2024-03-27T16:25:43.511Z',
            lastMessage: 'Hi there!',
        },
        {
            id: 8,
            name: 'Frank',
            timeOfLastMessage: '2024-03-27T12:25:43.511Z',
            lastMessage: 'Hello!',
        },
        {
            id: 9,
            name: 'Grace',
            timeOfLastMessage: '2024-03-27T11:25:43.511Z',
            lastMessage: 'Hey!',
        },
        {
            id: 10,
            name: 'Henry',
            timeOfLastMessage: '2024-03-27T10:25:43.511Z',
            lastMessage: 'Howdy!',
        },
        {
            id: 11,
            name: 'Ivy',
            timeOfLastMessage: '2024-03-27T09:25:43.511Z',
            lastMessage: 'Hi!',
        },
        {
            id: 12,
            name: 'Jack',
            timeOfLastMessage: '2024-03-27T08:25:43.511Z',
            lastMessage: 'Hey there!',
        },
        {
            id: 13,
            name: 'Katie',
            timeOfLastMessage: '2024-03-27T07:25:43.511Z',
            lastMessage: 'Hello, how are you?',
        },
        {
            id: 14,
            name: 'Liam',
            timeOfLastMessage: '2024-04-02T06:25:43.511Z',
            lastMessage: 'I am good, thank you!',
        },
        {
            id: 15,
            name: 'Mia',
            timeOfLastMessage: '2024-04-01T05:25:43.511Z',
            lastMessage: 'That\'s great to hear!',
        }
    ];

    // Order chatData by timeOfLastMessage in descending order
    chatData.sort((a, b) => new Date(b.timeOfLastMessage) - new Date(a.timeOfLastMessage));

    const handleChatSelection = (chat) => {
        // Handle chat selection logic here
        // navigate to ChatScreen with chat data for the selected chat
        navigation.navigate("ChatScreen", { chat });
    }

    const [modalVisible, setModalVisible] = useState(false);

    const [selectedUser, setSelectedUser] = useState(new Set());
    
    // After clicking the "Create" button
    const handleChatCreation = () => {
        console.log(selectedUser);
        const chat = {
            id: 16, // Change to a new chat ID 
            name: "New Chat", // Change to new name 
        }
        navigation.navigate("ChatScreen", {chat});
        setModalVisible(false)
    }

    // Handles clicking checkboxes when selecting users in a group 
    const handleUserSelection = (isChecked, item) => {
        selectedUser.has(item.id) ? selectedUser.delete(item.id) : selectedUser.add(item.id)
    }

    return (
        <View className="flex-1 min-h-screen bg-accent justify-start">
            <SafeAreaView className="">
                <View className="flex-row justify-between items-center content-center p-8">
                    <IconButton icon={<Icon name="address-book-o" size={32} color="white"/>} onPress={() => navigation.navigate("ContactScreen")}/>
                    <Text className="text-primary text-xl font-extrabold text-center">Chats</Text>
                    <IconButton icon={<Icon name="pencil-square-o" size={32} color="white"/>} onPress={() => setModalVisible(true)}/>
                </View>
            </SafeAreaView>
            <View className="flex flex-col flex-grow bg-primary rounded-t-3xl" >
                <ScrollView className="p-2 flex-1">
                    <View className="flex flex-col gap-y-2 justify-center items-center pb-12">
                        {
                            chatData.map((chat) => {
                                const formattedDate = formatDate(chat.timeOfLastMessage);

                                return (
                                    <TouchableOpacity key={chat.id} onPress={() => handleChatSelection(chat)} className="flex flex-row w-full p-4 content-center items-center justify-center">
                                        <InitialIcon name={chat.name}/>
                                        <View className="flex flex-col flex-grow">
                                            <View className="flex flex-row justify-between items-center content-center mx-2">
                                                <Text className="text-lg flex-grow font-semibold">{chat.name}</Text>
                                                <Text className="px-2 text-gray-400">{formattedDate}</Text>
                                                <Icon name="angle-right" size={24} color="#9ca3af" className="self-end"/>
                                            </View>
                                            <Text className="mx-2 text-gray-400">{chat.lastMessage}</Text>
                                        </View>
                                    </TouchableOpacity>
                                );
                            })
                        }
                    </View>
                </ScrollView>
            </View>
            <SlidingModal modalVisible={modalVisible} setModalVisible={setModalVisible} height={0.85} dismissHandler={() => setSelectedUser(new Set([]))}>
                <SafeAreaView className="flex flex-col justify-end h-full">
                    <View className="py-4">
                        <Text className="text-black text-xl font-extrabold text-center">New Chat</Text>
                    </View>
                    <FlatList 
                        className = "h-4/5 bg-white"
                        keyExtractor = {(item) => item.id}
                        data = {chatData}
                        renderItem = {({item}) => (
                            <View>
                                <View className = "flex flex-row items-center p-4 border border-y-zinc-100 border-l-0 border-r-0"> 
                                    <InitialIcon name={item.name}/>
                                    <Text className = "grow text-md p-4">{item.name}</Text>
                                    <BouncyCheckbox fillColor="green" onPress={(isChecked) =>         handleUserSelection(isChecked, item)}/>
                                </View>
                            </View>
                        )}
                    />
                    <View className="px-4 pt-6 pb-2">
                        <TextButton onPress={handleChatCreation} title="Create Chat"/>
                    </View>
                </SafeAreaView>
            </SlidingModal>
        </View>
    );
};

export default ChatSelectionScreen;
