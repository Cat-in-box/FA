package Task_1;

import java.util.concurrent.ThreadLocalRandom;

public class Matrix {
    private int matr[][];

    public Matrix(int m, int n) {
        this.matr = new int[m][n];
    }

    public void Fill() {
        for (int i = 0; i < this.matr.length; i++) {
            for (int j = 0; j < this.matr[i].length; j++) {
                this.matr[i][j] = ThreadLocalRandom.current().nextInt(0, 9 + 1);
            }
        }
    }

    public void PrintMatrix() {
        for (int i = 0; i < matr.length; i++) {
            for (int j = 0; j < matr[i].length; j++){
                System.out.print(matr[j][i] + " ");
            }
            System.out.println("");
        }
    }
}
