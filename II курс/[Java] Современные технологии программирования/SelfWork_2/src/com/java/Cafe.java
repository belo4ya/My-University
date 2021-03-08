package com.java;

public class Cafe {
    private Menu barMenu;
    private Menu foodMenu;

    public Cafe(Menu barMenu, Menu foodMenu) {
        this.foodMenu = foodMenu;
        this.barMenu = barMenu;
    }

    public void addToBarMenu(Product product) {
        barMenu.addProduct(product);
    }

    public void removeProductBarMenu(Product product) {
        barMenu.removeProduct(product);
    }

    public void addToFoodMenu(Product product) {
        foodMenu.addProduct(product);
    }

    public void removeProductFoodMenu(Product product) {
        foodMenu.removeProduct(product);
    }

    public Order makeOrder(String... products) {
        return new Order(barMenu, foodMenu, products);
    }
}
