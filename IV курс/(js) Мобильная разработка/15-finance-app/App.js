import {StyleSheet} from 'react-native';
import {NavigationContainer} from "@react-navigation/native";
import { Button, View } from 'react-native';
import { createDrawerNavigator } from '@react-navigation/drawer';
import React from 'react';

const Drawer = createDrawerNavigator();


export default function App() {
  return (
    <NavigationContainer>
      <Drawer.Navigator initialRouteName="Home">
        <Drawer.Screen name="Home" component={HomeScreen}/>
        <Drawer.Screen name="Notifications" component={NotificationsScreen}/>
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
