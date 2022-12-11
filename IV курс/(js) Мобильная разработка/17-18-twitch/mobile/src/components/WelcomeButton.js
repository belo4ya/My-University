import React from 'react';
import styled, {css} from "styled-components/native";

const WelcomeButton = ({onPress, primary, children}) => {
    return (
        <ButtonContainer onPress={onPress} primary={primary}>
            <ButtonText primary={primary}>{children}</ButtonText>
        </ButtonContainer>
    );
};

const ButtonContainer = styled.TouchableOpacity`
  flex: 1;
  background: #a062fd;
  border-radius: 8px;
  border: 0;
  padding: 10px;
  margin: 8px;

  ${(props) => props.primary && css`
    background: #ffffff;
  `}
`;

const ButtonText = styled.Text`
  text-align: center;
  font-size: 14px;
  font-weight: 500;
  color: white;

  ${(props) => props.primary && css`
    color: #000000;
  `}
`;

export default WelcomeButton;