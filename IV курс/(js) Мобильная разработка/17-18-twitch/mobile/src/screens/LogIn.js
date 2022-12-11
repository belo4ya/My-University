import React from 'react';
import {Text, TouchableOpacity, View} from "react-native";

const LogIn = ({navigation, logIn}) => {
    const _logIn = () => {
        logIn()
        navigation.navigate("MainNav")
    }
    return (
        <View>
            <Text>LogIn LogIn LogIn</Text>
            <TouchableOpacity onPress={_logIn}><Text>Войти</Text></TouchableOpacity>
        </View>
    );
};

export default LogIn;