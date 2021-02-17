package Task2;

public class FixedEmployee extends Employee {
    private int fixedPayment;

    public FixedEmployee(int ID, String name, int FixedPayment) {
        super(ID, name);
        this.fixedPayment = FixedPayment;
    }

    @Override
    void setAverageMonthlySalary(float Value) {
        this.setAverageMonthlySalary(Value);
    }
}
