import {View, Text, SafeAreaView, ScrollView, Button, TouchableOpacity} from "react-native";
import Icon from "react-native-vector-icons/FontAwesome";

const ChatScreen = ({route, navigation}) => {
    const {chat} = route.params;

    // TODO: Query chat messages from backend using chat.id

    return (
        <SafeAreaView>
            <View className="flex flex-row justify-between items-center content-center p-2 gap-4">
                <TouchableOpacity className="px-4">
                    <Icon name="arrow-left" size={24} color="black"/>
                </TouchableOpacity>
                <Text className="flex-grow font-bold text-xl">{chat.name}</Text>
            </View>
            <ScrollView>
                {/* Display chat messages here */}
            </ScrollView>
        </SafeAreaView>
    );
};

export default ChatScreen;
