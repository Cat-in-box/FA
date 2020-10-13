package Task_1;

public class Main {

    public static void main(String[] args) {

        System.out.println("Hello world!");
        Matrix matrix1 = new Matrix(5,5);
        matrix1.Fill();
        matrix1.PrintMatrix();

        Matrix matrix2 = new Matrix(5,4);
        matrix2.Fill();
        matrix2.PrintMatrix();

        Operations Opr = new Operations(matrix1,matrix2);
        Opr.Summ(-1).PrintMatrix();


    }
}
