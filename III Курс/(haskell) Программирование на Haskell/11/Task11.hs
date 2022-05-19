module Task11 where

-- Ковалев А.И.
-- ПИ19-3
-- Вариант 5

-- Построить список из разностей 1-го и 2-го элементов, 3-го и 4-го и т.д.

seqDiff :: [Integer] -> [Integer]
seqDiff xs = zipWith (-) (onEven xs) (onOdd xs)
  where
    onEven :: [a] -> [a]
    onEven = on [False, True]

    onOdd :: [a] -> [a]
    onOdd = on [True, False]

    on :: [Bool] -> [a] -> [a]
    on cond = foldr (\(c, x) -> if c then (x :) else id) [] . zip (cycle cond)

main :: IO ()
main = do
  print $ seqDiff [1, 4, 5, 6, 8, 18] -- [3,1,10]
  print $ seqDiff [1 .. 9] -- [1,1,1,1]
  print $ seqDiff [1 .. 10] -- [1,1,1,1,1]
  print $ seqDiff [2, 4 .. 10] -- [2,2]
  print $ seqDiff [1] -- []
  print $ seqDiff [] -- []
  print $ take 6 (seqDiff [0, 3 ..]) -- [3,3,3,3,3,3]
