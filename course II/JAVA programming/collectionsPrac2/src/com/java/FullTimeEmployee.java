package com.java;

public class FullTimeEmployee extends Employee {
    private double monthlyRate;

    public FullTimeEmployee(String name, double monthlyRate) {
        super(name);
        this.monthlyRate = Math.abs(monthlyRate);
    }

    public double getMonthlyRate() {
        return monthlyRate;
    }

    public void setMonthlyRate(double monthlyRate) {
        this.monthlyRate = Math.abs(monthlyRate);
    }

    @Override
    public double getPayroll() {
        return monthlyRate;
    }
}
