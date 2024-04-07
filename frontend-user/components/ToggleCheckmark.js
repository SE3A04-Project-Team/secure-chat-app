import React, { useState } from 'react';
import { View, TouchableOpacity, StyleSheet, Animated } from 'react-native';
import { Ionicons } from '@expo/vector-icons'; // Assuming you have Ionicons installed

const ToggleCheckmark = ({ onChange }) => {
  const [isChecked, setIsChecked] = useState(false);
  const scaleValue = new Animated.Value(0);

  const handleToggle = () => {
    setIsChecked(!isChecked);
    onChange(!isChecked);
    Animated.spring(scaleValue, {
      toValue: isChecked ? 0 : 1,
      duration: 300,
      useNativeDriver: false
    }).start();
  };

  const animatedStyle = {
    transform: [
      {
        scale: scaleValue.interpolate({
          inputRange: [0, 1],
          outputRange: [0, 1],
          extrapolate: 'clamp'
        })
      }
    ]
  };

  return (
    <TouchableOpacity onPress={handleToggle}>
      <View style={styles.container}>
        <Animated.View style={[styles.checkmark, animatedStyle]}>
          {isChecked && <Ionicons name="checkmark" size={24} color="white" />}
        </Animated.View>
      </View>
    </TouchableOpacity>
  );
};

const styles = StyleSheet.create({
  container: {
    width: 30,
    height: 30,
    borderRadius: 15,
    backgroundColor: '#eee',
    justifyContent: 'center',
    alignItems: 'center'
  },
  checkmark: {
    width: 30,
    height: 30,
    borderRadius: 15,
    backgroundColor: 'green',
    justifyContent: 'center',
    alignItems: 'center'
  }
});

export default ToggleCheckmark;
