import React, {useEffect, useState} from 'react';
import {StyleSheet, Text, TouchableOpacity, View} from 'react-native';
import {Accelerometer} from 'expo-sensors';

// noinspection JSUnusedGlobalSymbols
export default function App() {
  const [{r, g, b}, _] = useState({r: 255, g: 255, b: 255})
  const [{x, y, z}, setXYZ] = useState({x: 0, y: 0, z: 0})
  const [{dR, dG, dB}, setRGB] = useState({dR: r, dG: g, dB: b})
  const [acc, setAcc] = useState(0)
  const [subscription, setSubscription] = useState(null);
  const [firstMeasure, setFirstMeasure] = useState(null)

  const _listener = ({x, y, z}) => {
    let sync = firstMeasure
    if (firstMeasure === null) {
      sync = {x, y, z}
      setFirstMeasure({x, y, z})
    }
    x -= sync.x
    y -= sync.y
    z -= sync.z

    const acc = Math.round(Math.abs(x) * 42 + Math.abs(y) * 42 + Math.abs(z) * 42)
    setAcc(acc)
    setRGB({
      dR: r,
      dG: (g - acc),
      dB: (b - acc),
    })
    setXYZ({
      x: x,
      y: y,
      z: z,
    })
  }

  const _subscribe = () => {
    setSubscription(Accelerometer.addListener(_listener));
    Accelerometer.setUpdateInterval(50);
  };

  const _unsubscribe = () => {
    subscription && subscription.remove();
    setSubscription(null);
  };

  useEffect(() => {
    _subscribe();
    return () => _unsubscribe();
  }, []);

  return (
    <View style={{...styles.background, backgroundColor: `rgb(${dR}, ${dG}, ${dB})`}}>
      <View style={styles.container}>
        <View style={styles.textView}>
          <Text style={styles.text}>x: {Math.round(x * 10)}, y: {Math.round(y * 10)}, z: {Math.round(z * 10)}</Text>
        </View>
        <View style={styles.textView}>
          <Text style={styles.text}>rgb({dR}, {dG}, {dB})</Text>
        </View>
        <View style={styles.textView}>
          <Text style={styles.text}>Acceleration: {acc}</Text>
        </View>
        <View style={styles.textView}>
          <TouchableOpacity onPress={subscription ? _unsubscribe : _subscribe}>
            <Text style={styles.text}>{subscription ? 'On' : 'Off'}</Text>
          </TouchableOpacity>
        </View>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  background: StyleSheet.absoluteFillObject,
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
  textView: {
    backgroundColor: '#ffffff',
  },
  text: {
    fontSize: 32,
    fontWeight: 'bold',
  }
});
