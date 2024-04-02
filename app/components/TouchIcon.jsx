import {TouchableOpacity} from "react-native";

const TouchIcon = ({ icon, onPress }) => {
    return (
        <TouchableOpacity onPress={onPress}>
            {icon}
        </TouchableOpacity>
    );
};

export default TouchIcon;
