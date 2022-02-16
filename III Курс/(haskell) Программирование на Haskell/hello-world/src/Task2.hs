-- Вариант-9
module Task2 where

-- 1. Определите функцию, принимающую на вход целое число n и возвращающую список, содержащий n элементов, упорядоченных по возрастанию.
-- Список коэффициентов ряда Тэйлора для функции exp(x)

-- Дополнительно:
-- Список натуральных чисел.
nn :: Int -> [Int]
nn n = [1 .. n]

headNN :: Int -> [Int]
headNN n
  | n < 1 = []
  | n == 1 = [1]
  | otherwise = headNN (n - 1) ++ [n]

tailNN :: Int -> [Int]
tailNN n
  | n < 1 = []
  | otherwise = tailNN' n [n]
  where
    tailNN' 1 b = b
    tailNN' a b = tailNN' (a - 1) ((a - 1) : b)

--tailNN_ :: Int -> [Int]
--tailNN_ n
--  | n < 1 = []
--  | otherwise = tailNN' 1 [1]
--  where
--    tailNN' 10 b = b  -- TODO: n = 10
--    tailNN' a b = tailNN' (a + 1) (b ++ [a + 1])

tailNN_ :: Int -> [Int]
tailNN_ n
  | n < 1 = []
  | otherwise = tailNN' 1 [1]
  where
    tailNN' a b
      | a == n = b
      | otherwise = tailNN' (a + 1) (b ++ [a + 1])

-- Список нечетных натуральных чисел.

-- Список четных натуральных чисел.

-- Список квадратов натуральных чисел.

-- Список факториалов.

-- Список степеней двойки.

-- Список треугольных чисел 3.

-- Список пирамидальных чисел 4.

-- Список биномиальных коэффициентов.
