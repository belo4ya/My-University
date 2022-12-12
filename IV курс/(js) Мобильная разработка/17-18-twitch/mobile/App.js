import {NavigationContainer} from "@react-navigation/native";
import WelcomeNav from "./src/navigation/WelcomeNav";

import React from 'react';
import {StatusBar} from "react-native";

const App = () => {
    return (
        <>
            <NavigationContainer independent={true}>
                <WelcomeNav/>
                <StatusBar style="light"/>
            </NavigationContainer>
        </>
    );
}

export default App;
