import React from 'react';
import styled from "styled-components/native";
import {Octicons} from "@expo/vector-icons";
import FormInput from "../components/FormInput";

const LogIn = ({navigation, logIn}) => {
    const _logIn = () => {
        logIn()
        navigation.navigate("MainNav")
    }
    return (
        <Container>
            <Form>
                <Field>
                    <FieldLabel>Имя пользователя</FieldLabel>
                    <FormInput
                        textContentType="username"
                        cursorColor="#9146ff"
                    />
                </Field>
                <Field>
                    <FieldLabel>Пароль</FieldLabel>
                    <FormInput
                        textContentType="password"
                        secureTextEntry={true}
                        Icon={() => <Octicons name="eye" size={24} color="#afafba"/>}
                    />
                </Field>
                <Link>Создать аккаунт</Link>
                <ButtonContainer onPress={_logIn}>
                    <ButtonText>Войти</ButtonText>
                </ButtonContainer>
            </Form>
        </Container>
    );
};

const Container = styled.View`
  flex: 1;
  background: #0e0e10;
  padding: 0 32px;
`;

const Form = styled.View`
  margin-top: 50px
`

const Field = styled.View`
  margin-top: 16px;
`;

const FieldLabel = styled.Text`
  font-size: 16px;
  font-weight: 600;
  color: #ffffff;
`;

const Link = styled.Text`
  margin-top: 16px;
  font-weight: 600;
  color: #ab70ff;
`;

const ButtonContainer = styled.TouchableOpacity`
  display: flex;
  background: #9146ff;
  margin-top: 16px;
  border-radius: 8px;
`;

const ButtonText = styled.Text`
  color: #ffffff;
  text-align: center;
  font-weight: 600;
  padding: 10px;
`;

export default LogIn;