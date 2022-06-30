-- Задание. Определите следующие функции с использованием функций высшего порядка:
-- 3) Функция countEven, возвращающая количество нечетных элементов в списке.

countEven items = length (filter odd items)

main :: IO ()
main = do
    let list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(countEven list1)