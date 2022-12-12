import React from 'react';
import styled from "styled-components/native";

const BaseFollowingSection = ({title, children}) => {
    return (
        <Section>
            <SectionTitle>{title}</SectionTitle>
            <SectionContent>{children}</SectionContent>
        </Section>
    );
};

const Section = styled.View`
  margin-top: 30px;
`

const SectionTitle = styled.Text`
  color: #ffffff;
  font-size: 20px;
  font-weight: bold;
`

const SectionContent = styled.View`
  margin-top: 15px;
`

export default BaseFollowingSection;