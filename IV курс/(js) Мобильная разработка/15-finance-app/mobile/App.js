import 'react-native-gesture-handler';
import {StatusBar, StyleSheet} from 'react-native';
import {NavigationContainer} from "@react-navigation/native";
import {createDrawerNavigator} from '@react-navigation/drawer';
import React from 'react';
import Costs from "./src/screens/Costs";
import Earnings from "./src/screens/Earnings";
import Login from "./src/screens/Login";
import Settings from "./src/screens/Settings";

const Drawer = createDrawerNavigator();


const App = () => {
  return (
    <NavigationContainer>
      <Drawer.Navigator initialRouteName="Home">
        <Drawer.Screen name="Costs" component={Costs}/>
        <Drawer.Screen name="Earnings" component={Earnings}/>
        <Drawer.Screen name="Login" component={Login}/>
        <Drawer.Screen name="Settings" component={Settings}/>
      </Drawer.Navigator>
    </NavigationContainer>
  );
}


const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});


export default App;
