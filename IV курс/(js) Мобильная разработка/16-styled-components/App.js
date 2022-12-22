import styled from 'styled-components/native';
import {LinearGradient} from 'expo-linear-gradient';

import React, {useState} from 'react';
import {Switch} from 'react-native';
import {AntDesign, Feather, FontAwesome, MaterialCommunityIcons} from '@expo/vector-icons';

import creditCard from './assets/images/credit-card.png';

const Container = styled.ScrollView``;

const Wrapper = styled.View`
  background: #000;
  flex: 1;
`;

const Header = styled(LinearGradient)`
  height: 280px;
`;

const HeaderContainer = styled.SafeAreaView`
  flex: 1;
  align-items: center;
  justify-content: center;
`;

const Title = styled.Text`
  color: #fff;
  font-size: 12px;
  font-weight: bold;
`;

const BalanceContainer = styled.View`
  margin: 5px 0;
  flex-direction: row;
  align-items: center;
`;

const Value = styled.Text`
  font-size: 34px;
  color: #fff;
  font-weight: 200;
`;

const Bold = styled.Text`
  font-weight: bold;
`;

const EyeButton = styled.TouchableOpacity`
  margin-left: 10px;
`;

const Info = styled.Text`
  color: #fff;
  font-size: 12px;
  font-weight: bold;
`;

const Actions = styled.View`
  flex-direction: row;
  margin-top: 40px;
`;

const Action = styled.TouchableOpacity`
  flex-direction: row;
  align-items: center;
  justify-content: center;
  border: 1px solid rgba(255, 255, 255, 0.6);
  width: 150px;
  height: 45px;
  border-radius: 25px;
  margin: 0 10px;
`;

const ActionLabel = styled.Text`
  font-size: 12px;
  color: #fff;
  margin-left: 10px;
`;

const UseBalance = styled.View`
  background: #1C1C1E;
  height: 60px;
  flex-direction: row;
  padding: 0 16px;
  align-items: center;
  justify-content: space-between;
`;

const UseBalanceTitle = styled.Text`
  color: #fff;
  font-size: 12px;
  font-weight: 500;
`;

const PaymentMethods = styled.View`
  margin-top: 25px;
  padding: 0 14px;
`;

const PaymentMethodsTitle = styled.Text`
  color: #8E8E93;
  font-size: 12px;
  text-transform: uppercase;
`;

const Card = styled.View`
  background: #1E232A;
  padding: 20px;
  border-radius: 8px;
  margin-top: 10px;
`;

const CardBody = styled.View`
  flex-direction: row;
`;

const CardDetails = styled.View`
  flex: 1;
  margin-right: 40px;
`;

const CardTitle = styled.Text`
  font-size: 14px;
  font-weight: bold;
  color: #fff;
`;

const CardInfo = styled.Text`
  font-size: 10px;
  color: rgba(255, 255, 255, 0.8);
  margin-top: 15px;
`;

const Img = styled.Image`
  width: 60px;
`;

const AddButton = styled.TouchableOpacity`
  flex-direction: row;
  align-items: center;
  margin-top: 25px;
`;

const AddLabel = styled.Text`
  color: #0DB060;
  font-size: 14px;
  font-weight: bold;
  margin-left: 15px;
`;

const UseTicketContainer = styled.View`
  align-items: center;
  margin-top: 25px;
`;

const UseTicketButton = styled.TouchableOpacity`
  flex-direction: row;
`;

const UseTicketLabel = styled.Text`
  color: #0DB060;
  font-size: 14px;
  font-weight: bold;
  margin-left: 15px;
  text-decoration-line: underline;
`;

// noinspection JSUnusedGlobalSymbols
export default function App() {
  const [isVisible, setIsVisible] = useState(true);
  const [useBalance, setUseBalance] = useState(true);

  function handleToggleVisibility() {
    setIsVisible((prevState) => !prevState);
  }

  function handleToggleUseBalance() {
    setUseBalance((prevState) => !prevState);
  }

  return (
    <Wrapper>
      <Container>
        <Header
          colors={
            useBalance
              ? ['#52E78C', '#1AB563']
              : ['#D3D3D3', '#868686']
          }
        >
          <HeaderContainer>
            <Title>Wallet Balance</Title>

            <BalanceContainer>
              <Value>
                $ <Bold>{isVisible ? '798.611,65' : '----'}</Bold>
              </Value>

              <EyeButton onPress={handleToggleVisibility}>
                <Feather
                  name={isVisible ? 'eye' : 'eye-off'}
                  size={28}
                  color="#fff"
                />
              </EyeButton>
            </BalanceContainer>

            <Info>
              Your balance is 100%
            </Info>

            <Actions>
              <Action>
                <MaterialCommunityIcons name="cash" size={28} color="#fff"/>
                <ActionLabel>Add Funds</ActionLabel>
              </Action>

              <Action>
                <FontAwesome name="bank" size={20} color="#fff"/>
                <ActionLabel>Withdraw</ActionLabel>
              </Action>
            </Actions>
          </HeaderContainer>
        </Header>

        <UseBalance>
          <UseBalanceTitle>
            Block funds
          </UseBalanceTitle>

          <Switch
            value={useBalance}
            onValueChange={handleToggleUseBalance}
          />
        </UseBalance>

        <PaymentMethods>
          <PaymentMethodsTitle>
            Form of payment
          </PaymentMethodsTitle>

          <Card>
            <CardBody>
              <CardDetails>
                <CardTitle>
                  Register your credit card
                </CardTitle>
                <CardInfo>
                  Register a credit card to be able to make payments even if you don't have a balance on Wallet.
                </CardInfo>
              </CardDetails>

              <Img source={creditCard} resizeMode="contain"/>
            </CardBody>

            <AddButton>
              <AntDesign name="pluscircleo" size={30} color="#0DB060"/>
              <AddLabel>
                Add credit card
              </AddLabel>
            </AddButton>
          </Card>

          <UseTicketContainer>
            <UseTicketButton>
              <MaterialCommunityIcons name="ticket-outline" size={20} color="#0DB060"/>
              <UseTicketLabel>
                Use promo code
              </UseTicketLabel>
            </UseTicketButton>
          </UseTicketContainer>
        </PaymentMethods>
      </Container>
    </Wrapper>
  );
}
