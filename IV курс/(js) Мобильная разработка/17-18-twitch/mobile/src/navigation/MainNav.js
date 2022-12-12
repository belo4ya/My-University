import React from 'react';
import {createBottomTabNavigator} from "@react-navigation/bottom-tabs";
import Following from "../screens/Following";
import Discover from "../screens/Discover";
import Browse from "../screens/Browse";
import Search from "../screens/Search";
import {AntDesign, Entypo, MaterialCommunityIcons} from "@expo/vector-icons";
import {getHeaderTitle} from '@react-navigation/elements';
import styled from "styled-components/native";
import Header from "../components/Header";

const Tab = createBottomTabNavigator();

const MainNav = ({navigation}) => {
        return (
            <>
                <Header navigation={navigation}/>
                <Tab.Navigator
                    initialRouteName="Following"
                    screenOptions={({route}) => ({
                        header: getHeader,
                        headerStyle: {backgroundColor: "#0e0e10"},
                        headerTintColor: "#ffffff",
                        tabBarIcon: ({color}) => {
                            const {Icon, name, style} = icons[route.name];
                            return <Icon name={name} size={24} color={color} style={style}/>
                        },
                        tabBarActiveTintColor: "#be93fd",
                        tabBarInactiveTintColor: "#ffffff",
                        tabBarItemStyle: {
                            paddingVertical: 4,
                        },
                        tabBarStyle: {
                            height: 60,
                            backgroundColor: "#0e0e10",
                            paddingHorizontal: 8,
                        },
                    })}
                >
                    <Tab.Screen name="Following" component={Following} options={{title: "Отслеживаемое"}}/>
                    <Tab.Screen name="Discover" component={Discover} options={{title: "Поиск"}}/>
                    <Tab.Screen name="Browse" component={Browse} options={{title: "Просмотр"}}/>
                    <Tab.Screen name="Search" component={Search} options={{title: "Поиск", headerShown: false}}/>
                </Tab.Navigator>
            </>
        )
            ;
    }
;

const getHeader = ({route, options}) => {
    const title = getHeaderTitle(options, route.name)
    return (
        <Container>
            <Title>{title}</Title>
        </Container>
    );
};

const Container = styled.View`
  background: #0e0e10;
  padding: 4px 16px 16px;
  margin-bottom: -1px;
  display: flex;
`;

const Title = styled.Text`
  color: #ffffff;
  font-size: 36px;
  font-weight: 600;
`;

const icons = {
    Following: {
        Icon: Entypo,
        name: "heart",
    },
    Discover: {
        Icon: MaterialCommunityIcons,
        name: "compass-outline",
    },
    Browse: {
        Icon: MaterialCommunityIcons,
        name: "card-multiple-outline",
        style: {transform: [{rotate: "90deg"}]},
    },
    Search: {
        Icon: AntDesign,
        name: "search1",
    },
};

export default MainNav;