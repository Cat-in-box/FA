-- 21. Построить список из элементов исходного списка, находящихся на позициях 3, 6, 9 и т.д.

f [] = [] -- если остался пустой список, 1 или 2 элемента - убираем их
f (x:[]) = []
f (x:y:[]) = []
f x = [x!!2] ++ f (drop 3 x) -- иначе берем 3й и удаляем тройку


main :: IO ()
main = do
    let list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    let list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    let list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12]

    print(f list1)
    print(f list2)
    print(f list3)