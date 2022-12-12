import React from 'react';
import StreamFollowed from "./stream/StreamFollowed";
import BaseFollowingSection from "./BaseFollowingSection";
import api from "../api";
import {makeViewersString} from "./stream/BaseStreamCard";

const YourActiveChannels = ({channels}) => {
    return (
        <BaseFollowingSection title="Ваши активные каналы">
            {channels.map(i => {
                const channel = i.channel
                const stream = i.stream
                return <StreamFollowed
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

export default YourActiveChannels;