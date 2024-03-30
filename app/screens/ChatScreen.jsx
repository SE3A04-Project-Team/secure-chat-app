import {View, Text, SafeAreaView} from "react-native";

const ChatScreen = ({route, navigation}) => {
    const {chat} = route.params;

    // TODO: Query chat messages from backend using chat.id

    return (
        <SafeAreaView>
            <Text>Chat with {chat.name}</Text>
        </SafeAreaView>
    );
};

export default ChatScreen;
