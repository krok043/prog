package mix;

import java.util.Scanner;

public class ej2 {
    public static void opcion1() {
        Scanner sc = new Scanner(System.in);
        int n1 = sc.nextInt();
        int n2 = sc.nextInt();
        //.....
    }

    public static void main(String[] args) {
        System.out.println("1. Dados tres numeros, mostrar el elemento del medio");
        System.out.println("2. Determinar si un numero es perfecto");
        System.out.println("3. Salir");
        System.out.print("Ingresa opcion: ");

        Scanner sc = new Scanner(System.in);
        int op = sc.nextInt();

        sc.close();

        switch(op) {
            case 1:
                //Hacer programa para el elemento del medio
                opcion1();
                break;
            case 2:
                //Hacer programa para el numero perfecto
                break;
            case 3:
                //Salir
                System.out.println("Chau");
                break;
            default:
                //En caso de opcion incorrecta
                System.out.println("Flaco, has ingresado una opcion incorrecta");
        }
    }
}
