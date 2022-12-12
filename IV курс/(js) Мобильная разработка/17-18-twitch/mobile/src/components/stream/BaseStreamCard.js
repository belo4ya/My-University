import React from 'react';
import styled from "styled-components/native";
import {SimpleLineIcons} from "@expo/vector-icons";
import {TouchableOpacity, View} from "react-native";

const BaseStreamCard = ({options, since}) => {
    return (
        <Container>
            <Left style={since ? {alignItems: "center"} : {}}>
                <View>
                    <Preview source={require("../../../assets/images/preview.jpg")}/>
                    {!since ? (
                        <Viewers>
                            <ViewersIcon/>
                            <ViewersText>3,7 тыс.</ViewersText>
                        </Viewers>
                    ) : null}
                </View>
                <Info>
                    <Channel>
                        <ChannelAvatar source={require("../../../assets/images/avatar.jpg")}/>
                        <ChannelTitle>DreadzTV</ChannelTitle>
                    </Channel>
                    <Title numberOfLines={1}>Олег вернет все | t.me/realknp</Title>
                    <Category numberOfLines={1}>{since ? `${since} | ` : ""}Dark and Darker</Category>
                    {!since ? (
                        <TagsContainer>
                            <Tag>English</Tag>
                            <Tag>Русский</Tag>
                            <Tag>Русский</Tag>
                            <Tag>Русский</Tag>
                        </TagsContainer>
                    ) : null}
                </Info>
            </Left>
            {options ? (
                    <TouchableOpacity style={{marginTop: 8}}>
                        <SimpleLineIcons name="options-vertical" size={18} color="#dddde2"/>
                    </TouchableOpacity>
                )
                : null}
        </Container>
    );
};

const Container = styled.TouchableOpacity`
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  margin: 15px 0;
`

const Left = styled.View`
  display: flex;
  flex-direction: row;
`

const Preview = styled.Image`
  width: 140px;
  height: 80px;
`

const Viewers = styled.View`
  position: absolute;
  left: 4px;
  bottom: 4px;
  display: flex;
  flex-direction: row;
  align-items: center;
`

const ViewersIcon = styled.View`
  background: #ea1313;
  width: 8px;
  height: 8px;
  border-radius: 4px;
  margin-right: 4px;
`

const ViewersText = styled.Text`
  color: #ffffff;
  font-weight: 700;
  font-size: 13px;
  margin-left: 2px;
`

const Info = styled.View`
  display: flex;
  margin-left: 12px;
  width: 200px;
`

const Channel = styled.View`
  display: flex;
  flex-direction: row;
  align-items: center;
`

const ChannelAvatar = styled.Image`
  width: 20px;
  height: 20px;
  border-radius: 10px;
`

const ChannelTitle = styled.Text`
  color: #ffffff;
  font-weight: 500;
  margin-left: 4px;
  font-size: 15px;
`

const Title = styled.Text`
  color: #dddde2;
  font-weight: 500;
  font-size: 13px;
  margin-top: 4px;
`

const Category = styled.Text`
  color: #b0b0bb;
  font-weight: 400;
  font-size: 13px;
  margin-top: 4px;
`

const TagsContainer = styled.View`
  display: flex;
  flex-direction: row;
  margin-top: 8px;
`

const Tag = styled.Text`
  color: #ffffff;
  background: #323234;
  font-size: 12px;
  padding: 4px 8px;
  margin-right: 4px;
  border-radius: 12px;
`

export default BaseStreamCard;