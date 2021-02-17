package Task2;

public class HourlyEmployee extends Employee {
    private int rate;

    public HourlyEmployee(int ID, String name, int Rate) {
        super(ID, name);
        this.rate = Rate;
    }

    @Override
    void setAverageMonthlySalary(float Value) {
        this.setAverageMonthlySalary((float) (20.8*8*this.rate));
    }
}
