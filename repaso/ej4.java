package repaso;

import java.util.Scanner;
public class ej4 {
    
    public static void main(String args[]){
        Scanner in = new Scanner(System.in);
        String x = in.nextLine();
        System.out.println("Introduce una frase: ");
        String[] letraArray = in.nextLine().split(" ");
    
        int contadorLetraRepetida = 0;
        in.close();

        for(int j =0;j<letraArray.length;j++){

            if (x.equals(letraArray[j]))
                contadorLetraRepetida++;
        }
        System.out.println("El elemento '" + x + "' se repite "+ contadorLetraRepetida + " veces.");
    }
}

// 1 3 4 3 4 5

/*
 * 2 3 4 2 
 * 2 3 4 5
 */

/*
 * 1 2 3 5 8
 * 5 8 4 8 8
 * 4 5 8 4 8
 * 4 8 7 0 2
 * 5 8 7 8 4
 */