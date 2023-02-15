package com.mycompany.objetojpane;

import javax.swing.JOptionPane;
import java.util.Random;

public class Objetojpane {

    public static void main(String[] args) {
        
        int x = JOptionPane.showConfirmDialog(null, "Crear robots");
        if (x == 0) {
            Random r = new Random();
            int can_robots = r.nextInt(5, 11);
            
            Robot[] robots = new Robot[can_robots];
            
            for (int i = 0; i < can_robots; i++) {
                Robot r1 = new Robot();
                robots[i] = r1;
            }
            
            for (int i = 0; i < can_robots; i++) {
                System.out.println("Porcentaje de vida de robot " + i + ": " + robots[i].getPorcentaje_vida());
            }
            
            int prim = -1; //Porcentaje de vida
            int seg = -1;
            int ter = -1;
            
            for (int i = 0; i < can_robots; i++) {
                int vida = robots[i].getPorcentaje_vida();
                if (vida > prim){
                    ter = seg;
                    seg = prim;                    
                    prim = vida;
                }
                else if (vida > seg) {
                    ter = seg;
                    seg = vida;
                }
                else if(vida > ter) {
                    ter = vida;
                }
            }
            
            JOptionPane.showMessageDialog(null, "" + prim + "\n" + seg + "\n" + ter);
        }
        
    }
}
