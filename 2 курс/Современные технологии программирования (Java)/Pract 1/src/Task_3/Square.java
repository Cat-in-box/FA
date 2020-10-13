package Task_3;

public class Square extends Shapes {
    private int height;
    private int width;
    private int length;
    public Square(int x, int y, int z) {
        super(x, y, z);
    }

    @Override
    public int getX() {
        return 0;
    }

    @Override
    public int getY() {
        return 0;
    }

    @Override
    public int getZ() {
        return 0;
    }

    @Override
    public double getArea(int height, int width, int length) {
        return 0;
    }

    @Override
    public double getPSerimeter(int height, int width, int length) {
        return 0;
    }
}
