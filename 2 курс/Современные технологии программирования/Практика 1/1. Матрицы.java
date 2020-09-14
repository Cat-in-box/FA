public class MyClass {
    public static void main(String args[]) {

        System.out.println("Meow");

        Matrix Matrix1 = new Matrix(2, 2);
        /// Matrix.set_size(2, 2);
        System.out.println(Matrix1.matrix.length);
        Matrix1.Fill_same_elements(1);
        System.out.println(Matrix1.matrix[0][0]);
    }

    public static class Matrix_operations {
        int a[][];
        int b[][];

        public Matrix_operations() {
        }

        public int[][] Summ () {

        }
    }

    public static class Matrix {
        int matrix[][];
        int m;
        int n;

        public Matrix (int m, int n) {
            this.m = m;
            this.n = n;
            this.matrix = new int [m][n];
        }

        public void Fill_same_elements(int value){
            for (int i = 0; i < this.m; i++) {
                for (int j = 0; j < this.n; j++){
                    matrix[i][j] = value;
                }
            }
        }

    }

}
