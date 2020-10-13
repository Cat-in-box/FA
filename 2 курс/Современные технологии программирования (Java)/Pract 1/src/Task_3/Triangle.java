package Task_3;

public class Triangle extends Shapes implements Figures{

    public Triangle(int x, int y, int z) {
        super(x, y, z);
    }

    public int getX() {
        return 0;
    }

    public int getY() {
        return 0;
    }

    public int getZ() {
        return 0;
    }

    public double getArea(int height, int width, int length) {
        return 0;
    }

    public double getPSerimeter(int height, int width, int length) {
        return height + width + length;
    }
}
