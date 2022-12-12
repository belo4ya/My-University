import React, {useContext, useEffect, useState} from 'react';
import styled from "styled-components/native";
import YourActiveChannels from "../components/YourActiveChannels";
import RecommendedChannelsForYou from "../components/RecommendedChannelsForYou";
import ContinueViewing from "../components/ContinueViewing";
import YourInactiveChannels from "../components/YourInactiveChannels";
import {UserContext} from "../navigation/context";
import api from "../api";
import {useIsFocused} from "@react-navigation/native";

const Following = () => {
    const {user} = useContext(UserContext)
    const isFocused = useIsFocused();
    const [activeChannels, setActiveChannels] = useState([])
    const [recommendations, setRecommendations] = useState([])
    const [records, setRecords] = useState([])
    const [offlineChannels, setOfflineChannels] = useState([])

    useEffect(() => {
        api.getFollows(user.access_token).then(resp => {
            const active = []
            const offline = []
            resp.data.map(i => {
                i.active ? active.push(i) : offline.push(i)
            })
            setActiveChannels(active)
            setOfflineChannels(offline)
            console.log("Success: getFollows:", resp.data)
        }).catch(e => {
            console.log("Error: getFollows", e)
        })

        api.getRecommendations(user.access_token).then(resp => {
            setRecommendations(resp.data)
            console.log("Success: getRecommendations:", resp.data)
        }).catch(e => {
            console.log("Error: getRecommendations", e)
        })

        api.getRecords(user.access_token).then(resp => {
            setRecords(resp.data)
            console.log("Success: getRecords:", resp.data)
        }).catch(e => {
            console.log("Error: getRecords", e)
        })
    }, [isFocused])

    return (
        <Container>
            <YourActiveChannels channels={activeChannels}/>
            <RecommendedChannelsForYou recommendations={recommendations}/>
            <ContinueViewing records={records}/>
            <YourInactiveChannels channels={offlineChannels}/>
        </Container>
    );
};

const Container = styled.ScrollView`
  flex: 1;
  background: #0e0e10;
  padding: 0 16px;
`

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

export default Following;