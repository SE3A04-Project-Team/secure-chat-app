import {Text, View} from "react-native";
import {getFirstTwoInitials} from "../utils/stringUtils";

const InitialIcon = ({ name }) => {

    return (
        <View className="w-10 h-10 rounded-full flex justify-center items-center bg-gray-400">
            <Text className="text-xl font-bold text-primary">{getFirstTwoInitials(name)}</Text>
        </View>
    );
};

export default InitialIcon;
