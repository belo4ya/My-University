package com.java.Shapes;

public class Box extends Shape {

    public Box(double volume) {
        this.volume = volume;
    }

    public boolean add(Shape shape) {
        if (this.volume >= shape.volume) {
            this.volume -= shape.volume;
            return true;
        } else return false;
    }
}
