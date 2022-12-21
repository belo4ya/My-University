import * as React from 'react';
import {
    Text,
    View,
    Image,
    StyleSheet,
    Pressable,
    Button,
    TouchableOpacity,
    ImageBackground,
    Dimensions,
    Alert,
    ScrollView
} from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import Constants from 'expo-constants';
import ShareExample from './share'
import {Linking} from 'react-native'


const Stack = createNativeStackNavigator();

const Contacts = () => {
  return (
    <NavigationContainer>
      <Stack.Navigator>
        <Stack.Screen
          name="Home"
          component={HomeScreen}
          options={{ title: 'Cписок контактов' }}
        />
        <Stack.Screen 
        name="Profile"
        options={{title: 'Контакт'}}
        component={ProfileScreen} 
        />
        <Stack.Screen 
        name="Call" 
        component={CallScreen} 
        />
        <Stack.Screen 
        name="VideoCall" 
        component={VideoCallScreen} 
        /> 
      </Stack.Navigator>
    </NavigationContainer>
  );
};


const HomeScreen = ({ navigation }) => {
  return (
    <ScrollView>
      <Pressable 
        onPress={() =>
          navigation.navigate('Profile', { name: 'Алексей Ковалев', photo: require('./assets/avatar.jpg'), phone: "+79015017137" })
        }
        style={styles.button}
      >
      <View style={styles.container}>
        <Image style = {styles.picture}
        source={require('./assets/avatar.jpg')}
        />
         <Text style={styles.text}>Алексей Ковалев</Text>
         </View>
      </Pressable>
      <Pressable
        onPress={() =>
          navigation.navigate('Profile', { name: 'Джефф Безос', photo: require('./assets/avatar2.jpg'), phone: "+79524333963" })
        }
        style={styles.button}
      >
      <View style={styles.container}>
        <Image style = {styles.picture}
        source={require('./assets/avatar2.jpg')}
        />
         <Text style={styles.text}>Джефф Безос</Text>
         </View>
      </Pressable>
      <Pressable
        onPress={() =>
          navigation.navigate('Profile', { name: 'Алексей Ковалев', photo: require('./assets/avatar.jpg'), phone: "+79015017137" })
        }
        style={styles.button}
      >
      <View style={styles.container}>
        <Image style = {styles.picture}
        source={require('./assets/avatar.jpg')}
        />
         <Text style={styles.text}>Алексей Ковалев</Text>
         </View>
      </Pressable>
      <Pressable
        onPress={() =>
          navigation.navigate('Profile', { name: 'Джефф Безос', photo: require('./assets/avatar2.jpg'), phone: "+79524333963" })
        }
        style={styles.button}
      >
      <View style={styles.container}>
        <Image style = {styles.picture}
        source={require('./assets/avatar2.jpg')}
        />
         <Text style={styles.text}>Джефф Безос</Text>
         </View>
      </Pressable>
      <Pressable
        onPress={() =>
          navigation.navigate('Profile', { name: 'Алексей Ковалев', photo: require('./assets/avatar.jpg'), phone: "+79015017137" })
        }
        style={styles.button}
      >
      <View style={styles.container}>
        <Image style = {styles.picture}
        source={require('./assets/avatar.jpg')}
        />
         <Text style={styles.text}>Алексей Ковалев</Text>
         </View>
      </Pressable>
      <Pressable
        onPress={() =>
          navigation.navigate('Profile', { name: 'Джефф Безос', photo: require('./assets/avatar2.jpg'), phone: "+79524333963" })
        }
        style={styles.button}
      >
      <View style={styles.container}>
        <Image style = {styles.picture}
        source={require('./assets/avatar2.jpg')}
        />
         <Text style={styles.text}>Джефф Безос</Text>
         </View>
      </Pressable>
      <Pressable
        onPress={() =>
          navigation.navigate('Profile', { name: 'Алексей Ковалев', photo: require('./assets/avatar.jpg'), phone: "+79015017137" })
        }
        style={styles.button}
      >
      <View style={styles.container}>
        <Image style = {styles.picture}
        source={require('./assets/avatar.jpg')}
        />
         <Text style={styles.text}>Алексей Ковалев</Text>
         </View>
      </Pressable>
      <Pressable
        onPress={() =>
          navigation.navigate('Profile', { name: 'Джефф Безос', photo: require('./assets/avatar2.jpg'), phone: "+79524333963" })
        }
        style={styles.button}
      >
      <View style={styles.container}>
        <Image style = {styles.picture}
        source={require('./assets/avatar2.jpg')}
        />
         <Text style={styles.text}>Джефф Безос</Text>
         </View>
      </Pressable>
      <Pressable
        onPress={() =>
          navigation.navigate('Profile', { name: 'Алексей Ковалев', photo: require('./assets/avatar.jpg'), phone: "+79015017137" })
        }
        style={styles.button}
      >
      <View style={styles.container}>
        <Image style = {styles.picture}
        source={require('./assets/avatar.jpg')}
        />
         <Text style={styles.text}>Алексей Ковалев</Text>
         </View>
      </Pressable>
      <Pressable
        onPress={() =>
          navigation.navigate('Profile', { name: 'Джефф Безос', photo: require('./assets/avatar2.jpg'), phone: "+79524333963" })
        }
        style={styles.button}
      >
      <View style={styles.container}>
        <Image style = {styles.picture}
        source={require('./assets/avatar2.jpg')}
        />
         <Text style={styles.text}>Джефф Безос</Text>
         </View>
      </Pressable>
      <Pressable
        onPress={() =>
          navigation.navigate('Profile', { name: 'Алексей Ковалев', photo: require('./assets/avatar.jpg'), phone: "+79015017137" })
        }
        style={styles.button}
      >
      <View style={styles.container}>
        <Image style = {styles.picture}
        source={require('./assets/avatar.jpg')}
        />
         <Text style={styles.text}>Алексей Ковалев</Text>
         </View>
      </Pressable>
      <Pressable
        onPress={() =>
          navigation.navigate('Profile', { name: 'Джефф Безос', photo: require('./assets/avatar2.jpg'), phone: "+79524333963" })
        }
        style={styles.button}
      >
      <View style={styles.container}>
        <Image style = {styles.picture}
        source={require('./assets/avatar2.jpg')}
        />
         <Text style={styles.text}>Джефф Безос</Text>
         </View>
      </Pressable>
      </ScrollView>
  );
};

