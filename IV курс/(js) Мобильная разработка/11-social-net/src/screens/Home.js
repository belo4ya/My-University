import React from 'react';
import {View,Text,Image,ImageBackground,TouchableOpacity} from 'react-native';
import {ScrollView,TextInput} from 'react-native-gesture-handler';
import Icon from '@expo/vector-icons/Entypo';
import Posts from '../screens/Posts'

export default class Home extends React.Component{
  
    state={
        popularSelected:true
    }
    onTabPressed=()=>{
        this.setState({popularSelected:!this.state.popularSelected})
    }
    render(){
        return(
          <ScrollView

            showsVerticalScrollIndicator={false}
            style={{
                height:"100%",
                backgroundColor:"#2195f1"
            }}
          >
              <View style={{
                  height:260,
                  width:"100%",
                  paddingHorizontal:35
              }}>
                  <View style={{
                      flexDirection:"row",
                      width:"100%",
                      paddingTop:40,
                      alignItems:"center"
                  }}>
                      <View style={{
                          width:"50%"
                      }}>
                          <Image source={require('../images/Untitled.png')}
                            style={{width:20,height:20}}/>
                      </View>
                      <View style={{
                          width:"50%",
                          alignItems:"flex-end",
                      }}>
                          <Icon name = "dots-two-vertical"
                            size={22}
                            color="#d2d2d2"
                            style={{
                                marginRight:-7,
                                marginTop:7
                            }}/>
                      </View>
                  </View>


                <Text style={{
                    fontFamily:"Bold",
                    fontSize:25,
                    color:"#FFF",
                    paddingVertical:25
                }}>Социальная сеть, для ...</Text>

                <View style={{
                    flexDirection:"row",
                    borderColor:"#ffffff",
                    borderRadius:20,
                    borderWidth:1,
                    paddingVertical:5,
                    alignItems:"center"
                }}>
                    <TextInput
                        placeholder="Найти льва..."
                        placeholderTextColor="#ffffff"
                        style={{
                            paddingHorizontal:20,
                            fontFamily:"Medium",
                            fontSize:11,
                            width:"90%",
                            color:"#ffffff",
                        }}
                    />
                    <Icon name="magnifying-glass"
                          size={15}
                          color="#ffffff"/>
                </View>

              </View>

              <View style={{
                  backgroundColor:"#FFF",
                  borderTopLeftRadius:40,
                  borderTopRightRadius:40,
                  height:1800,
                  paddingHorizontal:35
              }}>
                  <View style={{
                      flexDirection:"row",
                      paddingTop:20
                  }}>
                      <TouchableOpacity
                        onPress={this.onTabPressed}
                        style={{
                            borderBottomColor:this.state.popularSelected ? "#2195f1":"#FFF",
                            borderBottomWidth:4,
                            paddingVertical:6
                        }}
                      >
                          <Text style={{
                              fontFamily:"Bold",
                              color:this.state.popularSelected ? "#2195f1":"#9ca1a2"
                          }}>Самые популярные</Text>
                      </TouchableOpacity>


                      <TouchableOpacity
                        onPress={this.onTabPressed}
                        style={{
                            borderBottomColor:this.state.popularSelected ? "#FFF":"#2195f1",
                            borderBottomWidth:4,
                            paddingVertical:6,
                            marginLeft:30
                        }}
                      >
                          <Text style={{
                              fontFamily:"Bold",
                              color:this.state.popularSelected ? "#9ca1a2":"#2195f1"
                          }}>Последние</Text>
                      </TouchableOpacity>
                  </View>

                  <View style={{
                      flexDirection:"row"
                  }}>
                      <Posts
                        onPress={()=>this.props.navigation.navigate('Detail')}
                        name="Алексей Ковалев"
                        profile={require('../images/avatar.jpg')}
                        photo={require('../images/lion_1.jpg')}
                      />
                      <View style={{
                          height:160,
                          backgroundColor:"#2195f1",
                          width:20,
                          marginLeft:20,
                          marginTop:120,
                          borderTopLeftRadius:20,
                          borderBottomLeftRadius:20
                      }}>
                      </View>
                  </View>

                  <View style={{
                      flexDirection:"row"
                  }}>
                      <View style={{
                          height:160,
                          backgroundColor:"#2195f1",
                          width:20,
                          marginLeft:-40,
                          marginRight:20,
                          marginTop:120,
                          borderTopRightRadius:20,
                          borderBottomRightRadius:20
                      }}>
                      </View>
                      <Posts
                        onPress={()=>this.props.navigation.navigate('Detail')}
                        name="Алексей Ковалев"
                        profile={require('../images/avatar.jpg')}
                        photo={require('../images/lion_2.jpg')}
                      />
                  </View>

                  <View style={{flexDirection:"row"}}>
                      <Posts
                        onPress={()=>this.props.navigation.navigate('Detail')}
                        name="Алексей Ковалев"
                        profile={require('../images/avatar.jpg')}
                        photo={require('../images/lion_3.jpg')}
                      />
                      <View style={{
                          height:160,
                          backgroundColor:"#2195f1",
                          width:20,
                          marginLeft:20,
                          marginTop:120,
                          borderTopLeftRadius:20,
                          borderBottomLeftRadius:20
                      }}>
                      </View>
                  </View>

                  <View style={{
                      flexDirection:"row"
                  }}>
                      <View style={{
                          height:160,
                          backgroundColor:"#2195f1",
                          width:20,
                          marginLeft:-40,
                          marginRight:20,
                          marginTop:120,
                          borderTopRightRadius:20,
                          borderBottomRightRadius:20
                      }}>
                      </View>
                      <Posts
                        onPress={()=>this.props.navigation.navigate('Detail')}
                        name="Алексей Ковалев"
                        profile={require('../images/avatar.jpg')}
                        photo={require('../images/lion_1.jpg')}
                      />
                  </View>

                  <View style={{flexDirection:"row"}}>
                      <Posts
                        onPress={()=>this.props.navigation.navigate('Detail')}
                        name="Алексей Ковалев"
                        profile={require('../images/avatar.jpg')}
                        photo={require('../images/lion_2.jpg')}
                      />
                      <View style={{
                          height:160,
                          backgroundColor:"#2195f1",
                          width:20,
                          marginLeft:20,
                          marginTop:120,
                          borderTopLeftRadius:20,
                          borderBottomLeftRadius:20
                      }}>
                      </View>
                  </View>
              </View>

          </ScrollView>
        )
    }
}