import Data.List

-- ЗАДАНИЕ 1. Определите функцию, принимающую на вход целое число n и возвращающую список, содержащий n элементов, упорядоченных по возрастанию.
-- 8) Список пирамидальных чисел 4.
squareList :: (Fractional a, Ord a) => a -> [a]
squareList (n) = if n<0 then [] else squareList(n-1) ++ [(2*n^3 + 3*n^2 + n)/6]

-- 1) Список натуральных чисел.
natureList :: Int -> [Int]
natureList (n) = if n<0 then [] else natureList(n-1) ++ [n]