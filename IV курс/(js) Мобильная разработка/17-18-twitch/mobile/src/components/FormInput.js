import React, {useState} from 'react';
import styled from "styled-components/native";

const FormInput = ({textContentType, secureTextEntry, Icon}) => {
    const [style, setStyle] = useState({backgroundColor: "#323234", borderColor: "#323234"})
    const onFocus = () => {
        setStyle({backgroundColor: "#18181b", borderColor: "#c296fd"})
    }
    const onBlur = () => {
        setStyle({backgroundColor: "#323234", borderColor: "#323234"})
    }
    return (
        <InputContainer style={{...style, borderWidth: 2}}>
            <FieldInput
                textContentType={textContentType}
                secureTextEntry={secureTextEntry}
                cursorColor="#9146ff"
                onFocus={onFocus}
                onBlur={onBlur}
                style={{backgroundColor: style.backgroundColor}}
            />
            {Icon ? Icon() : null}
        </InputContainer>
    );
};

const InputContainer = styled.View`
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  background: #323234;
  margin-top: 10px;
  padding: 12px;
  border-radius: 4px;
`

const FieldInput = styled.TextInput`
  flex: 1;
  background: #323234;
  color: #ffffff;
  font-size: 16px;
`;

export default FormInput;