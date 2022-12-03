import React, {useState} from "react";
import {Button, StyleSheet, TextInput, View} from 'react-native'
import AsyncStorage from '@react-native-async-storage/async-storage';

import {AuthContext} from "../context";
import {ACCESS_TOKEN_KEY, API_URL} from "../constants";

const Login = () => {
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')

  const {signIn} = React.useContext(AuthContext)

  const storeToken = async (token) => {
    try {
      await AsyncStorage.setItem(ACCESS_TOKEN_KEY, token)
    } catch (e) {
      console.log(`Can't save token ${e}`)
    }
  }

  const submitHandler = () => {
    fetch(`${API_URL}/login`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        "username": username,
        "password": password
      })
    }).then((resp) => resp.json())
      .then((data) => {
        const token = data[ACCESS_TOKEN_KEY]
        signIn(token)
        console.log(`GOT TOKEN: ${token}`)
      }).catch((e) => {
      console.log(`GOT ERROR: ${e}`)
    })
  }

  return (
    <View style={styles.container}>
      <TextInput
        defaultValue={username}
        onChangeText={x => setUsername(x)}
        placeholder={'username'}
        style={styles.input}
      />
      <TextInput
        defaultValue={password}
        onChangeText={x => setPassword(x)}
        placeholder={'password'}
        style={styles.input}
        secureTextEntry={true}
      />
      <Button
        title={'Login'}
        style={styles.input}
        onPress={submitHandler}
      />
    </View>
  )
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
  input: {
    width: 300,
    height: 48,
    padding: 10,
    borderWidth: 1,
    borderColor: 'black',
    marginBottom: 10,
  }
});

export default Login;

