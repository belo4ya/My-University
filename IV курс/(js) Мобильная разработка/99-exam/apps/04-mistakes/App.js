import React from 'react'
import { View } from 'react-native'
import { COLORS } from './src/constants'
import Header from './src/components/Header'
import Categories from './src/components/Categories'
import Popular from './src/components/Popular'

export default function App() {
  return (
    <View
      style={{
        padding: 24,
        paddingTop: 55,
        paddingBottom: 75,
        backgroundColor: COLORS.black,
      }}>
      <Header />
      <Categories />
      <Popular />
    </View>
  )
}
