import { StyleSheet, TouchableOpacity, View, Text, TouchableHighlight } from "react-native";
import { useState } from "react";

export default function App() {
  return <Counter />
}

function Counter() {
  const [num, setNum] = useState(0)
  const increment = () => {
    setNum(num => num + 1)
  }
  const decrement = () => {
    setNum(num => num - 1)
  }
  const reset = () => {
    setNum(0)
  }

  return (
    <View style={styles.container}>
      <Text style={styles.counter}>{num}</Text>
      <View style={styles.controllers}>
        <CounterButton title="-1" onPress={decrement} />
        <CounterButton title="0" onPress={reset} />
        <CounterButton title="+1" onPress={increment} />
      </View>
    </View>
  )
}

function CounterButton({title, onPress}) {
  return (
    <TouchableHighlight
      style={styles.buttonContainer}
      underlayColor={"#fcff84"}
      onPress={onPress}>
      <Text style={styles.buttonText}>{title}</Text>
    </TouchableHighlight>
  )
}

const styles = StyleSheet.create({
  container: {
    ...StyleSheet.absoluteFillObject,
    flex: 1,
    backgroundColor: "#ffffff",
    alignItems: "center",
    justifyContent: "center",
  },
  counter: {
    fontSize: 100,
    fontWeight: "800",
    textAlign: "center",
    color: "#da6487",
    marginVertical: 60,
  },
  controllers: {
    flexDirection: "row",
    alignItems: "center",
    justifyContent: "space-between",
    width: "80%"
  },
  buttonContainer: {
    backgroundColor: "#da6487",
    paddingVertical: 8,
    paddingHorizontal: 28,
    borderRadius: 12,
  },
  buttonText: {
    fontSize: 32,
    fontWeight: "700",
    textAlign: "center",
    color: "#ffffff",
  }
})
