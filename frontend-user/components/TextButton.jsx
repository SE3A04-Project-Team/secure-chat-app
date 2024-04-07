import React from 'react';
import {Text, TouchableOpacity} from 'react-native';

const TextButton = ({ onPress, title, opacityStyle, textStyle }) => {

    return (
        <TouchableOpacity onPress={onPress} className={opacityStyle ? opacityStyle : 'py-3 bg-secondary rounded-xl'}>
            <Text className={textStyle ? textStyle : 'text-xl font-bold text-center text-primary'}>{title}</Text>
        </TouchableOpacity>
    );
};

export default TextButton;
