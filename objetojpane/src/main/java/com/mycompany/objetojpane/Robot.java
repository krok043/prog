package com.mycompany.objetojpane;

import java.util.Random;

public class Robot {
    private int porcentaje_vida;
    
    public Robot() {
        Random r = new Random();
        this.porcentaje_vida = r.nextInt(10, 101);
    }

    public int getPorcentaje_vida() {
        return porcentaje_vida;
    }
}
