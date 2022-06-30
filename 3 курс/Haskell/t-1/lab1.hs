import Data.List

-- ЗАДАНИЕ 1. Приведите пример нетривиальных выражений, принадлежащих следующему типу:
-- 8) (Bool,([Bool],[Integer]))
t1 = (True,([False, False],[4, 8, 6]))
-- ghci> :t t1
-- t1 :: (Bool, ([Bool], [Integer]))

-- ЗАДАНИЕ 2. Определите следующие функции:
-- 8) Функция isRectangular, принимающая в качестве параметров координаты трех точек на плоскости,
--    и возвращающая True, если образуемый ими треугольник — прямоугольный.
isRectangular :: (Num n, Eq n, Ord n) => (n, n) -> (n, n) -> (n, n) -> Bool
isRectangular a b c = rightTriangleTuple!!2 == rightTriangleTuple!!0 + rightTriangleTuple!!1
    where rightTriangleTuple = rightTriangle a b c --переменная для хранения подсчитанных значений квадратов длины сторон

--функция для подстчета квадрата расстояния между парами точек (т. е. длины сторон треугольника) и их сортировки по возрастанию
rightTriangle :: (Num n, Ord n) => (n, n) -> (n, n) -> (n, n) -> [n]
rightTriangle a b c = sort [(fst(a)-fst(b))^2 + (snd(a)-snd(b))^2, (fst(a)-fst(c))^2 + (snd(a)-snd(c))^2, (fst(b)-fst(c))^2 + (snd(b)-snd(c))^2]