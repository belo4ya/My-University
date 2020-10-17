package com.java.Shapes;

public class Ball extends SolidOfRevolution {

    public Ball(double radius) {
        super(radius);
        this.volume = Math.PI * Math.pow(radius, 3) / 3;
    }
}
