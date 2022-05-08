module Task4 where

import Data.Char (ord)

-- Ковалев А.И.
-- ПИ19-3
-- Вариант: 3-2)

-- Функции работы с бинарными деревьями поиска. Определите тип данных, представляющий бинарные деревья поиска.
-- В отличие от деревьев, представленных в методических указаниях, в деревьях поиска данные могут находиться
-- не только в листьях, но и в промежуточных узлах дерева. Будем использовать деревья для представления
-- ассоциативного массива, сопоставляющие значения ключей (представляемых как строки) целым числам.
-- Для каждого узла с некоторым ключом в левом поддереве должны содержаться элементы с меньшими значениями ключа,
-- а в правом — с большими. При поиске соответствия между строкой и числом необходимо учитывать эту информацию,
-- поскольку она позволяет более эффективно извлекать информацию из дерева.

-- Определите описанный тип данных и следующие функции:
--    1) add, добавляющую в дерево заданную пару ключа и значения.
--    2) find, возвращающую число, соответствующее заданной строке.
--    3) exists, проверяющую, что элемент с заданным ключом содержится в дереве.
--    4) toList, преобразующая заданное дерево поиска в список, упорядоченный по значениям ключей.

data BTree
  = Empty
  | Node (String, Integer) BTree BTree
  deriving (Show)

add :: BTree -> (String, Integer) -> BTree
add Empty kv = Node kv Empty Empty
add (Node x@(kx, _) l r) y@(ky, _)
  | ky < kx = Node x (add l y) r
  | otherwise = Node x l (add r y)

find :: BTree -> String -> Maybe Integer
find Empty _ = Nothing
find (Node (k, v) l r) i
  | k == i = Just v
  | i < k = find l i
  | otherwise = find r i

exists :: BTree -> String -> Bool
exists Empty _ = False
exists (Node (k, _) l r) i
  | k == i = True
  | i < k = exists l i
  | otherwise = exists r i

fromList :: [(String, Integer)] -> BTree
fromList [] = Empty
fromList xs = foldl add Empty xs

toList :: BTree -> [(String, Integer)]
toList Empty = []
toList (Node kv l r) = toList l ++ [kv] ++ toList r

------------------ Pretty-Format ------------------

indent :: [String] -> [String]
indent = map ("  " ++)

layout :: BTree -> [String]
layout Empty = []
layout (Node kv l r) = indent (layout r) ++ [show kv] ++ indent (layout l)

pformat :: BTree -> String
pformat = unlines . layout

------------------ Pretty-Format ------------------

nodes :: [Char] -> [(String, Integer)]
nodes chrs = [([ch, '_'] ++ show (ord ch), toInteger (ord ch)) | ch <- chrs]

tree :: BTree
tree =
  fromList
    ( nodes ['F']
        ++ nodes ['A', 'F' .. 'Q']
        ++ nodes ['C', 'E' .. 'G']
        ++ nodes ['Z', 'W' .. 'I']
        ++ nodes ['B' .. 'D']
    )

main :: IO ()
main = do
  putStrLn $ pformat tree
  putStrLn $ pformat (add tree ("H", 42))
  print $ find tree "P_80" -- Just 80
  print $ find tree "B_66" -- Just 66
  print $ find tree "Z_0" -- Nothing

--        ("Z_90",90)
--          ("W_87",87)
--            ("T_84",84)
--              ("Q_81",81)
--      ("P_80",80)
--        ("N_78",78)
--          ("K_75",75)
--    ("K_75",75)
--      ("G_71",71)
--  ("F_70",70)
--("F_70",70)
--      ("E_69",69)
--          ("D_68",68)
--        ("C_67",67)
--    ("C_67",67)
--      ("B_66",66)
--  ("A_65",65)
