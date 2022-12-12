import React from 'react';
import styled from "styled-components/native";
import ChannelCard from "../components/channel/ChannelCard";
import StreamFollowed from "../components/stream/StreamFollowed";
import StreamRecommended from "../components/stream/StreamRecommended";
import StreamRecord from "../components/stream/StreamRecord";

const Following = () => {
    return (
        <Container>
            <Section>
                <SectionTitle>Ваши активные каналы</SectionTitle>
                <SectionContent>
                    <StreamFollowed/>
                    <StreamFollowed/>
                    <StreamFollowed/>
                </SectionContent>
            </Section>
            <Section>
                <SectionTitle>Рекомендуемые вам каналы</SectionTitle>
                <SectionContent>
                    <StreamRecommended/>
                    <StreamRecommended/>
                    <StreamRecommended/>
                    <StreamRecommended/>
                    <StreamRecommended/>
                    <StreamRecommended/>
                    <StreamRecommended/>
                </SectionContent>
            </Section>
            <Section>
                <SectionTitle>Продолжить просмотр</SectionTitle>
                <SectionContent>
                    <StreamRecord/>
                    <StreamRecord/>
                </SectionContent>
            </Section>
            <Section>
                <SectionTitle>Ваши неактивные каналы</SectionTitle>
                <SectionContent>
                    <ChannelCard mark={"34 новых видео"}/>
                    <ChannelCard mark={"12 новых видео"}/>
                    <ChannelCard mark={"5 новых видео"}/>
                    <ChannelCard mark={"4 новых видео"}/>
                    <ChannelCard/>
                    <ChannelCard/>
                    <ChannelCard/>
                    <ChannelCard/>
                    <ChannelCard/>
                    <ChannelCard/>
                    <ChannelCard/>
                    <ChannelCard/>
                    <ChannelCard/>
                </SectionContent>
            </Section>
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