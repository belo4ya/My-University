-- Ковалев Алексей
module Main where

import Data.Typeable

var :: [[[(Integer, Bool)]]]
var = [[[(123, True), (345, False)]]]

main :: IO ()
main = do
  print (typeOf var)
