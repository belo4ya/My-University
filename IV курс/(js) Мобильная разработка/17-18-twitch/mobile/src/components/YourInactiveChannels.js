import React from 'react';
import BaseFollowingSection from "./BaseFollowingSection";
import ChannelCard from "./channel/ChannelCard";

const YourInactiveChannels = () => {
    return (
        <BaseFollowingSection title="Продолжить просмотр">
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
        </BaseFollowingSection>
    );
};

export default YourInactiveChannels;