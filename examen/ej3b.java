package examen;

import java.util.Scanner;
import java.util.jar.Attributes.Name;

public class ej3b {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();

        int[][] mat = new int[n][m];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                mat[i][j] = sc.nextInt();
            }
        }

        
        if (n == m) {
            int[][] nma = new int[n][m];
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++){
                    nma[i][j] = firstD(mat[i][j]);
                }
            }

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    System.out.print(nma[i][j] + " ");
                }
                System.out.println();
            }
        }
        else {
            int[] nma = new int[n];

            for (int i = 0; i < n; i++) {
                nma[i] = mayor(mat[i]);
            }

            System.out.println();
            for (int i = 0; i < nma.length; i++) {
                System.out.println(nma[i]);
            }
        }
        sc.close();
    }
    
    public static int firstD(int n) {
        int res = 0;
        while (n > 0) {
            if (n < 10)
            {
                res = n;
                break;
            }
            n = n / 10;
        }
        return res;
    }

    public static int mayor(int[] v) {
        int m = 0;

        for (int i = 0; i < v.length; i++) {
            if (m < v[i]) {
                m = v[i];
            }
        }
        return m;
    }
}
