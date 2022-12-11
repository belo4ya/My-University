import React from 'react';
import {ImageBackground, StyleSheet} from "react-native";
import styled from "styled-components/native";
import WelcomeButton from "../components/WelcomeButton";

const Welcome = ({navigation}) => {
    return (
        <ImageBackground
            source={require('../../assets/images/welcome.png')}
            style={StyleSheet.absoluteFill}
        >
            <Container>
                <WelcomeButton onPress={() => navigation.navigate("LogIn")}>Войти</WelcomeButton>
                <WelcomeButton onPress={() => navigation.navigate("SignUp")} primary>Регистрация</WelcomeButton>
            </Container>
        </ImageBackground>
    );
};

const Container = styled.View`
  display: flex;
  flex-direction: row;
  position: absolute;
  bottom: 20px;
  padding: 8px;
`;

export default Welcome;