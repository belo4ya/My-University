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

const Costs = () => {
  const [dataArray, setDataArray] = useState([])
  const [isLoading, setIsLoading] = useState(false)
  const [accessToken, setAccessToken] = useState('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NzA0NjkzMDN9.QvPxMlryQnH_GImMq8KLkvPf7MxaNSmZwJAhL6INGAQ')

  const [currentAmount, setCurrentAmount] = useState(0)
  const [currentCategory, setCurrentCategory] = useState('')
  const [currentSource] = useState('')

  const renderItem = ({item}) => (
    <TouchableHighlight style={styles.rowFront} underlayColor={'#AAA'}>
      <View style={styles.costLineWrapper}>
        <Text style={styles.costAmount}>{item.amount} р.</Text>
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
    getData()
    AsyncStorage.getItem('access_token').then((value) => {
      if (value) {
        setAccessToken(value)
      }
    })
  }, [])

  useEffect(() => {
    if (accessToken !== '') {
      getData()
    }
  }, [accessToken])

  const getData = () => {
    setIsLoading(true)
    fetch('http://192.168.1.133:1323/api/costs', {
      headers: {
        'Authorization': `Bearer ${accessToken}`
      },
    }).then(res => res.json())
      .then(res => setDataArray(res))
      .catch(e => console.log("GET /costs", e))
      .finally(() => setIsLoading(false))
  }

  function deleteData(id) {
    const requestOptions = {
      method: 'DELETE',
      headers: {
        'Authorization': `Bearer ${accessToken}`,
      }
    }

    fetch(`http://192.168.1.133:1323/api/costs/${id}`, requestOptions).catch(e => {
      console.log(`DELETE /costs/${id} ${e}`)
    })
  }

  function sendData() {
    const requestOptions = {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${accessToken}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        "datetime": dayjs(Date.now()).format(),
        "amount": Number(currentAmount),
        "source": currentSource,
        "category": currentCategory
      })
    }
    fetch(
      'http://192.168.1.133:1323/api/costs',
      requestOptions,
    ).then(res => res.json())
      .then(() => {
        getData()
        setCurrentAmount(0)
      }).catch(e => console.log("POST /costs", e))
  }

  return (
    <SafeAreaView>
      <View style={styles.adderblock}>
        <TextInput
          style={styles.bigtextinput}
          onChangeText={amount => setCurrentAmount(Number(amount))}
          keyboardType="numeric"
          defaultValue={currentAmount.toString()}
        />
        <Picker
          selectedValue={currentCategory}
          onValueChange={(category) =>
            setCurrentCategory(category)
          }>
          <Picker.Item label="Еда" value="Еда"/>
          <Picker.Item label="Кафе" value="Кафе"/>
          <Picker.Item label="Развлечения" value="Развлечения"/>
          <Picker.Item label="Транспорт" value="Транспорт"/>
          <Picker.Item label="Коммуналка" value="Коммуналка"/>
          <Picker.Item label="Экстренные ситуации" value="Экстренные ситуации"/>
          <Picker.Item label="Одежда" value="Одежда"/>
          <Picker.Item label="Аптека" value="Аптека"/>
          <Picker.Item label="Other" value="Other"/>
          <Picker.Item label="Телефон" value="Телефон"/>
          <Picker.Item label="Интернет" value="Интернет"/>
          <Picker.Item label="Электроника" value="Электроника"/>
          <Picker.Item label="Налоги" value="Налоги"/>
          <Picker.Item label="Подписки в интернете" value="Подписки в интернете"/>
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

export default Costs;
