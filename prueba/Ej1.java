package prueba;

import java.util.Scanner;

public class Ej1 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        int op, n, m;
        int[][] mat;
        int[] vec;
        
        do {
            System.out.println("1. Llenar matriz");
            System.out.println("2. Llenar vector");
            System.out.println("3. Hallar la suma de las diagonales de la matriz");
            System.out.println("4. Hallar la multiplicacion de una matriz x un vector");
            System.out.println("5. Salir");

            op = in.nextInt();

            switch (op) {
                case 1:
                    n = in.nextInt();
                    m = in.nextInt();
                    mat = new int[n][m];
                    for (int i = 0; i < n; i++) {
                        for (int j = 0; j < m; j++) {
                            mat[i][j] = in.nextInt();
                        }
                    }
                    break;
            
                case 2:
                    n = in.nextInt();
                    vec = new int[n];
                    for (int i = 0; i < n; i++) {
                        vec[i] = in.nextInt();
                    }
                    break;

                case 3:
                    // sumaDiagonales(mat);
                    break;

                case 4:
                    // int[][] mul = new int[n][m];
                    
                    //multiplicaMatrizVector(mat, vec);
                    break;
                
                case 5:
                    System.out.println("Adios");

                default:
                    System.out.println("Opcion incorrecta");
                    break;
            }
        } while ( op != 5);  
        in.close();      
    }

    public static void sumaDiagonales(int[][] mat, int n, int m) {
        int suma = 0;
        // for (int i = 0; i < n; i++) {
        //     for (int j = 0; j < m; j++) {
        //         suma = suma + 
        //     }
            
        // }

        int x = 0, y = mat.length - 1;
            while (x < mat.length && y >= 0) {
                suma += mat[y][x];
                x++;
                y--;
            }
        System.out.println();
    }
}
