package com.java;

public class Main {

    public static void main(String[] args) {
        // демонстрацию не успел

        Product cofe = new Product("Кофе", 60, "чашка", 20, new String[] {"dasd", "das"});
        Menu barMenu = new BarMenu(
                cofe, cofe, cofe
        );
        Menu foodMenu = new FoodMenu(
                cofe, cofe, cofe
        );

        Cafe bestCafe = new Cafe(barMenu, foodMenu);
        System.out.println(bestCafe.makeOrder("Кофе"));
    }
}
