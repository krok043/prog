package examen;

import java.util.Scanner;

public class ej1b {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String cad = sc.nextLine();
        sc.close();
        int len = cad.length();

        if (len % 2 == 0){
            char[] ccad = cad.toCharArray();
            for (int i = 0; i < ccad.length; i++) {
                if (ccad[i] == 'a')
                    ccad[i] = '1';
                if (ccad[i] == 'e')
                    ccad[i] = '2';
                if (ccad[i] == 'i')
                    ccad[i] = '3';
                if (ccad[i] == 'o')
                    ccad[i] = '4';
                if (ccad[i] == 'u')
                    ccad[i] = '5';
            }

            cad = ccad.toString();

        }
        else {
            char[] ccad = cad.toCharArray();
            for (int i = 0; i < ccad.length; i++) {
                if (ccad[i] != 'a' && ccad[i] != 'e' && ccad[i] != 'i' && ccad[i] != 'o' && ccad[i] != 'u' && ccad[i] != ' ')
                    ccad[i] = Character.toUpperCase(ccad[i]);
            }
            cad = "";
            for (int i = 0; i < ccad.length; i++) {
                cad = cad + ccad[i];
                
            }
        }
        System.out.println(cad);
    }
}
