module Task10 where

import Control.Exception

-- Ковалев А.И.
-- ПИ19-3
-- Вариант 17

-- Построить список из трех списков одинаковой длины из сумм элементов

sumList3 :: [Integer] -> [Integer] -> [Integer] -> [Integer]
sumList3 = validateLength $ zipWith3 (\a b c -> a + b + c)

validateLength :: (Foldable t1, Foldable t2, Foldable t3) => (t1 a1 -> t2 a2 -> t3 a3 -> t4) -> t1 a1 -> t2 a2 -> t3 a3 -> t4
validateLength f xs ys zs
  | length xs == length ys && length xs == length zs = f xs ys zs
  | otherwise = error "the length should be the same"

exHandler :: SomeException -> IO ()
exHandler ex = putStrLn $ "Caught exception: " ++ (head . lines) (show ex)

main :: IO ()
main = do
  print $ sumList3 [1, 2, 3] [4, 5, 6] [7, 8, 9] -- [12,15,18]
  print $ sumList3 [1 .. 10] [2, 4 .. 20] [3, 6 .. 30] -- [6,12,18,24,30,36,42,48,54,60]
  print $ sumList3 [] [] [] -- []
  let ex1 = sumList3 [1, 2, 3] [1, 2] [1] -- Exception: the length should be the same
  let ex2 = sumList3 [1, 2, 3] [] [] -- Exception: the length should be the same
  catch (print ex1) exHandler
  catch (print ex2) exHandler
