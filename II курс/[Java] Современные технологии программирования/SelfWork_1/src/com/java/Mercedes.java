package com.java;

public class Mercedes extends Car {
    private String tyreSupplier;

    public Mercedes(String color, double speed, int transmissionType,
                    double currentSpeed, double price, String tyreSupplier) {
        super(color, speed, transmissionType, currentSpeed, price);
        this.tyreSupplier = tyreSupplier;
    }

    public String getTyreSupplier() {
        return tyreSupplier;
    }
}
