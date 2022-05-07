-- Ковалев А.И.
-- ПИ19-3
-- Вариант-7

-- Определим следующий набор операций над строками:
-- Очистка: удаление всех символов из строки
-- Удаление: удаление всех вхождений указанного символа
-- Замена: замена всех вхождений одного символа на другой
-- Добавление: добавление в начало строки указанного символа
-- Разработайте тип данных, характеризующий операции над строками. Определите следующие функции:
--    - process, получающая в качестве аргумента действие и строку и возвращающая строку,
--      модифицированную в соответствие с указанным действием.
--    - processAll, аналогичная предыдущей, но получающая список действий и выполняющая их по порядку.
--    - deleteAll, принимающая две строки и удаляющей из второй строки все символы первой.
--      При реализации обязательно использовать функцию processAll.

module Task3 where

import Data.Char (isAlphaNum)

data StrOp
  = Clr -- Очистка: удаление всех символов из строки
  | Rmv Char -- Удаление: удаление всех вхождений указанного символа
  | Sub Char Char -- Замена: замена всех вхождений одного символа на другой
  | Append Char -- Добавление: добавление в начало строки указанного символа
  deriving (Show)

process :: StrOp -> String -> String
process Clr s = filter isAlphaNum s
process (Rmv ch) s = filter (/= ch) s
process (Sub rep ch) s = map (\x -> if x == rep then ch else x) s
process (Append ch) s = ch : s

processAll :: [StrOp] -> String -> String
processAll xs s = foldl (flip process) s xs

deleteAll :: String -> String -> String
deleteAll s1 = processAll (map Rmv s1)

main :: IO ()
main = do
  let s = "Hello, world!"
  print $ process Clr s -- "Helloworld"
  print $ process (Rmv 'o') s -- "Hell, wrld!"
  print $ process (Sub 'H' 'h') s -- "hello, world!"
  print $ process (Append '!') s -- "!Hello, world!"
  print $ processAll [Clr, Rmv 'o', Sub 'H' 'h', Append '!'] s -- "!hellwrld"
  print $ deleteAll "abcde" s -- "Hllo, worl!"
