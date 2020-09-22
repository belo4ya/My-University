package com.java.Shapes;

public class SolidOfRevolution extends Shape {
    protected double radius;

    public SolidOfRevolution(double radius) {
        this.radius = radius;
        this.volume = Math.PI * radius * radius;
    }

    public double getRadius() {
        return radius;
    }
}
