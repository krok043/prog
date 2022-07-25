package repaso;

import java.util.Scanner;

public class ej2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        char[] c1 = sc.nextLine().toCharArray();
        char[] c2 = sc.nextLine().toCharArray();
        int m = 0;

        if (c1.length > c2.length) m = c1.length;
        else m = c2.length; 

        for (int i = 0; i < m; i++) {
            if (c1.length > i)
                System.out.print(c1[i]);
            if (c2.length > i) 
                System.out.print(c2[i]);
        }
    }
}
