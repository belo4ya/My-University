import React from 'react';
import BaseStreamCard from "./BaseStreamCard";

const StreamRecord = ({channel, stream, since}) => {
    return (
        <BaseStreamCard channel={channel} stream={stream} since={since}/>
    );
};

export default StreamRecord;