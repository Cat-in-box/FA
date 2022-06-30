import Data.List

-- ЗАДАНИЕ 2. Определите следующие функции.
-- 8) Функция countTrue :: [Bool] -> Integer, возвращающая количество элементов списка, равных True.
countTrue :: [Bool] -> Integer
countTrue []            =  0
countTrue (True  : xs)  =  1 + countTrue xs
countTrue (False : xs)  =  countTrue xs

-- 2) Функция вычленения n-го элемента из заданного списка.
searchN :: ([a], Int) -> a
searchN (l, n) = l!!n