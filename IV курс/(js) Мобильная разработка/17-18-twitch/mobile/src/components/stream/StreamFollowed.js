import React from 'react';
import BaseStreamCard from "./BaseStreamCard";

const StreamFollowed = ({channel, stream}) => {
    return (
        <BaseStreamCard channel={channel} stream={stream}/>
    );
};

export default StreamFollowed;