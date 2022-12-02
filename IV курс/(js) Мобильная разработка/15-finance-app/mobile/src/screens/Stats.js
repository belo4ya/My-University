import React from "react";
import {StyleSheet, Text, View} from 'react-native'

export default function Stats() {
  return (
    <View style={styles.container}>
      <Text>Stats screen</Text>
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
