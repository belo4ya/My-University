import React from 'react';
import styled from "styled-components/native";
import {AntDesign, MaterialCommunityIcons, MaterialIcons} from "@expo/vector-icons";
import {TouchableOpacity} from "react-native";

const Header = ({navigation}) => {
    return (
        <Container>
            <TouchableOpacity onPress={() => navigation.navigate("Settings")}>
                <Avatar source={require("../../assets/images/avatar.jpg")}/>
            </TouchableOpacity>
            <IconContainer>
                <IconItem>
                    <AntDesign name="inbox" size={24} color="#ffffff"/>
                </IconItem>
                <IconItem>
                    <MaterialIcons name="chat-bubble-outline" size={24} color="#ffffff"/>
                </IconItem>
                <IconItem>
                    <CreateIconContainer>
                        <MaterialCommunityIcons name="access-point" size={22} color="#ffffff"/>
                        <CreateIconText>Создать</CreateIconText>
                    </CreateIconContainer>
                </IconItem>
            </IconContainer>
        </Container>
    );
};

const Container = styled.View`
  background: #0e0e10;
  height: 60px;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  padding: 4px 16px;
`;

const Avatar = styled.Image`
  height: 32px;
  width: 32px;
  border-radius: 16px;
`;

const IconContainer = styled.View`
  display: flex;
  flex-direction: row;
  align-items: center;
`;

const IconItem = styled.TouchableOpacity`
  margin-left: 28px;
`;

const CreateIconContainer = styled.View`
  display: flex;
  flex-direction: row;
  align-items: center;
  background: #3e3e40;
  border-radius: 20px;
  padding: 8px 16px;
`;

const CreateIconText = styled.Text`
  margin-left: 6px;
  color: #ffffff;
  font-size: 12px;
  font-weight: 500;
`;

export default Header;