package repaso;

import java.util.Scanner;

public class ej7 {

    public static int[] burbuja(int[] A) {
        int i, j, aux;
        for (i = 0; i < A.length - 1; i++) {
            for (j = 0; j < A.length - i - 1; j++) {                                                              
                if (A[j + 1] < A[j]) {
                    aux = A[j + 1];
                    A[j + 1] = A[j];
                    A[j] = aux;
                }
            }
        }
        return A;
    }
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        // int n = in.nextInt();
        // int m = in.nextInt();
        // int[][] mat = new int[n][m];
        // for (int i = 0; i < n; i++) {
        //     for (int j = 0; j < m; j++){
        //         mat[i][j] = in.nextInt();
        //     }
        // }
        
        int n = 3;
        int m = 4;

        int[][] mat = {{2, 54, 234, 34},{3, 4, 1, 423}, {345, 3, 23, 3466}};


        int aux;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m-1; j++){
                for (int k = 0; k < m-j-1; k++){

                    if (mat[i][k+1] < mat[i][k]) {
                        aux = mat[i][k+1];
                        mat[i][k+1] = mat[i][k];
                        mat[i][k] = aux;
                    }
                }
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++){
                System.out.print(mat[i][j]);
                System.out.print(" ");
            }
            System.out.println();
        }
    }    
}
