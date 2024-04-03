import {ScrollView, Text, TouchableOpacity, View} from "react-native";
import Icon from 'react-native-vector-icons/FontAwesome';
import IconButton from "../components/IconButton";

const ChatSelectionScreen = ({ navigation }) => {

    // TODO: Query chat data from backend

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

    const getInitials = (name) => {
        const nameArray = name.split(" ");
        return nameArray.map(word => word[0]).join("").toUpperCase();
    };

    const handleChatSelection = (chat) => {
        // Handle chat selection logic here
        // navigate to ChatScreen with chat data for the selected chat
        navigation.navigate("ChatScreen", { chat });
    }

    // format the date
    const formatDate = (dateString) => {
        const dateObject = new Date(dateString);
        const currentDate = new Date();

        // Check if the date is within the current day (0-24h)
        if (dateObject.getDate() === currentDate.getDate() && dateObject.getMonth() === currentDate.getMonth() && dateObject.getFullYear() === currentDate.getFullYear()) {
            // Format time in 12-hour AM/PM format
            let hours = dateObject.getHours();
            const amPm = hours >= 12 ? 'PM' : 'AM';
            hours = hours % 12 || 12;
            const minutes = dateObject.getMinutes().toString().padStart(2, '0');
            return `${hours}:${minutes} ${amPm}`;
        }

        // Check if the date was yesterday
        const yesterday = new Date(currentDate);
        yesterday.setDate(currentDate.getDate() - 1);
        if (dateObject.getDate() === yesterday.getDate() && dateObject.getMonth() === yesterday.getMonth() && dateObject.getFullYear() === yesterday.getFullYear()) {
            return 'Yesterday';
        }

        // Check if the date was within the last week
        const oneWeekAgo = new Date(currentDate);
        oneWeekAgo.setDate(currentDate.getDate() - 7);
        if (dateObject > oneWeekAgo) {
            // Output the day name
            const daysOfWeek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
            return daysOfWeek[dateObject.getDay()];
        }

        // If none of the above conditions match, return the year-month-day format
        return `${dateObject.getFullYear()}-${(dateObject.getMonth() + 1).toString().padStart(2, '0')}-${dateObject.getDate().toString().padStart(2, '0')}`;
    };

    return (
        <View className="flex-1 min-h-screen bg-accent justify-start">
            <View className="flex-1 flex-row justify-between items-center content-center px-8">
                <IconButton icon={<Icon name="address-book" size={32} color="white"/>} onPress={() => navigation.navigate("ContactScreen")}/>
                <Text className="text-primary text-xl font-extrabold text-center">Chats</Text>
                <IconButton icon={<Icon name="user" size={32} color="white"/>} onPress={() => navigation.navigate("ProfileScreen")}/>
            </View>
            <View className="bg-primary rounded-t-3xl h-4/5">
                <ScrollView className="p-2">
                    <View className="flex flex-col gap-y-2 justify-center items-center">
                        {
                            chatData.map((chat) => {
                                const formattedDate = formatDate(chat.timeOfLastMessage);

                                return (
                                <TouchableOpacity key={chat.id} onPress={() => handleChatSelection(chat)} className="flex flex-row w-full p-4 content-center items-center justify-center">
                                    <View className="w-10 h-10 rounded-full flex justify-center items-center bg-gray-400">
                                        <Text className="text-xl font-bold text-primary">{getInitials(chat.name)}</Text>
                                    </View>
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
        </View>
    );
};

export default ChatSelectionScreen;
