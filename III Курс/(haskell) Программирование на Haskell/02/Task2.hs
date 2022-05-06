-- Вариант-9
module Task2 where

import Data.List (transpose)
import Data.Ratio ((%))

-- 1. Определите функцию, принимающую на вход целое число n и возвращающую список, содержащий n элементов, упорядоченных по возрастанию.
-- Список коэффициентов ряда Тэйлора для функции exp(x).
-- e^x = 1 + x / 1! + x^2 / 2! + x^3 / 3! + ... + x^n / n! + ...

-- неэффективно? Работает быстрее чем эффективаня реализация (см. ниже задание на вычисление списка факториалов)
taylorExp :: Integer -> [Rational]
taylorExp n
  | n < 1 = []
  | otherwise = 1 : [1 % product [1 .. m] | m <- [1 .. n - 1]]

taylorExp' :: Integer -> [Rational]
taylorExp' n
  | n < 1 = []
  | otherwise = map (1 %) f
  where
    f = scanl (*) 1 [1 .. n - 1]

-- 2. Определите следующие функции:
-- Функция makePositive, которая меняет знак всех отрицательных элементов списка чисел,
-- например: makePositive [-1, 0, 5, -10, -20] дает [1,0,5,10,20].
makePositive :: [Integer] -> [Integer]
makePositive = map abs

main :: IO ()
main = do
  let n = 10 :: Integer
  putStrLn ("Коэффициенты ряда Тэйлора для функции exp(x) (n=" ++ show n ++ ")")
  print (taylorExp n)
  let xs = [-1, 0, 5, -10, -20] :: [Integer]
  putStrLn ("\nmakePositive(" ++ show xs ++ ")")
  print (makePositive xs)

-- Дополнительно:
-- =====================================================================================================================
-- Список натуральных чисел.
nn :: Int -> [Int]
nn n = [1 .. n]

headNN :: Int -> [Int]
headNN n
  | n < 1 = []
  | n == 1 = [1]
  | otherwise = headNN (n - 1) ++ [n]

tailBackNN :: Int -> [Int]
tailBackNN n
  | n < 1 = []
  | otherwise = f n [n]
  where
    f 1 b = b
    f a b = f (a - 1) ((a - 1) : b)

--tailForwardNN :: Int -> [Int]
--tailForwardNN n
--  | n < 1 = []
--  | otherwise = f 1 [1]
--  where
--    f 10 b = b  -- TODO: n = 10
--    f a b = f (a + 1) (b ++ [a + 1])

tailForwardNN :: Int -> [Int]
tailForwardNN n
  | n < 1 = []
  | otherwise = f 1 [1]
  where
    f a b
      | a == n = b
      | otherwise = f (a + 1) (b ++ [a + 1])

-- Список нечетных натуральных чисел.
tailBackOddNN :: Int -> [Int]
tailBackOddNN n
  | n < 1 = []
  | otherwise = f n [n * 2 - 1]
  where
    f 1 b = b
    f a b = f (a - 1) ((head b - 2) : b)

-- Список четных натуральных чисел.
tailBackEvenNN :: Int -> [Int]
tailBackEvenNN n
  | n < 1 = []
  | otherwise = f n [n * 2]
  where
    f 1 b = b
    f a b = f (a - 1) ((head b - 2) : b)

-- Список квадратов натуральных чисел.
headSquaresNN :: Int -> [Int]
headSquaresNN n
  | n < 1 = []
  | otherwise = headSquaresNN (n - 1) ++ [n * n]

tailSquaresNN :: Int -> [Int]
tailSquaresNN n
  | n < 1 = []
  | otherwise = f n [n * n]
  where
    f 1 b = b
    f a b = f c ((c * c) : b)
      where
        c = a - 1

-- Список факториалов. (Big Research 🔎)
factorialList :: Integer -> [Integer]
factorialList 0 = [1]
factorialList n = [product [1 .. m] | m <- [1 .. n]]

factorialList' :: Integer -> [Integer]
factorialList' 0 = [1]
factorialList' n = scanl (*) 1 [1 .. n]

