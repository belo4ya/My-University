package com.java;


public class Main {

    public static void main(String[] args) {
        TemperatureConvertor convertor = new TemperatureConvertor();
        System.out.println(convertor.celsiusToFahrenheit(15));
        System.out.println(convertor.fahrenheitToCelsius(convertor.celsiusToFahrenheit(15)));
    }
}
