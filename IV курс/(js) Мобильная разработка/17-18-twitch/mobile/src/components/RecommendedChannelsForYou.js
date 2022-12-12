import React from 'react';
import BaseFollowingSection from "./BaseFollowingSection";
import StreamRecommended from "./stream/StreamRecommended";
import api from "../api";
import {makeViewersString} from "./stream/BaseStreamCard";

const RecommendedChannelsForYou = ({recommendations}) => {
    return (
        <BaseFollowingSection title="Рекомендуемые вам каналы">
            {recommendations.map(i => {
                const channel = i.channel
                const stream = i.stream
                return <StreamRecommended
                    key={i.id}
                    channel={{
                        name: channel.name,
                        avatar: api.baseURL + channel.avatar,
                    }}
                    stream={{
                        title: stream.title,
                        category: stream.category,
                        tags: stream.tags,
                        preview: api.baseURL + stream.preview,
                        viewers: makeViewersString(stream.viewers)
                    }}
                />
            })}
        </BaseFollowingSection>
    );
};

export default RecommendedChannelsForYou;