package Task_1;

public class Operations {
    private int A[][];
    private int B[][];

    public Operations(Matrix a, Matrix b) {
        this.A = a.matr;
        this.B = b.matr;
    }

    public Matrix Summ(int x) {
        if (x < 0) {
            x = -1;
        }
        else {
            x = 1;
        }
        int m = this.A.length;
        int n = this.A[0].length;
        if ((this.A.length != this.B.length) | (this.A[0].length != this.B[0].length)) {
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
        Matrix C = new Matrix(m,n);
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                C.matr[i][j] = this.A[i][j] + x*this.B[i][j];
            }
        }
        return C;
    }
    //public Matrix Mult() {

    //}
}
