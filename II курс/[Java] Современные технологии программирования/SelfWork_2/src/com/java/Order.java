package com.java;

import java.util.HashSet;

public class Order {
    static private int counter = 0;
    private final int id;
    private HashSet<Product> products = new HashSet<>();
    private Menu barMenu;
    private Menu foodMenu;
    private float cost;
    private boolean status;

    public Order(Menu barMenu, Menu foodMenu) {
        id = counter++;
        this.barMenu = barMenu;
        this.foodMenu = foodMenu;
        this.cost = 0;
        this.status = true;
    }

    public Order(Menu barMenu, Menu foodMenu, String[] products) {
        id = counter++;
        this.barMenu = barMenu;
        this.foodMenu = foodMenu;
        makeOrder(products);
        this.status = true;
    }

    public int getId() {
        return id;
    }

    public float getCost() {
        return cost;
    }

    public void makeOrder(String... products) {
        for (String p : products) {
            Product product = barMenu.orderProduct(p);
            if (product == null) {
                product = foodMenu.orderProduct(p);
            }
            if (product != null) {
                this.products.add(product);
                this.cost += product.getPrice();
            }
        }
    }

    public void closeOrder() {
        for (Product p : products) {
            foodMenu.addProduct(p);
        }
        status = false;
    }

    @Override
    public String toString() {
        return "Order{" +
                "id=" + id +
                ", products=" + products +
                ", cost=" + cost +
                '}';
    }
}
