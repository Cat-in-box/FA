--Удалить из программы комментарии. Для исходного файла проверяется расширение (если расширение не соответствует, ничего не делать)
--3) на С++ (расширение *.сpp), комментарии // …
--b) имя файла передается вводом с консоли

checkType (x:xs) = if xs == ".cpp" then True else checkType xs

commFinder (x:xs) = if (x == "/") && ((head xs) == "/")
                    then commRemover (x:xs)
                    else commFinder xs

commRemover (x:xs) = if (x == "\n") 
                     then xs
                     else commRemover xs


main = do
    let path = "hello_world.cpp"
    content <- readFile path
    print (commFinder content)