headFactorialList :: Integer -> [Integer]
headFactorialList n
  | n < 1 = []
  | otherwise = headFactorialList (n - 1) ++ [f n]
  where
    f 0 = 1
    f a = f (a - 1) * a

tailFactorialList :: Integer -> [Integer] -- TODO: почему это не быстрее чем headFactorialList?
tailFactorialList n
  | n < 1 = []
  | otherwise = f 1 1 [1]
  where
    f a b c
      | a == n = c
      | otherwise = f x y (c ++ [y])
      where
        x = a + 1
        y = b * x

tailBackFactorialList :: Integer -> [Integer]
tailBackFactorialList n
  | n < 1 = []
  | otherwise = f n [product [1 .. n]]
  where
    f 1 b = b
    f a b = f (a - 1) ((head b `div` a) : b)

-- Список степеней двойки. (захватил 0-ю степень 2-ки для разнообразия)
appendBitPow :: Integer -> [Integer]
appendBitPow n
  | n < 1 = []
  | otherwise = f 1 [1]
  where
    f a b
      | a == n = b
      | otherwise = f (a + 1) (b ++ [last b * 2])

prependBitPow :: Integer -> [Integer]
prependBitPow n
  | n < 1 = []
  | otherwise = f n [2 ^ (n - 1)]
  where
    f 1 b = b
    f a b = f (a - 1) ((head b `div` 2) : b)

-- Список биномиальных коэффициентов.
binomial :: Integer -> Integer -> Integer
binomial 0 _ = 0
binomial _ 0 = 0
binomial _ 1 = 1
binomial n k = binomial (n - 1) k + binomial (n - 1) (k - 1)

binomialList :: Integer -> [Integer]
binomialList n = [binomial n k | k <- [1 .. n]]

-- Функция, принимающая на входе список вещественных чисел и вычисляющую их арифметическое среднее.
-- Постарайтесь, чтобы функция осуществляла только один проход по списку.
average :: Fractional t => [t] -> t
average = f 0 0
  where
    f s n [] = s / n
    f s n (x : xs) = f (s + x) (n + 1) xs

-- Функция вычленения n-го элемента из заданного списка.
getItem :: [a] -> Int -> a
getItem xs n = xs !! (n - 1)

-- Функция сложения элементов двух списков.
-- Возвращает список, составленный из сумм элементов списков-параметров.
-- Учесть, что переданные списки могут быть разной длины.
sumZip :: Num b => [b] -> [b] -> [b]
sumZip as bs = map sum (transpose [as, bs])

-- Функция removeOdd, которая удаляет из заданного списка целых чисел все нечетные числа.
-- Например: removeOdd [1,4,5,6,10] должен возвращать [4,10].
removeOdd :: [Integer] -> [Integer]
removeOdd = filter even

-- Функция removeEmpty, которая удаляет пустые строки из заданного списка строк.
-- Например: removeEmpty ["", "Hello", "", "", "World!"] возвращает ["Hello","World!"].
removeEmpty :: [[Char]] -> [[Char]]
removeEmpty xs = [x | x <- xs, x /= ""]

removeEmpty' :: [[Char]] -> [[Char]]
removeEmpty' = filter (/= "")

-- Функция countTrue :: [Bool] -> Integer, возвращающая количество элементов списка, равных True.
countTrue :: [Bool] -> Integer
countTrue = foldl f 0
  where
    f s True = s + 1
    f s False = s

-- Функция delete :: Char -> String -> String, которая принимает на вход строку и символ и возвращает строку, в которой удалены все вхождения символа.
-- Пример: delete ’l’ "Hello world!" должно возвращать "Heo word!".
delete :: Char -> String -> String
delete ch s = [x | x <- s, x /= ch]

-- Функция substitute :: Char -> Char -> String -> String, которая заменяет в строке указанный символ на заданный.
-- Пример: substitute ’e’ ’i’ "eigenvalue" возвращает "iiginvalui"
substitute :: Char -> Char -> String -> String
substitute p r s = [if x == p then r else x | x <- s]

substitute' :: Char -> Char -> String -> String
substitute' p r = map (\ch -> if ch == p then r else ch)
