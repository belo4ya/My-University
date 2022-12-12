import React from 'react';
import styled from "styled-components/native";
import YourActiveChannels from "../components/YourActiveChannels";
import RecommendedChannelsForYou from "../components/RecommendedChannelsForYou";
import ContinueViewing from "../components/ContinueViewing";
import YourInactiveChannels from "../components/YourInactiveChannels";

const Following = () => {
    return (
        <Container>
            <YourActiveChannels/>
            <RecommendedChannelsForYou/>
            <ContinueViewing/>
            <YourInactiveChannels/>
        </Container>
    );
};

const Container = styled.ScrollView`
  flex: 1;
  background: #0e0e10;
  padding: 0 16px;
`

const Section = styled.View`
  margin-top: 30px;
`

const SectionTitle = styled.Text`
  color: #ffffff;
  font-size: 20px;
  font-weight: bold;
`

const SectionContent = styled.View`
  margin-top: 15px;
`

export default Following;