import {SafeAreaView, ScrollView, Text, TouchableOpacity, View, FlatList} from "react-native";
import Icon from 'react-native-vector-icons/FontAwesome';
import IconButton from "../components/IconButton";
import {formatPythonTimeString} from "../utils/dateUtils";
import InitialIcon from "../components/InitialIcon";
import {useEffect, useState} from "react";
import SlidingModal from "../components/SlidingModal";
import axios from "axios";
import BouncyCheckbox from "react-native-bouncy-checkbox";
import TextButton from "../components/TextButton";


const ChatSelectionScreen = ({ navigation }) => {
    const serverUrl = process.env.EXPO_PUBLIC_SERVER_URL;
    const currentUserId = 'w0qh0NXts4gROIOPU7Aq';
    const [chatData, setChatData] = useState(null);
    const [modalVisible, setModalVisible] = useState(false);
    const [selectedUser, setSelectedUser] = useState(new Set());

    useEffect(() => {
        const getRoomsData = async () => {
            try {
                const response = await axios.post(`${serverUrl}/message_server/get_rooms`, 
                {
                    clientID: currentUserId,
                },
                {
                    headers: {
                        clientID: currentUserId,
                    }
                }
            );
                setChatData(response.data);
                return response.data;
            } catch (error) {console.error('Error:', error)}
        };
        getRoomsData();
    }, []);
    
    const handleChatSelection = (room_id, room_name) => {
        // Handle chat selection logic here
        // navigate to ChatScreen with chat data for the selected chat
        navigation.navigate("ChatScreen", {room_id, room_name});
    }
    
    // Handles clicking checkboxes when selecting users in a group 
    const handleUserSelection = (isChecked, item) => {
        selectedUser.has(item.id) ? selectedUser.delete(item.id) : selectedUser.add(item.id)
    }
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
                        {chatData?.rooms && (
                            chatData.rooms.map((room) => {
                                const formattedDate = room.recent_message?.timestamp ? formatPythonTimeString(room.recent_message.timestamp) : null;
                                return (
                                    <TouchableOpacity 
                                        key={room.room_id} 
                                        onPress={() => handleChatSelection(room.room_id, room.room_name)} 
                                        className="flex flex-row w-fit p-4 content-center items-center justify-center"
                                    >
                                        {room.room_name && <InitialIcon name={room.room_name}/>}
                                        <View className="flex flex-col flex-grow">
                                            <View className="flex flex-row justify-between items-center content-center mx-2">
                                                {room.room_name && <Text className="text-lg w-48 font-semibold" numberOfLines={1}>{room.room_name}</Text>}
                                                {formattedDate && <Text className="px-2 text-gray-400" numberOfLines={1}>{formattedDate}</Text>}
                                                <Icon name="angle-right" size={24} color="#9ca3af" className="self-end"/>
                                            </View>
                                            <Text className="mx-2 text-gray-400 w-48" numberOfLines={1}>{room.recent_message.content}</Text>
                                        </View>
                                    </TouchableOpacity>
                                );
                            })
                        )}
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
                                    <BouncyCheckbox fillColor="green" onPress={(isChecked) => handleUserSelection(isChecked, item)}/>
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
