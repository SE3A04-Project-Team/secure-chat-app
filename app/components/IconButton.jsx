import {TouchableOpacity} from "react-native";

const IconButton = ({ icon, onPress }) => {
    return (
        <TouchableOpacity onPress={onPress}>
            {icon}
        </TouchableOpacity>
    );
};

export default IconButton;
