package Task_1;

public class Operations {
    private int A[][];
    private int B[][];

    public Operations(int a[][], int b[][]) {
        this.A = a;
        this.B = b;
    }

    public int [][] Summ() {
        int m = this.A.length;
        int n = this.A[0].length;
        if ((this.A.length != this.B.length) & (this.A[0].length != this.B[0].length)) {
            System.out.println("Матрицы разного размера, мы их обрезали");

            if (this.A.length < this.B.length) {
                m = this.A.length;
            }
            else {
                m = this.B.length;
            }

            if (this.A[0].length < this.B[0].length) {
                n = this.A[0].length;
            }
            else {
                n = this.B[0].length;
            }
        }
        int C[][] = new int [m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                C[i][j] = this.A[i][j] + this.B[i][j];
            }
        }
        return C;
    }
}
