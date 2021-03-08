package com.java;

public class Bmw extends Car{
    private String assemblyCountry;

    public Bmw(String color, double speed, int transmissionType,
               double currentSpeed, double price, String assemblyCountry) {
        super(color, speed, transmissionType, currentSpeed, price);
        this.assemblyCountry = assemblyCountry;
    }

    public String getAssemblyCountry() {
        return assemblyCountry;
    }
}
