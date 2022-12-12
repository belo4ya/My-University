import React, {useContext, useState} from 'react';
import styled from "styled-components/native";
import {Octicons} from "@expo/vector-icons";
import FormInput from "../components/FormInput";
import {UserContext} from "../navigation/context";
import api from "../api";
import {ToastAndroid} from "react-native";

const LogIn = ({navigation}) => {
    const {setUser} = useContext(UserContext)
    const [username, setUsername] = useState("")
    const [password, setPassword] = useState("")

    const logIn = (username, password) => {
        api.logIn(username, password).then(resp => {
            const access_token = resp.data["access_token"]
            api.getUserinfo(resp.data["access_token"]).then(resp => {
                setUser({...resp.data, access_token: access_token})
                console.log("logIn success:", resp.data)
                navigation.navigate("MainNav")
            })
        }).catch(e => {
            console.log("logIn fail:", e)
            ToastAndroid.show('Неверный логин или пароль, попробуйте еще раз', 3)
        })
    }

    return (
        <Container>
            <Form>
                <Field>
                    <FieldLabel>Имя пользователя</FieldLabel>
                    <FormInput
                        textContentType="username"
                        cursorColor="#9146ff"
                        value={username}
                        onChangeText={username => setUsername(username)}
                    />
                </Field>
                <Field>
                    <FieldLabel>Пароль</FieldLabel>
                    <FormInput
                        textContentType="password"
                        secureTextEntry={true}
                        Icon={() => <Octicons name="eye" size={24} color="#afafba"/>}
                        value={password}
                        onChangeText={password => setPassword(password)}
                    />
                </Field>
                <Link>Создать аккаунт</Link>
                <ButtonContainer onPress={() => logIn(username, password)}>
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
