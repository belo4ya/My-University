import React, {useEffect, useState} from "react";
import {
  Button,
  SafeAreaView,
  StyleSheet,
  Text,
  TextInput,
  TouchableHighlight,
  TouchableOpacity,
  View
} from 'react-native'
import dayjs from 'dayjs'

import AsyncStorage from '@react-native-async-storage/async-storage';
import {Picker} from "@react-native-picker/picker";
import {SwipeListView} from 'react-native-swipe-list-view';
import {ACCESS_TOKEN_KEY, API_URL} from "../constants";

const Earnings = () => {
  const [dataArray, setDataArray] = useState([])
  const [isLoading, setIsLoading] = useState(false)
  const [token, setToken] = useState('')

  const [currentAmount, setCurrentAmount] = useState('')
  const [currentCategory, setCurrentCategory] = useState('Зарплата')
  const [currentSource, setCurrentSource] = useState('Тинькофф')

  const renderItem = ({item}) => (
    <TouchableHighlight
      style={styles.rowFront}
      underlayColor={'#AAA'}
    >
      <View style={styles.costLineWrapper}>
        <Text style={styles.costAmount}>{item.amount}</Text>
        <Text style={styles.costSource}>{item.source}</Text>
        <Text style={styles.costCategory}>{item.category}</Text>
        <Text style={styles.costDate}>{dayjs(item.datetime).format('hh:mm DD.MM.YY')}</Text>
      </View>
    </TouchableHighlight>
  )

  const closeRow = (rowMap, rowKey) => {
    if (rowMap[rowKey]) {
      rowMap[rowKey].closeRow();
    }
  };

  const deleteRow = (rowMap, rowKey) => {
    closeRow(rowMap, rowKey);
    const newData = [...dataArray];
    const prevIndex = dataArray.findIndex(item => item.id === rowKey);
    newData.splice(prevIndex, 1);
    setDataArray(newData);
    deleteData(rowKey)
  };

  const renderHiddenItem = (data, rowMap) => (
    <View style={styles.rowBack}>
      <TouchableOpacity
        style={[styles.backRightBtn, styles.backRightBtnRight]}
        onPress={() => deleteRow(rowMap, data.item.id)}
      >
        <Text style={styles.backTextWhite}>Delete</Text>
      </TouchableOpacity>
    </View>
  );

  useEffect(() => {
    AsyncStorage.getItem(ACCESS_TOKEN_KEY).then((value) => {
      if (value) {
        setToken(value)
      }
    })
  }, [])

  useEffect(() => {
    if (token !== '') {
      getData()
    }
  }, [token])

  const getData = () => {
    setIsLoading(true)
    let URL = `${API_URL}/api/earnings`
    fetch(URL, {
      headers: {
        'Token': token
      }
    }).then(res => res.json()).then(res => {
      setDataArray(res)
    }).finally(() => setIsLoading(false))
  }

  function deleteData(id) {
    const requestOptions = {
      method: 'DELETE',
      headers: {
        'Token': token
      },
      body: JSON.stringify({
        "id": id
      })
    }

    fetch(`${API_URL}/api/earnings/${id}`, requestOptions).then((res) => {
      return res.json();
    }).then(() => {
      getData()
    }).catch(function (error) {
      console.log('delete earnings error: ', error)
    })
  }

  function sendData() {
    const requestOptions = {
      method: 'POST',
      headers: {
        'Token': token
      },
      body: JSON.stringify({
        "datetime": dayjs(Date.now()).format(),
        "amount": Number(currentAmount),
        "source": currentSource,
        "category": currentCategory
      })
    }
    if (currentAmount !== '') {
      fetch(`${API_URL}/api/earnings`, requestOptions).then((res) => {
        return res.json();
      }).then((res) => {
        getData()
        setCurrentAmount('')
        //console.log("sendData OK")
      }).catch(function (error) {
        console.log('sendData POST ERROR: ', error)
      })
    }
  }

  return (
    <SafeAreaView>
      <View style={styles.adderblock}>
        <TextInput
          style={styles.bigtextinput}
          onChangeText={text => setCurrentAmount(text)}
          keyboardType="numeric"
          defaultValue={currentAmount}
        />
        <Picker
          selectedValue={currentCategory}
          onValueChange={(itemValue, itemIndex) =>
            setCurrentCategory(itemValue)
          }>
          <Picker.Item label="MAIN SALARY" value="MAIN SALARY"/>
          <Picker.Item label="Patreon" value="Patreon"/>
          <Picker.Item label="Youtube" value="Youtube"/>
        </Picker>
        <View style={styles.bigbuttonwrapper}>
          <Button
            title={'Add'}
            style={styles.input}
            onPress={sendData}
          />
        </View>
      </View>
      <SwipeListView
        data={dataArray}
        renderItem={renderItem}
        keyExtractor={item => item.id.toString()}
        onRefresh={getData}
        refreshing={isLoading}
        renderHiddenItem={renderHiddenItem}
        rightOpenValue={-75}
      />
    </SafeAreaView>
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
  },
  costLineWrapper: {
    height: 50,
    flex: 1,
    flexDirection: 'row',
  },
  costAmount: {
    height: 50,
    lineHeight: 50,
    flex: 2,
    paddingLeft: 20,
  },
  costSource: {
    height: 50,
    lineHeight: 50,
    flex: 2,
  },
  costCategory: {
    height: 50,
    lineHeight: 50,
    flex: 4,
  },
  costDate: {
    height: 50,
    lineHeight: 50,
    flex: 3,
    paddingRight: 20,
  },
  adderblock: {
    paddingTop: 55,
  },
  bigtextinput: {
    fontSize: 20,
    borderWidth: 1,
    borderColor: 'grey',
    height: 50,
    width: 300,
    textAlign: 'center',
    alignSelf: 'center',
  },
  bigbuttonwrapper: {
    paddingBottom: 15
  },
  backTextWhite: {
    color: '#FFF',
  },
  rowFront: {
    alignItems: 'center',
    backgroundColor: '#CCC',
    borderBottomColor: 'black',
    borderBottomWidth: 1,
    justifyContent: 'center',
    height: 50,
  },
  rowBack: {
    alignItems: 'center',
    backgroundColor: '#DDD',
    flex: 1,
    flexDirection: 'row',
    justifyContent: 'space-between',
    paddingLeft: 15,
  },
  backRightBtn: {
    alignItems: 'center',
    bottom: 0,
    justifyContent: 'center',
    position: 'absolute',
    top: 0,
    width: 75,
  },
  backRightBtnLeft: {
    backgroundColor: 'blue',
    right: 75,
  },
  backRightBtnRight: {
    backgroundColor: 'red',
    right: 0,
  },
});

export default Earnings;