const ProfileScreen = ({ navigation, route }) => {
  return (
  <View style={styles.profile}>
      <Image style = {styles.profilePicture}
        source={route.params.photo}
        />
      <Text style={styles.profileText}>{route.params.name}</Text>
      <Text style={styles.phoneNumber}> {route.params.phone} </Text> 

      <View style={styles.actionContainer}>
    
        <TouchableOpacity  style={{flex: 1}}
          onPress={() => Linking.openURL("tel:"+route.params.phone)

          }>

          <Image style = {styles.icon}
                  source={{
                  uri: 'https://sun9-24.userapi.com/impg/IZciE5BzErQXOTPCYHeRVMFrQGYuT1jkPeyJ_Q/Kl5gttw5xSI.jpg?size=128x129&quality=95&sign=7fc1e3ce0c6eab7372338f150d954b08&type=album',
                  }}
                />
        </TouchableOpacity>


        <TouchableOpacity  style={{flex: 1}}
          onPress={() => Linking.openURL("sms:"+route.params.phone)

          }>

          <Image style = {styles.icon}
                  source={{
                  uri: 'https://sun9-60.userapi.com/impg/nbvYMUUT1QoakRrTiQ0abqeDZFJqdeXfv3cuiA/o_zUh8Q6w5I.jpg?size=126x126&quality=95&sign=aac187ab399f5a135ca24b80448b79c4&type=album',
                  }}
                />
        </TouchableOpacity>

        <TouchableOpacity  style={{flex: 1}}
          onPress={() =>
            navigation.navigate('VideoCall', {name: route.params.name, photo: route.params.photo, phone: route.params.phone})
          }>
          <Image style = {styles.icon} 
            source={{
            uri: 'https://sun9-46.userapi.com/impg/oCSyIQlxo-yh3cPzx8_j9vgJ4vGln5v6tm4cDA/GOJT88kNPos.jpg?size=126x126&quality=95&sign=c648c8aa3665ac0b6ad7ff446752f9ef&type=album',
            }}
          />
        </TouchableOpacity >
        

      </View>
            <ShareExample title={route.params.name+" "+route.params.phone}/>

    </View> 
     
)};

