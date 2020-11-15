package com.java;

public class BarMenu extends Menu {

    public BarMenu(Product... products) {
        super(products);
    }

    @Override
    public String toString() {
        return "BarMenu{" +
                "products=" + products +
                ", stopList=" + stopList +
                '}';
    }
}
