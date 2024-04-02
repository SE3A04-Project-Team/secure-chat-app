import React, {useEffect, useState} from 'react';
import {Animated, Dimensions, Modal, TouchableOpacity} from "react-native";

const SlidingModal = ({ children, modalVisible, setModalVisible }) => {
    const [backgroundAnimation] = useState(new Animated.Value(0));
    const [contentAnimation] = useState(new Animated.Value(0));

    useEffect(() => {
        if (modalVisible) {
            Animated.parallel([
                Animated.timing(backgroundAnimation, {
                    toValue: 1,
                    duration: 300,
                    useNativeDriver: true,
                }),
                Animated.timing(contentAnimation, {
                    toValue: 1,
                    duration: 300,
                    useNativeDriver: true,
                })
            ]).start();
        } else {
            Animated.parallel([
                Animated.timing(backgroundAnimation, {
                    toValue: 0,
                    duration: 300,
                    useNativeDriver: true,
                }),
                Animated.timing(contentAnimation, {
                    toValue: 0,
                    duration: 300,
                    useNativeDriver: true,
                })
            ]).start(() => {
                // Execute this callback after the animation completes
                // Set modal visibility to false after animation
                setModalVisible(false);
            });
        }

        // Cleanup function
        return () => {
            // Reset animations
            backgroundAnimation.setValue(0);
            contentAnimation.setValue(0);
        };
    }, [modalVisible]);

    const toggleModal = () => {
        setModalVisible(!modalVisible);
    };

    const backgroundOpacity = backgroundAnimation.interpolate({
        inputRange: [0, 1],
        outputRange: [0, 0.5],
    });

    const screenHeight = Dimensions.get('window').height;
    const contentHeight = screenHeight * 0.25; // Minimum 25% of screen height

    const contentTranslateY = contentAnimation.interpolate({
        inputRange: [0, 1],
        outputRange: [contentHeight, 0],
    });

    const handleBackgroundPress = () => {
        // Trigger closing animation
        Animated.parallel([
            Animated.timing(backgroundAnimation, {
                toValue: 0,
                duration: 300,
                useNativeDriver: true,
            }),
            Animated.timing(contentAnimation, {
                toValue: 0,
                duration: 300,
                useNativeDriver: true,
            })
        ]).start(() => {
            // Set modal visibility to false after animation
            setModalVisible(false);
        });
    };

    return (
        <Modal
            transparent
            visible={modalVisible}
            onRequestClose={toggleModal}
        >
            <Animated.View
                style={{
                    flex: 1,
                    backgroundColor: 'rgba(0, 0, 0, 0.5)',
                    opacity: backgroundOpacity,
                }}
            >
                <TouchableOpacity
                    style={{ flex: 1 }}
                    activeOpacity={1}
                    onPress={handleBackgroundPress} // Handle background press
                />
            </Animated.View>

            <Animated.View
                style={{
                    position: 'absolute',
                    bottom: 0,
                    left: 0,
                    right: 0,
                    backgroundColor: 'white',
                    borderTopLeftRadius: 20,
                    borderTopRightRadius: 20,
                    height: contentHeight,
                    transform: [{ translateY: contentTranslateY }],
                }}
            >
                {children}
            </Animated.View>
        </Modal>
    );
}

export default SlidingModal;
