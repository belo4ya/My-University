import React from 'react';
import {createNativeStackNavigator} from "@react-navigation/native-stack";
import Welcome from "../screens/Welcome"
import LogIn from "../screens/LogIn"
import SignUp from "../screens/SignUp";
import MainNav from "./MainNav";

const Stack = createNativeStackNavigator();

const WelcomeNav = ({logIn}) => {
    return (
        <Stack.Navigator
            initialRouteName="Welcome"
            screenOptions={{
                headerStyle: {backgroundColor: "#0e0e10"},
                headerTintColor: "#ffffff",
            }}
        >
            <Stack.Screen name="Welcome" component={Welcome} options={{headerShown: false}}/>
            <Stack.Screen name="LogIn" options={{title: "Войти"}}>
                {(props) => <LogIn {...props} logIn={logIn}/>}
            </Stack.Screen>
            <Stack.Screen name="SignUp" component={SignUp} options={{title: "Регистрация"}}/>
            <Stack.Screen name="MainNav" component={MainNav} options={{headerShown: false}}/>
        </Stack.Navigator>
    );
};

export default WelcomeNav;