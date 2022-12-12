import React, {useState} from 'react';
import {createNativeStackNavigator} from "@react-navigation/native-stack";
import Welcome from "../screens/Welcome"
import LogIn from "../screens/LogIn"
import SignUp from "../screens/SignUp";
import MainNav from "./MainNav";
import Settings from "../screens/Settings";
import {UserContext} from "./context";
import {AntDesign} from "@expo/vector-icons";

const Stack = createNativeStackNavigator();

const WelcomeNav = () => {
    const [user, setUser] = useState(false)
    const getSettingsOptions = ({navigation}) => ({
        title: "Учетная запись",
        headerStyle: {backgroundColor: "#18181b"},
        headerTitleAlign: "center",
        headerIconColor: "#ffffff",
        headerLeft: () => <AntDesign name="close" size={30} color="#ffffff" onPress={navigation.goBack}/>,
    })
    return (
        <UserContext.Provider value={{user: user, setUser: setUser}}>
            <Stack.Navigator
                initialRouteName="Welcome"
                screenOptions={{
                    headerStyle: {backgroundColor: "#0e0e10"},
                    headerTintColor: "#ffffff",
                }}
            >
                <Stack.Screen name="Welcome" component={Welcome} options={{headerShown: false}}/>
                <Stack.Screen name="LogIn" options={{title: "Войти"}} component={LogIn}>
                </Stack.Screen>
                <Stack.Screen name="SignUp" component={SignUp} options={{title: "Регистрация"}}/>
                <Stack.Screen
                    name="MainNav" component={MainNav}
                    options={{headerShown: false}}
                    initialParams={{user: user}}
                />
                <Stack.Screen
                    name="Settings"
                    component={Settings}
                    options={getSettingsOptions}
                />
            </Stack.Navigator>
        </UserContext.Provider>
    );
};

export default WelcomeNav;