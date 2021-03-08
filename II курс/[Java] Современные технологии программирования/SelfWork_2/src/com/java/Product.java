package com.java;

import java.util.Arrays;

public class Product {
    private final float price;
    private final String unit;
    private int amount;
    private final String name;
    private final String[] meal;

    public Product(String name, float price, String unit, int amount, String[] meal) {
        this.name = name;
        this.price = price;
        this.unit = unit;
        this.amount = amount;
        this.meal = meal;
    }

    public Product(Product product) {
        this.name = product.name;
        this.price = product.price;
        this.unit = product.unit;
        this.amount = 1;
        this.meal = product.meal;
    }

    public String getName() {
        return name;
    }

    public float getPrice() {
        return price;
    }

    public String getUnit() {
        return unit;
    }

    public int getAmount() {
        return amount;
    }

    public void decrementAmount() {
        if (amount > 0) {
            amount--;
        }
    }

    public void updateAmount(int amount) {
        this.amount = amount;
    }

    public String[] getMeal() {
        return meal;
    }

    @Override
    public String toString() {
        return "Product{" +
                "name=" + name +
                "price=" + price +
                ", unit=" + unit +
                ", amount=" + amount +
                ", meal=" + Arrays.toString(meal) +
                '}';
    }
}
