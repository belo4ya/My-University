module Task6 where

-- Ковалев А.И.
-- ПИ19-3
-- использование функций свертки для проверки сходимости ряда Тейлора к экспоненте

import Data.Ratio ((%))

taylorExp :: Integer -> [Rational]
taylorExp n
  | n < 1 = []
  | otherwise = map (1 %) f
  where
    f = scanl (*) 1 [1 .. n - 1]

cumSum :: Num a => [a] -> [a]
cumSum = scanl (+) 0

main :: IO ()
main = do
  let expKs = taylorExp 10
  -- [1 % 1,1 % 1,1 % 2,1 % 6,1 % 24,1 % 120,1 % 720,1 % 5040,1 % 40320,1 % 362880]
  print expKs
  -- [0.0,1.0,2.0,2.5,2.6666666666666665,2.7083333333333335,2.716666666666667,
  -- 2.7180555555555554,2.7182539682539684,2.71827876984127,2.7182815255731922]
  print (map fromRational . cumSum $ expKs :: [Double])
