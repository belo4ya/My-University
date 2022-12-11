import {NavigationContainer} from "@react-navigation/native";
import WelcomeNav from "./src/navigation/WelcomeNav";
import Header from "./src/components/Header";

import React, {useState} from 'react';
import {StatusBar} from "react-native";

const App = () => {
    const [user, setUser] = useState(false)
    const logIn = () => {
        setUser(true)
    }
    return (
        <NavigationContainer>
            {user ? <Header/> : null}
            <WelcomeNav logIn={logIn}/>
            {/*<StatusBar style="light"/>*/}
        </NavigationContainer>
    );
}

export default App;
