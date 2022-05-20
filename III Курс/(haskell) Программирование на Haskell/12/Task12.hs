{-# LANGUAGE TemplateHaskell, TemplateHaskellQuotes #-}

module Task12 where

-- Ковалев А.И.
-- ПИ19-3
-- Вариант 4a

-- Удалить из программы комментарии:
-- на Haskell (расширение *.hs), комментарии - "--"
-- имя файла передается - параметром функции

{-
putStrLn "putStrLn \"Строчные комментарии в haskell пишутся так: -- inline comment example\""
-}

import Data.List (isPrefixOf)
import Language.Haskell.Exts

fileExt :: [Char]
fileExt = "hs"

commentPrefix :: [Char]
commentPrefix = "--"

-- Получение типа типа-разрешения файла
getExt :: (Char -> Bool) -> [Char] -> [[Char]]
getExt p s = case dropWhile p s of
  "" -> []
  s' -> w : getExt p s''
    where
      (w, s'') = break p s'

-- Проверка на корректный тип файла
commentCleaner :: [Char] -> IO ()
commentCleaner file_name =
  if last (getExt (== '.') file_name) == fileExt
    then dataReader file_name
    else print ("Not ." ++ fileExt ++ " file")

-- Чтение данных из файла
dataReader :: FilePath -> IO ()
dataReader path = do
  contents <- readFile path
  let buff = dataCommentRemover (lines contents)
  print "Comments was deleted"
  writeFile ("clear_" ++ path) (unlines buff)

-- Удаление комментария из строки
dataCommentRemover :: [[Char]] -> [[Char]]
dataCommentRemover [] = []
dataCommentRemover (l : ls)
  | commentPrefix `isPrefixOf` l = ls
  | otherwise = l : dataCommentRemover ls

main :: IO ()
main = do
  print "123"
  let testCase = "putStrLn \"Строчные комментарии в haskell пишутся так: -- inline comment example\""
  print "123"
  print (parseFileContentsWithComments (defaultParseMode {parseFilename = "WithComments.hs"}) "line 1\nline 2")

--  commentCleaner "WithComments.hs"
