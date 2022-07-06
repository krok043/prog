package c_java;

public class ejemplo2 {
    public static int suma(int a, int b) {
        return a + b;
    }

    void saludar(String nombre) {
        System.out.println("Hola " + nombre);
    }

    public static void main(String[] args) {
        int resultado = suma(1, 2);
        System.out.println(resultado);
    }
}