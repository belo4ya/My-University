package com.java.Shapes;

public class Box extends Shape {

    public Box(double volume) {
        super(volume);
    }

    public boolean add(Shape shape) {
        if (this.getVolume() >= shape.getVolume()) {
            this.setVolume(this.getVolume() - shape.getVolume());
            return true;
        } else return false;
    }
}
