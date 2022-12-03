import {StatusBar} from 'expo-status-bar';
import React, {useEffect, useMemo, useState} from 'react';
import {ActivityIndicator, SafeAreaView, StyleSheet} from 'react-native';

import {createDrawerNavigator} from '@react-navigation/drawer';
import {NavigationContainer} from '@react-navigation/native';

import AsyncStorage from '@react-native-async-storage/async-storage';

import Earnings from "./src/screens/Earnings";
import Costs from "./src/screens/Costs";
import Login from './src/screens/Login'
import Settings from "./src/screens/Settings";
import Stats from './src/screens/Stats'
import {AuthContext} from "./src/context";
import {ACCESS_TOKEN_KEY} from "./src/constants";


const Drawer = createDrawerNavigator();

const App = () => {
  const [accessToken, setAccessToken] = useState('')
  const [isLoading, setIsLoading] = useState(true)

  const authContent = useMemo(() => ({
    signIn: (token) => {
      console.log("signIn")
      AsyncStorage.setItem(ACCESS_TOKEN_KEY, token).then(() => {
        setIsLoading(false)
        setAccessToken(token)
      })
    },
    signOut: () => {
      AsyncStorage.removeItem('access_token').then(() => {
        setIsLoading(false)
        setAccessToken('')
      })
    }
  }), [])

  useEffect(() => {
    AsyncStorage.getItem(ACCESS_TOKEN_KEY).then((value) => {
      if (value) {
        setAccessToken(value)
      }
    })
  }, [])

  useEffect(() => {
    setTimeout(() => {
      setIsLoading(false)
    }, 800)
  }, [])

  if (isLoading) {
    return (
      <SafeAreaView style={styles.container}>
        <ActivityIndicator size='large'/>
      </SafeAreaView>
    )
  }

  return (
    <AuthContext.Provider value={authContent}>
      <NavigationContainer>
        {/*{accessToken !== null ? (*/}
        <Drawer.Navigator>
          <Drawer.Screen name="Stats" component={Stats}/>
          <Drawer.Screen name="Costs" component={Costs}/>
          <Drawer.Screen name="Earnings" component={Earnings}/>
          <Drawer.Screen name="Settings" component={Settings}/>
          <Drawer.Screen name="Login" component={Login}/>
        </Drawer.Navigator>
        {/*) : (*/}
        {/*  <Drawer.Navigator>*/}
        {/*    <Drawer.Screen name="Login" component={Login}/>*/}
        {/*  </Drawer.Navigator>*/}
        {/*)}*/}
        <StatusBar style="auto"/>
      </NavigationContainer>
    </AuthContext.Provider>
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
