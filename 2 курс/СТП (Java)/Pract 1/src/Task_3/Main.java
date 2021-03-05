package Task_3;

import java.util.Scanner;

public class Main {
    public static void main(String [] args) {

        Scanner scanner = new Scanner(System.in);
        System.out.println("Введите длину квадрата");
        int length = scanner.nextInt();
        System.out.println("length = " + length);
        Square square1 = new Square(1, 2, 3);
        System.out.println("Площадь квадрата = " + square1.getArea(length, 2, 2));

        Shapes shape1 = new Square(1, 2, 3);
        System.out.println("x = " + ((Shapes)square1).getX());

        System.out.println("Введите длину квадрата");
        System.out.println("length = " + length);
        Triangle triangle1 = new Triangle(1, 2, 3);
        System.out.println("Периметр треугольника = " + triangle1.getPSerimeter(4, 2, 2));
    }
}
