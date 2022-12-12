import React from 'react';
import styled from "styled-components/native";

const ChannelCard = ({mark}) => {
    return (
        <Container>
            <Card>
                <Channel>
                    <ChannelAvatar source={require("../../../assets/images/avatar.jpg")}/>
                    <ChannelDescription>
                        <ChannelTitle>betboom_ru</ChannelTitle>
                        {mark ? <MarkText>{mark}</MarkText> : null}
                    </ChannelDescription>
                </Channel>
                {mark ? <Marker/> : null}
            </Card>
        </Container>
    );
};

const Container = styled.View`
  display: flex;
  margin: 15px 0;
`

const Card = styled.View`
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
`

const Channel = styled.View`
  display: flex;
  flex-direction: row;
  align-items: center;
`

const ChannelAvatar = styled.Image`
  height: 36px;
  width: 36px;
  border-radius: 18px;
`

const ChannelDescription = styled.View`
  margin-left: 8px;
`

const ChannelTitle = styled.Text`
  color: #ffffff;
  font-weight: 500;
  font-size: 15px;
`

const MarkText = styled.Text`
  color: #b0b0bb;
  font-weight: 400;
  font-size: 13px;
  margin-top: 2px;
`

const Marker = styled.View`
  background: #b0b0bb;
  width: 8px;
  height: 8px;
  border-radius: 4px;
  margin-right: 4px;
`

export default ChannelCard;