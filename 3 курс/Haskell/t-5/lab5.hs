-- ЗАДАНИЕ 2. Функции для работы с типом List. Для введенного ранее типа List определите следующие функции:
-- 3) removeNegative, которая из списка целых (тип List Integer) удаляет отрицательные элементы.

data List a = Nil | Cons a (List a) deriving Show

headList (Cons x _) = x
headList Nil = error "headList: empty list"
 
tailList (Cons _ y) = y
tailList Nil = error "tailList: empty list"

removeNegative Nil = Nil
removeNegative (Cons x y) | (x < 0) = tailList (Cons x y)
                          | otherwise = (Cons x (removeNegative y))

-- ЗАДАНИЕ 8. Иерархия должностей в некоторой организации образует древовидную структуру.
-- Каждый работник, однозначно характеризующийся уникальным именем, имеет несколько подчиненных.
-- Определите тип данных, представляющий такую иерархию и опишите следующие функции:
-- 1) getSubordinate, возвращающую список подчиненных указанного работника.

data Person = PersonName (String) [Person] deriving (Eq, Show)

getName (PersonName n _) = n

getNames = map getName

getSubordinatePersons (PersonName _ p) = p

finder ((PersonName n p) :xs) name | (n == name) = getSubordinatePersons (PersonName n p)
                                   | otherwise = finder xs name

getSubordinate (PersonName n p) name = getNames (finder [(PersonName n p)] name)