import React from "react";
import {Button, StyleSheet, View} from 'react-native'
import {AuthContext} from "../context";


const Settings = () => {
  const {signOut} = React.useContext(AuthContext)

  return (
    <View style={styles.container}>
      <Button
        title={'Logout'}
        style={styles.input}
        onPress={signOut}
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

export default Settings;

