import React from 'react';
import {Text, TouchableOpacity} from 'react-native';

const TextButton = ({ onPress, title }) => {

    return (
        <TouchableOpacity onPress={onPress} className="py-3 bg-accent rounded-xl">
            <Text className="text-xl font-bold text-center text-primary">{title}</Text>
        </TouchableOpacity>
    );
};

export default TextButton;
