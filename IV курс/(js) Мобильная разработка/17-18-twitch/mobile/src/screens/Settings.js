import React, {useContext} from 'react';
import styled from "styled-components/native";
import {UserContext} from "../navigation/context";

const Settings = ({navigation}) => {
    const {setUser} = useContext(UserContext)
    const logOut = () => {
        console.log("logOut")
        setUser(true)
        navigation.navigate("Welcome")
    }
    return (
        <Container>
            <ButtonContainer onPress={logOut}>
                <ButtonText>Выйти</ButtonText>
            </ButtonContainer>
        </Container>
    );
};

const Container = styled.View`
  flex: 1;
  background: #18181b;
  padding: 0 16px;
  align-items: center;
  flex-direction: row;
  justify-content: center;
`

const ButtonContainer = styled.TouchableOpacity`
  flex: 1;
  border-width: 1px;
  background: #1f1f23;
  border-color: #dddde2;
`

const ButtonText = styled.Text`
  text-align: center;
  color: #ffffff;
  font-weight: 500;
  padding: 12px;
`

export default Settings;