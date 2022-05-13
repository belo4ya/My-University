module Task9 where

-- Ковалев А.И.
-- ПИ19-3
-- Вариант 8

-- Найти номер элемента списка, имеющего максимальное значение.

argmax :: (Ord a, Num a, Enum a) => [a] -> a
argmax [] = -1
argmax xs = snd $ foldr (\(x, y) acc -> if x == z then (x, y) else acc) (0, head xs) (zip xs [0 ..])
  where
    z = maximum xs

main :: IO ()
main = do
  print $ argmax ([1 .. 10] :: [Integer]) -- 9
  print $ argmax ([1, 4, 2, 3]::[Integer]) -- 1
  print $ argmax ([5, 3, 1]::[Integer]) -- 0
  print $ argmax ([0]::[Integer]) -- 0
  print $ argmax ([]::[Integer]) -- -1
