import React from 'react';
import BaseFollowingSection from "./BaseFollowingSection";
import ChannelCard from "./channel/ChannelCard";

const YourInactiveChannels = ({channels}) => {
    return (
        <BaseFollowingSection title="Продолжить просмотр">
            {channels.map((i) => (
                <ChannelCard
                    key={i.id}
                    mark={"34 новых видео"}
                />
            ))}
        </BaseFollowingSection>
    );
};

export default YourInactiveChannels;