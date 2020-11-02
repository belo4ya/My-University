package com.java;

public class PartTimeEmployee extends Employee {
    private double hourlyRate;

    public PartTimeEmployee(String name, double hourlyRate) {
        super(name);
        this.hourlyRate = Math.abs(hourlyRate);
    }

    public double getHourlyRate() {
        return hourlyRate;
    }

    public void setHourlyRate(double hourlyRate) {
        this.hourlyRate = Math.abs(hourlyRate);
    }

    @Override
    public double getPayroll() {
        return 20.8 * 8 * this.hourlyRate;
    }
}
