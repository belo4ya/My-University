-- Вариант-9
module Task2 where

-- 1. Определите функцию, принимающую на вход целое число n и возвращающую список, содержащий n элементов, упорядоченных по возрастанию.
-- Список коэффициентов ряда Тэйлора для функции exp(x).
-- e^x = 1 + x / 1! + x^2 / 2! + x^3 / 3! + ... + x^n / n! + ...
import Data.Ratio ((%))

taylorExp :: Integer -> [Rational]
taylorExp n
  | n < 1 = []
  | otherwise = 1 : [1 % product [1 .. m] | m <- [1 .. n - 1]]

-- 2. Определите следующие функции:
-- Функция makePositive, которая меняет знак всех отрицательных элементов списка чисел,
-- например: makePositive [-1, 0, 5, -10, -20] дает [1,0,5,10,20].
makePositive :: Num b => [b] -> [b]
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
