package com.java;


public class TemperatureConvertor implements BaseTemperatureConverter {
    private static final double FAHRENHEIT = 32;
    private static final double KELVIN = 273.15;

    @Override
    public double celsiusToFahrenheit(double value) {
        return FAHRENHEIT + value * 1.8;
    }

    @Override
    public double celsiusToKelvin(double value) {
        return value + KELVIN;
    }

    @Override
    public double fahrenheitToCelsius(double value) {
        return (value - FAHRENHEIT) / 1.8;
    }

    @Override
    public double kelvinToCelsius(double value) {
        return value - KELVIN;
    }
}