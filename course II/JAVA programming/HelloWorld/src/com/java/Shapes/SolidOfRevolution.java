package com.java.Shapes;

public class SolidOfRevolution extends Shape {
    protected double radius;

    public SolidOfRevolution(double radius) {
        super(Math.PI * radius * radius);
        this.radius = radius;
    }

    public double getRadius() {
        return radius;
    }
}
