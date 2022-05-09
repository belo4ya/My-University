module Task5 where

-- Ковалев А.И.
-- ПИ19-3
-- Доп. задание: 8

-- Иерархия должностей в некоторой организации образует древовидную структуру.
-- Каждый работник, однозначно характеризующийся уникальным именем, имеет несколько подчиненных.
-- Определите тип данных, представляющий такую иерархию и опишите следующие функции:
--    getSubordinate, возвращающую список подчиненных указанного работника.
--    getAllSubordinate, возвращающую список всех подчиненных данного работника, включая косвенных.
--    getBoss, возвращающую начальника указанного работника.
--    getList, возвращающую список пар, первым элементом которых является имя работника,
--    а вторым — количество его подчиненных (включая косвенных).

data Employee = Null | Employee String Employee

instance Show Employee where
  show Null = "Null"
  show (Employee x _) = x

getSubordinate :: [Employee] -> String -> [Employee]
getSubordinate xs name = filter f xs
  where
    f Null = False
    f (Employee _ Null) = False
    f (Employee _ (Employee boss _)) = boss == name

getNames :: [Employee] -> [String]
getNames [] = []
getNames [Null] = []
getNames (Null : _ : _) = []
getNames (Employee name _ : xs) = name : getNames xs

getAllSubordinate :: [Employee] -> String -> [Employee]
getAllSubordinate xs name = subs ++ f xs (getNames subs)
  where
    f ys names = concat [getAllSubordinate ys x | x <- names]
    subs = getSubordinate xs name

getBoss :: [Employee] -> String -> Employee
getBoss [] _ = Null
getBoss [Null] _ = Null
getBoss (Null : _ : _) _ = Null
getBoss ((Employee x boss) : xs) name
  | x == name = boss
  | otherwise = getBoss xs name

director :: Employee
director = Employee "Director" Null

senior1 :: Employee
senior1 = Employee "Senior_1" director

middle1 :: Employee
middle1 = Employee "Middle_1" senior1

junior1 :: Employee
junior1 = Employee "Junior_1" middle1

junior2 :: Employee
junior2 = Employee "Junior_2" middle1

junior3 :: Employee
junior3 = Employee "Junior_3" middle1

middle2 :: Employee
middle2 = Employee "Middle_2" senior1

junior4 :: Employee
junior4 = Employee "Junior_4" middle2

junior5 :: Employee
junior5 = Employee "Junior_5" middle2

senior2 :: Employee
senior2 = Employee "Senior_2" director

middle3 :: Employee
middle3 = Employee "Middle_3" senior2

middle4 :: Employee
middle4 = Employee "Middle_4" senior2

senior3 :: Employee
senior3 = Employee "Senior_3" director

middle5 :: Employee
middle5 = Employee "Middle_5" senior3

middle6 :: Employee
middle6 = Employee "Middle_6" senior3

middle7 :: Employee
middle7 = Employee "Middle_7" senior3

company :: [Employee]
company =
  [ director,
    senior1,
    senior2,
    senior3,
    middle1,
    middle2,
    middle3,
    middle4,
    middle5,
    middle6,
    middle7,
    junior1,
    junior2,
    junior3,
    junior4,
    junior5
  ]

main :: IO ()
main = do
  print $ getSubordinate company "Senior_1" -- [Middle_1,Middle_2]
  print $ getSubordinate company "Middle_2" -- [Junior_4,Junior_5]
  print $ getAllSubordinate company "Senior_1" -- [Middle_1,Middle_2,Junior_1,Junior_2,Junior_3,Junior_4,Junior_5]
  print $ getAllSubordinate company "Senior_2" -- [Middle_3,Middle_4]
  print $ getBoss company "Middle_5" -- Senior_3
  print $ getBoss company "Director" -- Null
