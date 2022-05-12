-- Вариант-9
module Task1 where

-- 1. Приведите пример нетривиальных выражений, принадлежащих следующему типу:
-- [([Bool], [Double])]
var :: [([Bool], [Double])]
var = [([True, False, False], [2, 2.3, -0.22, 2 / 3]), ([False, True, False], [0.1, 0.2 + 0.3 + 0.1])]

-- 2. Определите следующие функции:
-- Функция isTriangle, определяющая, можно ли из отрезков с заданными длинами x, y и z построить треугольник.
sumGt :: (Ord a, Num a) => a -> a -> a -> Bool
sumGt a b c = a + b > c

isTriangle :: (Ord a, Num a) => a -> a -> a -> Bool
isTriangle x y z = sumGt x y z && sumGt z x y && sumGt y z x

-- Дополнительно:
-- Функция max3, по трем целым возвращающая наибольшее из них.
max3 :: Integer -> Integer -> Integer -> Integer
max3 a b c = max a (max b c)

-- Функция min3, по трем целым возвращающая наименьшее из них.
min3 :: Integer -> Integer -> Integer -> Integer
min3 a b c = min a (min b c)

-- Функция sort2, по двум целым возвращающая пару, в которой наименьшее из них стоит на первом месте, а наибольшее — на втором.
sort2 :: Integer -> Integer -> (Integer, Integer)
sort2 a b = if a > b then (b, a) else (a, b)

-- Функция bothTrue :: Bool -> Bool -> Bool, которая возвращает True тогда и только тогда, когда оба ее аргумента будут равны True.
-- Не используйте при определении функции стандартные логический операции (&&, || и т.п.).
bothTrue :: Bool -> Bool -> Bool
bothTrue a b
  | not a = False
  | not b = False
  | otherwise = True

otherwiseBothTrue :: Bool -> Bool -> Bool
otherwiseBothTrue True True = True
otherwiseBothTrue _ _ = False

-- Функция solve2::Double->Double->(Bool,Double), которая по двум числам, представляющим собой коэффициенты линейного уравнения ax + b = 0,
-- возвращает пару, первый элемент которой равен True, если решение существует и False в противном случае; при этом второй элемент равен либо значению корня, либо 0.0.
solve2 :: Double -> Double -> (Bool, Double)
solve2 0 0 = (True, 0)
solve2 0 _ = (False, 0)
solve2 a b = (True, - b / a)

-- Функция isParallel, возвращающая True, если два отрезка, концы которых задаются в аргументах функции, параллельны (или лежат на одной прямой).
-- Например, значение выражения isParallel (1,1) (2,2) (2,0) (4,2) должно быть равно True, поскольку отрезки (1,1) − (2,2) и (2,0) − (4,2) параллельны.
isParallel :: (Eq a, Num a) => (a, a) -> (a, a) -> (a, a) -> (a, a) -> Bool
isParallel (x0, y0) (x1, y1) (x2, y2) (x3, y3) = (y1 - y0) * (x3 - x2) == (x1 - x0) * (y3 - y2)

-- Функция isIncluded, аргументами которой служат параметры двух окружностей на плоскости (координаты центров и радиусы);
-- функция возвращает True, если вторая окружность целиком содержится внутри первой.
distance :: Floating a => (a, a) -> (a, a) -> a
distance (x0, y0) (x1, y1) = sqrt (((x1 - x0) ** 2) + ((y1 - y0) ** 2))

isIncluded :: (Ord a, Floating a) => (a, a, a) -> (a, a, a) -> Bool
isIncluded (x0, y0, r0) (x1, y1, r1) = r0 - r1 >= distance (x0, y0) (x1, y1)

-- Функция isRectangular, принимающая в качестве параметров координаты трех точек на плоскости, и возвращающая True,
-- если образуемый ими треугольник — прямоугольный.
-- a + b == c || c + a == b || b + c == a
(~=) :: (Ord t, Floating t) => t -> t -> Bool
(~=) a b = abs (a - b) < 1e-12

infix 4 ~=

isRectangular :: (Ord c, Floating c) => (c, c) -> (c, c) -> (c, c) -> Bool
isRectangular (x0, y0) (x1, y1) (x2, y2) = a + b ~= c || c + a ~= b || b + c ~= a
  where
    a = distance (x0, y0) (x1, y1) ** 2
    b = distance (x2, y2) (x0, y0) ** 2
    c = distance (x1, y1) (x2, y2) ** 2

-- Функция isSorted, принимающая на вход три числа и возвращающая True, если они упорядочены по возрастанию или по убыванию.
isSorted :: (Ord a, Num a) => a -> a -> a -> Bool
isSorted a b c = s0 == 0 || s1 == 0 || s0 == s1
  where
    s0 = signum (a - b)
    s1 = signum (b - c)
