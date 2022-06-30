-- 7. Вставить элемент в список на заданное место.

splitList i xs = [take (i-1) xs, drop (i-1) xs]

mergeLists spl n = spl!!0 ++ [n] ++ spl!!1

addToList n i list = mergeLists (splitList i list) n


-- 31. Выделить из списка элементы на четных позициях

f [] = []
f (x:[]) = []
f x = [x!!1] ++ f (drop 2 x)

main :: IO ()
main = do
    let list = [1, 2, 3, 4, 5]
    print (list)

    let n = 10
    let i = 2

    print (addToList n i list)
    print (f list)