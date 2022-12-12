import React from 'react';
import BaseStreamCard from "./BaseStreamCard";

const StreamRecommended = ({channel, stream}) => {
    return (
        <BaseStreamCard options channel={channel} stream={stream}/>
    );
};

export default StreamRecommended;