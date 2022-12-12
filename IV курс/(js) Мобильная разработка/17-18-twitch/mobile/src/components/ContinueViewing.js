import React from 'react';
import BaseFollowingSection from "./BaseFollowingSection";
import StreamRecord from "./stream/StreamRecord";

const ContinueViewing = () => {
    return (
        <BaseFollowingSection title="Ваши неактивные каналы">
            <StreamRecord/>
            <StreamRecord/>
        </BaseFollowingSection>
    );
};

export default ContinueViewing;