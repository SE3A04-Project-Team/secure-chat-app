import React from 'react';
import {SafeAreaView, View, Text, TouchableOpacity, TextInput} from 'react-native';
import { SelectList } from 'react-native-dropdown-select-list';
import TextButton from '../components/TextButton';
import IconButton from "../components/IconButton";
import Icon from "react-native-vector-icons/FontAwesome";

const GenerateReportScreen = ({navigation}) => {
    const [category, setCategory] = React.useState("");
    const [subCategory, setSubCategory] = React.useState("");
    
    const categories = [
        {key: 'John', value: 'John'},
        {key: 'Alice', value: 'Alice'},
        {key: 'Liam', value: 'Liam'},
        {key: 'Mia', value: 'Mia'},
        {key: 'Bob', value: 'Bob'},
        {key: 'Carlie', value: 'Charlie'},
        {key: 'Eve', value: 'Eve'},
        {key: 'David', value: 'David'},
        {key: 'Frank', value: 'Frank'},
        {key: 'Grace', value: 'Grace'},
        {key: 'Henry', value: 'Henry'},
        {key: 'Ivy', value: 'Ivy'},
    ];

    const subcategories = {
        'John': [
            {key:'1', value: 'David'},
            {key:'2', value: 'Frank'},
            {key:'3', value: 'Mia'},
            {key:'4', value: 'Ivy'},
        ],
        'Alice': [
            {key:'5', value: 'Eve'},
            {key:'6', value: 'Henry'},
            {key:'7', value: 'John'},
        ],
        'Liam': [
            {key:'8', value: 'Frank'},
            {key:'9', value: 'Alice'},
            {key:'10', value: 'Grace'},
        ] 
    };

    return (
        <View className="flex-1 min-h-screen bg-accent justify-start">
            <SafeAreaView className="flex-1">
                <View className="flex-row justify-between items-center content-center p-8">
                    <IconButton icon={<Icon name="arrow-left" size={32} color="white"/>} onPress={() => navigation.goBack()}/>
                    <Text className="flex-1 text-white text-xl font-extrabold text-center">Report Generation</Text>
                </View>
            </SafeAreaView>

            <View className="bg-primary rounded-t-3xl p-7 mt-5 h-4/5 justify-center">
                <View className="mb-10">
                    <Text className="text-secondary font-light text-lg">Please Select Person 1</Text>
                    <SelectList
                        setSelected={setCategory}
                        data = {categories}
                        placeholder = {"Select User"}
                    />
                </View>
                <View className="mb-10 ">
                    <Text className="text-secondary font-light text-lg">Please Select Person 2</Text>
                    <SelectList
                        setSelected={setSubCategory}
                        data = {subcategories[category]}
                        placeholder = {"Select Chat"}
                    />
                </View>

                <TextButton title={"Generate Report"}/>
            </View>
        </View>
    );
};

export default GenerateReportScreen;
