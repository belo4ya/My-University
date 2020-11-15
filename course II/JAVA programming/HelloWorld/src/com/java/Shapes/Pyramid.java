package com.java.Shapes;

public class Pyramid extends Shape {
    protected double s;
    protected double h;

    public Pyramid(double s, double h) {
        super(s * h / 3);
        this.s = s;
        this.h = h;
    }

    public double getH() {
        return h;
    }

    public double getS() {
        return s;
    }
}
