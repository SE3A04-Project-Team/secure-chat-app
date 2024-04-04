import {TouchableOpacity, View} from "react-native";

const IconButton = ({ icon, onPress, opacityStyle, containerStyle }) => {
    return (
        <View className={containerStyle}>
            <TouchableOpacity onPress={onPress} className={opacityStyle}>
                {icon}
            </TouchableOpacity>
        </View>
    );
};

export default IconButton;
