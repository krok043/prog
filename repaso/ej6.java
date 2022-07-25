package repaso;

import java.util.Scanner;

public class ej6 {
    public static void main(String[] args) {
        
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int m = in.nextInt();
        int total = 0;

        int[][] matriz = new int[n][m];

        for (int i = 0; i < n; i++){
            for (int j = 0; j < m; j++) {
                matriz[i][j] = in.nextInt();
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                int c = 0;
                while (matriz[i][j] > 0) {
                    matriz[i][j] = matriz[i][j] / 10;
                    c = c + 1;
                }

                if (c >= 3) {
                    total = total + 1;
                }
            }
        }
        System.out.println(total);
    }
}