const CallScreen = ({ navigation, route }) => {
  return (
      <ImageBackground style={{ flex: 1}} 
        source={route.params.photo}>
        <View style={{alignItems: "center", justifyContent: "center", flex: 1, backgroundColor: 'rgba(1,1,1,0.7)'}}>
          <Image style={{width: 150, height: 150, borderRadius: 100}} source={route.params.photo}/>
          <Text style={{textAlign: "center", fontSize:28, color:"rgb(255,255,255)", fontWeight: "bold"}}>
           Calling {route.params.name}...
          </Text>
          <Text style={{textAlign: "center", fontSize:20, color:"rgb(255,255,255)"}}>{route.params.phone}</Text>
          <TouchableOpacity 
            onPress={() =>
            navigation.navigate('Profile', {name: route.params.name, photo: route.params.photo, phone: route.params.phone})
            }>
          <Image style={{width: 50, height: 50, marginTop: 150}} source={{uri: "https://i.ya-webdesign.com/images/red-phone-icon-png-8.png"}}/>
        </TouchableOpacity>
        </View>
      </ImageBackground>
     
)};

const VideoCallScreen = ({ navigation, route }) => {
  return (
      <ImageBackground style={{ flex: 1}} 
        source={route.params.photo}>
        <View style={{alignItems: "center", justifyContent: "center", flex: 1, backgroundColor: 'rgba(1,1,1,0.7)'}}>
          <Image style={{width: 150, height: 150, borderRadius: 100}} source={route.params.photo}/>
          <Text style={{textAlign: "center", fontSize:28, color:"rgb(255,255,255)", fontWeight: "bold", marginLeft: 20, marginRight: 20}}>
           Начало звонка с {route.params.name}...
          </Text>
          <Text style={{textAlign: "center", fontSize:20, color:"rgb(255,255,255)"}}>{route.params.phone}</Text>
          <TouchableOpacity 
            onPress={() =>
            navigation.navigate('Profile', {name: route.params.name, photo: route.params.photo, phone: route.params.phone})
            }>
          <Image style={{width: 50, height: 50, marginTop: 150}} source={{uri: "https://i.ya-webdesign.com/images/red-phone-icon-png-8.png"}}/>
        </TouchableOpacity>
        </View>
      </ImageBackground>
     
)};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    flexDirection: 'row',
    backgroundColor: "rgb(255, 255, 255)"
  },
  profile:{
    marginTop: 20,
    alignItems: "center",
    backgroundColor: "rgb(255, 255, 255)",
    borderRadius: 20
  },
  button: {
    height: 80,
    backgroundColor : "rgb(250, 250, 250)",
    borderRadius: 8,
    borderColor: "rgb(1,1,1)",
    margin: 1
  },
  text: {
    fontSize: 18,
    lineHeight: 21,
    fontWeight: 'bold',
    marginLeft: 20,
    marginTop: 30
  },
  picture: {
    marginTop: 15,
    marginLeft: 15,
    width: 50,
    height: 50,
    borderRadius: 100
  },
  profilePicture: {
    marginTop: 20,
    width: 150,
    height: 150,
    borderRadius: 10
  },
  profileText: {
    fontSize: 32,
    fontWeight: 'bold',
    marginTop: 20
  },
  phoneNumber: {
    fontSize: 20
  },
  icon: {
    marginTop: 15,
    marginLeft: 20,
    marginRight: 20,
    width: 50,
    height: 50,
    borderRadius: 100,
    marginBottom: 30
  },
  actionContainer: {
    marginRight: 80,
    marginLeft: 80,
    alignItems: 'center',
    flexDirection: "row",
    justifyContent: "center"
  }
});


export default Contacts;
