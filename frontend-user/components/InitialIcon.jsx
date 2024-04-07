import {Text, View} from "react-native";
import {getInitials} from "../utils/stringUtils";

const InitialIcon = ({ name }) => {

    return (
        <View className="w-10 h-10 rounded-full flex justify-center items-center bg-gray-400">
            <Text className="text-xl font-bold text-primary">{getInitials(name)}</Text>
        </View>
    );
};

export default InitialIcon;
