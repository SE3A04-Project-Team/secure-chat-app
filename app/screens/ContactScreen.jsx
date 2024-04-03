import {ScrollView, Text, TouchableOpacity, View} from "react-native";
import Icon from "react-native-vector-icons/FontAwesome";
import IconButton from "../components/IconButton";

const ContactScreen = ({navigation}) => {

    const contactData = [
        {id: 1, name: "John Doe"},
        {id: 2, name: "Jane Doe"},
        {id: 3, name: "Alice"},
        {id: 4, name: "Bob"},
        {id: 5, name: "Charlie"},
        {id: 6, name: "David"},
        {id: 7, name: "Eve"},
        {id: 8, name: "Frank"},
        {id: 9, name: "Grace"},
        {id: 10, name: "Henry"},
    ]

    // function to sort contactData by name in ascending order (this should be handled by server later)
    const sortContacts = () => {
        contactData.sort((a, b) => a.name.localeCompare(b.name))
    }
    sortContacts()

    // TODO: Query contact data from server (contact list should be sorted by name)

    return (
        <View className="flex-1 min-h-screen bg-accent justify-start">
            <View className="flex-1 flex-row justify-between items-center content-center px-8">
                <IconButton icon={<Icon name="arrow-left" size={32} color="white"/>} onPress={() => navigation.goBack()}/>
                <Text className="text-white text-xl font-extrabold text-center">Contacts</Text>
                <IconButton icon={<Icon name="user" size={32} color="white"/>} onPress={() => navigation.navigate("ProfileScreen")}/>
            </View>
            <View className="bg-primary rounded-t-3xl h-4/5">
                <ScrollView className="p-2">
                    <View className="flex flex-col gap-y-2 justify-center items-center">
                        {
                            contactData.map((chat) => (
                                <TouchableOpacity key={chat.id} onPress={() => handleChatSelection(chat)} className="flex flex-row w-full p-4 content-center items-center">
                                    <Text className="flex-grow text-lg mx-2">{chat.name}</Text>
                                </TouchableOpacity>
                            ))
                        }
                    </View>
                </ScrollView>
            </View>
        </View>
    )
}

export default ContactScreen;
