import React from 'react';
import StreamFollowed from "./stream/StreamFollowed";
import styled from "styled-components/native";
import BaseFollowingSection from "./BaseFollowingSection";

const YourActiveChannels = () => {
    return (
        <BaseFollowingSection title="Ваши активные каналы">
            <StreamFollowed/>
            <StreamFollowed/>
            <StreamFollowed/>
        </BaseFollowingSection>
    );
};

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

export default YourActiveChannels;