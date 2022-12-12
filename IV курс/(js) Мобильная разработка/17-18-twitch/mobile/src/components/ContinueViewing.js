import React from 'react';
import BaseFollowingSection from "./BaseFollowingSection";
import StreamRecord from "./stream/StreamRecord";
import api from "../api";
import {makeSinceString} from "./stream/BaseStreamCard";

const ContinueViewing = ({records}) => {
    return (
        <BaseFollowingSection title="Ваши неактивные каналы">
            {records.map(i => {
                const channel = i.channel
                return <StreamRecord
                    key={i.id}
                    channel={{
                        name: channel.name,
                        avatar: api.baseURL + channel.avatar,
                    }}
                    stream={{
                        title: i.title,
                        category: i.category,
                        preview: api.baseURL + i.preview,
                    }}
                    since={makeSinceString(i.since)}
                />
            })}
        </BaseFollowingSection>
    );
};

export default ContinueViewing;