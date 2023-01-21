import { Text, TouchableHighlight, View } from "react-native";

// если это код действительно незавершенный и это подлый вопрос, то
// на экране будет белый текст об ошибке на красном фоне/черном фоне

// если код рабочий, то на экране будет плитка из серых карточек с категориями
// 3 карточки в ряду, т.к. у TouchableHighlight onPress не определен, цвет карточек
// при клике меняться не будет

const categories = [
  {title: "Title 1"},
  {title: "Title 2"},
  {title: "Title 3"},
  {title: "Title 4"},
  {title: "Title 5"},
  {title: "Title 6"},
]

export default function App() {
  return (
    <View
      style={{
        marginTop: 30,
        flexDirection: 'row',
        flexWrap: 'wrap',
        justifyContent: 'space-between',
      }}>
      {categories.map((cat, idx) => (
        <View
          key={`categories ${idx}`}
          style={{
            width: '30%',
            marginBottom: 20,
          }}>
          <TouchableHighlight
            key={`categories ${idx}`}
            underlayColor={COLORS.secondary}
            style={{
              height: 100,
              justifyContent: 'center',
              borderRadius: SIZES.radius,
              paddingLeft: 5,
              paddingRight: 5,
              backgroundColor: COLORS.gray,
            }}>
            <Text>{cat.title}</Text>
          </TouchableHighlight>
        </View>
      ))}
    </View>
  )
}

const SIZES = {
  radius: 8,
}

const COLORS = {
  secondary: "#fcff84",
  gray: "#7a7a7a",
}
