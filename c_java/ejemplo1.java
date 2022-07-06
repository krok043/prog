package c_java;

import java.util.Scanner;

public class ejemplo1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        //Crear una variable
        //TipodeDato nombreVariable;
        //nombreVariable = valorVariable;
        //TipodeDato nombreVariable = valorVariable;

        String nombre = sc.next();
        int edad = sc.nextInt();
        double altura = sc.nextDouble();
        
        System.out.println("Ingresaste el nombre de: " + nombre + ", tiene de edad: " + 
            edad + ", tiene una altura de: " + altura);        
    }
}