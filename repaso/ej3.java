package repaso;

import java.util.Scanner;

public class ej3 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int cx = sc.nextInt();

        int[] x = new int[cx];

        for (int i = 0; i < cx; i++) {
            x[i] = sc.nextInt();
        }

        int[] inversox = new int[cx];

        for (int i = 0; i < inversox.length; i++) {
            inversox[i] = inversorDigitos(x[i]);
        }
        
    }

    public static int inversorDigitos(int n) {
        return 0;
    }

    public static int digitoMedio(int n) {
        return 0;
    }

    public static int cantidadDigito(int n) {
        int c = 0;
        while (n > 0) {
            n = n / 10;
            c = c + 1;
        }
        return c;
    }
}
