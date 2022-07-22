package examen;

import java.util.Scanner;

public class ej_1a {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String cad = sc.nextLine();
        sc.close();
        int len = cad.length();
        String cad2 = "";

        if (len % 2 == 0){

            // String vo = "aeiou";
            // for (char c : cad.toCharArray()){
            //     if (vo.indexOf(c) != -1) {
            //         int p = cad.indexOf(c);
            //         cad.replace(c, "");

            //     }
            // }

            cad2 = cad.replaceAll("/[aeiou]/", "");
            // for (int i = 0; i < len; i++) {
            //     char c = cad.charAt(i);
            //     if (c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u')
            //         cad2 += c;
            // }
        }
        else {
            for (int i = 0; i < cad.length(); i++) {
                
            }
        }

        System.out.println(cad2);
    }
}