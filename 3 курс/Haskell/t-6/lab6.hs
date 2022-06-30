-- Вводим фигуры
data BaseFigure = Circle Float Float Float 
   | Rectangle Float Float Float Float
   | Triangle Float Float Float Float Float Float deriving (Eq, Show, Read)

-- Сдвиг фигуры на заданную величину по x и y
setFigureMovement (Rectangle x1 y1 x2 y2) dx dy      = (Rectangle (x1+dx) (y1+dy) (x2+dx) (y2+dy))
setFigureMovement (Circle x y r) dx dy               = (Circle (x+dx) (y+dy) r)
setFigureMovement (Triangle x1 y1 x2 y2 x3 y3) dx dy = (Triangle (x1+dx) (y1+dy) (x2+dx) (y2+dy) (x3+dx) (y3+dy))

-- Поиск новых координат точки для поворота
xnew :: Float -> Float -> Float -> Float -> Float -> Float
xnew x y x0 y0 alpha = (x-x0)*cos(alpha) - (y-y0)*sin(alpha) + x0
ynew :: Float -> Float -> Float -> Float -> Float -> Float
ynew x y x0 y0 alpha = (x-x0)*sin(alpha) + (y-y0)*cos(alpha) + y0

-- Поиск центра фигуры
findRectangleCentre :: Float -> Float -> Float
findRectangleCentre x1 x2 = (x2-x1)/2 + x1
findTriangleCentre :: Float -> Float -> Float -> Float
findTriangleCentre x1 x2 x3 = (x1+x2+x3)/3

-- Поворот фигуры на угол alpha
setFigureRotate :: BaseFigure -> Float -> BaseFigure
setFigureRotate (Rectangle x1 y1 x2 y2) alpha = (Rectangle x1new y1new x2new y2new)
   where x1new = xnew x1 y1 (findRectangleCentre x1 x2) (findRectangleCentre y1 y2) alpha
         y1new = ynew x1 y1 (findRectangleCentre x1 x2) (findRectangleCentre y1 y2) alpha
         x2new = xnew x2 y2 (findRectangleCentre x1 x2) (findRectangleCentre y1 y2) alpha
         y2new = ynew x2 y2 (findRectangleCentre x1 x2) (findRectangleCentre y1 y2) alpha
setFigureRotate (Circle x y r) alpha = (Circle x y r)
setFigureRotate (Triangle x1 y1 x2 y2 x3 y3) alpha = (Triangle x1new y1new x2new y2new x3new y3new)
   where x1new = xnew x1 y1 (findTriangleCentre x1 x2 x3) (findTriangleCentre y1 y2 y3) alpha
         y1new = ynew x1 y1 (findTriangleCentre x1 x2 x3) (findTriangleCentre y1 y2 y3) alpha
         x2new = xnew x2 y2 (findTriangleCentre x1 x2 x3) (findTriangleCentre y1 y2 y3) alpha
         y2new = ynew x2 y2 (findTriangleCentre x1 x2 x3) (findTriangleCentre y1 y2 y3) alpha
         x3new = xnew x3 y3 (findTriangleCentre x1 x2 x3) (findTriangleCentre y1 y2 y3) alpha
         y3new = ynew x3 y3 (findTriangleCentre x1 x2 x3) (findTriangleCentre y1 y2 y3) alpha


--Main-метод
main :: IO ()
main = do

   let testCircle = Circle 2 3 5
   print("testCircle ",testCircle)
   let testTriangle = Triangle 1 1 4 4 9 9
   print("testTriangle ",testTriangle)
   let testRectangle = Rectangle 1 1 4 4
   print("testRectangle ",testRectangle)

   print("---- setFigureMovement ----")
   print(setFigureMovement testCircle 7 8)
   print(setFigureMovement testTriangle 3 1)
   print(setFigureMovement testRectangle 2 5)
   
   print("---- setFigureRotate ----")
   print(setFigureRotate testCircle 30)
   print(setFigureRotate testTriangle 60)
   print(setFigureRotate testRectangle 45)
