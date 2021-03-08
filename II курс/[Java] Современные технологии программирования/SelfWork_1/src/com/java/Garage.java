package com.java;

import java.util.Collection;
import java.util.HashMap;
import java.util.Map;

public class Garage {
    private int capacity;
    private Map<Car, Integer> cars;

    public static void main(String[] args) {
        Map<Car, Integer> testCars = new HashMap<>();
        testCars.put(new Bmw("green", 100, 1, 50, 100, "da"), 10);

        Garage garage = new Garage(17, testCars);
        garage.showCars();
    }

    public Garage(int capacity, Map<Car, Integer> cars) {
        this.capacity = capacity;
        // проверка на вместимость
        this.cars = cars;
    }

    public void showCars() {
        Collection <Integer> values = this.cars.values();
        Collection <Car> keys = this.cars.keySet();
        for (int i = 0; i < keys.size(); i++) {
            System.out.println(values.toArray()[i] + " - " + keys.toArray()[i]);
        }
    }
}