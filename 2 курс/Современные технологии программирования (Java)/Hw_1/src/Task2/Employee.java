package Task2;

public abstract class Employee {

    private int ID;
    private String name;
    private float averageMonthlySalary;

    public Employee(int ID, String name) {
        this.ID = ID;
        this.name = name;
    }

    abstract void setAverageMonthlySalary(float Value);

}
