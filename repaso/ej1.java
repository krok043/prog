package repaso;

import java.util.Scanner;

public class ej1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        char[] cad = sc.nextLine().toCharArray();

        int cantidad_elementos = cad.length - 1;

        for (int i = cantidad_elementos; i >= 0; i--) {
            System.out.print(cad[i]);
        }

        sc.close();
    }
}