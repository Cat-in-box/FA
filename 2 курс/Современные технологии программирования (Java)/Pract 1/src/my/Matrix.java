package my;

public class Matrix {
    private int matr[][];

    public Matrix(int m, int n) {
        this.matr = new int[m][n];
    }

    public void Ones() {
        for (int i = 0; i < matr.length; i++) {
            for (int j = 0; i < matr[i].length; j++) {
                if (i == j) {
                    matr[i][j] = 1;
                }
                else {
                    matr[i][j] = 0;
                }
            }
        }
    }

    public void PrintMatrix() {
        for (int i = 0; i < matr.length; i++) {
            for (int j = 0; i < matr[i].length; j++){
                System.out.print(matr[j][i]);
            }
            System.out.println("");
        }
    }
}
