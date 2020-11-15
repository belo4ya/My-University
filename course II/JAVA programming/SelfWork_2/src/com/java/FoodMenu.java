package com.java;

public class FoodMenu extends Menu {

    public FoodMenu(Product... products) {
        super(products);
    }

    @Override
    public String toString() {
        return "FoodMenu{" +
                "products=" + products +
                ", stopList=" + stopList +
                '}';
    }
}
