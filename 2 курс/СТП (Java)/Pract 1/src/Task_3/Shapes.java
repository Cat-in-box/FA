package Task_3;

public abstract class Shapes {
    private int x;
    private int y;
    private int z;

    public Shapes(int x, int y, int z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }

    public abstract int getX();
    public abstract int getY();
    public abstract int getZ();

    public abstract double getArea(int height, int width, int length);
    public abstract double getPSerimeter(int height, int width, int length);
}
