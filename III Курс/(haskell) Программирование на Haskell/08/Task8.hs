module Task8 where

import System.Exit
import Task4

-- | Задание. Добавить в свою программы задания t-5 возможности ввода исходных данных из файлов,
-- | а также сохранение результата в файл. (база 7 баллов)
-- | Дополнительно (2-5 баллов):
-- | - ввод параметров с консоли
-- | - вывод (промежуточных, итоговых) данных на консоль
-- | - ввод имени входного (выходного) файла с консоли
-- | - выбор ветвления
-- | - повторный вызов исходных данных или завершение
newtype Config = Config {_path :: String}

mainLoop :: IO ()
mainLoop = do
  mainLoop' Config {_path = ""}

mainLoop' :: Config -> IO ()
mainLoop' conf = do
  mainMenu
  x <- getCMD
  procMainCMD x
  where
    getCMD :: IO String
    getCMD = do
      putStr ">>> "
      getLine

    mainMenu :: IO ()
    mainMenu = do
      let label = case _path conf of
            "" -> "stdout"
            path -> path
      putStrLn "1. Создать дерево (stdin)"
      putStrLn "2. Создать дерево (file)"
      putStrLn ("3. Настройки" ++ " (" ++ label ++ ")")
      putStrLn "4. Выход"

    procMainCMD :: String -> IO ()
    procMainCMD cmd = do
      case cmd of
        "1" -> procStdTree
        "2" -> procFileTree
        "3" -> procConf
        "4" -> exitSuccess
        _ -> mainLoop' conf
      where
        procStdTree :: IO ()
        procStdTree = do
          let tree = Empty
          putStrLn "Введите элементы дерева, каждый на новой строке. Чтобы завершить ввод введите пустую строку:"
          el' <- getCMD
          let el = read el' :: (String, Integer)
          putStrLn (pformat (add (add (add tree el) el) el))

        procFileTree :: IO ()
        procFileTree = do
          undefined

        procConf :: IO ()
        procConf = do
          confMenu
          x <- getCMD
          procConfCMD x
          where
            confMenu :: IO ()
            confMenu = do
              putStrLn "1. Режим вывода (stdout, file)"
              putStrLn "2. Назад"

            procConfCMD :: String -> IO ()
            procConfCMD cmd = do
              case cmd of
                "1" -> procConfInputMode
                "2" -> mainLoop' conf
                _ -> procConf
              where
                procConfInputMode :: IO ()
                procConfInputMode = do
                  putStrLn "Введите имя файла для сохранения результатов (оставьте пустым для использование stdout)"
                  path <- getCMD
                  mainLoop' Config {_path = path}

main :: IO ()
main = do
  putStrLn $ pformat tree
  putStrLn $ pformat (add tree ("H", 42))
  print $ find tree "P_80" -- Just 80
  print $ find tree "B_66" -- Just 66
  print $ find tree "Z_0" -- Nothing
  mainLoop
