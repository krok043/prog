package repaso;

import java.util.Scanner;

public class ej9 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        int n = in.nextInt();
        int m = in.nextInt();
        int[][] mat = new int[n][m];

        int c = 1;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                mat[j][i] = c;
                c++; 
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                System.out.print(mat[i][j]);
                System.out.print(" ");
            }
            System.out.println();
        }

        in.close();
    }
}
