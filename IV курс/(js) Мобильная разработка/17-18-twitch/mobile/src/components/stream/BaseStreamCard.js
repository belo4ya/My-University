import React from 'react';
import styled from "styled-components/native";

const BaseStreamCard = () => {
    return (
        <Container>
            <Preview source={require("../../../assets/images/preview.jpg")}/>
            <Info>
                <InfoContainer>
                    <Channel>
                        <ChannelAvatar source={require("../../../assets/images/avatar.jpg")}/>
                        <ChannelTitle>DreadzTV</ChannelTitle>
                    </Channel>
                    <Title numberOfLines={1}>Олег вернет все | t.me/realknp</Title>
                    <Category numberOfLines={1}>Dark and Darker</Category>
                </InfoContainer>
                <TagsContainer>
                    <Tag>English</Tag>
                    <Tag>Русский</Tag>
                    <Tag>Русский</Tag>
                    <Tag>Русский</Tag>
                </TagsContainer>
            </Info>
        </Container>
    );
};

const Container = styled.View`
  display: flex;
  flex-direction: row;
  margin: 15px 0;
`

const Preview = styled.Image`
  width: 140px;
  height: 80px;
`

const Info = styled.View`
  margin-left: 12px;
`

const InfoContainer = styled.View`
  width: 220px;
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