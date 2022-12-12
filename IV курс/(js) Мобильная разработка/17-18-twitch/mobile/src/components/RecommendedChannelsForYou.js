import React from 'react';
import BaseFollowingSection from "./BaseFollowingSection";
import StreamRecommended from "./stream/StreamRecommended";

const RecommendedChannelsForYou = () => {
    return (
        <BaseFollowingSection title="Рекомендуемые вам каналы">
            <StreamRecommended/>
            <StreamRecommended/>
            <StreamRecommended/>
            <StreamRecommended/>
            <StreamRecommended/>
            <StreamRecommended/>
            <StreamRecommended/>
        </BaseFollowingSection>
    );
};

export default RecommendedChannelsForYou;