package com.java;

import java.util.function.UnaryOperator;


public class EquationSolver {

    public static void test(UnaryOperator<Double> equation, double a, double b, double dev) {
        Double x = halfIntervalMethod(equation, a, b, dev);

        if (x == null) {
            System.out.printf("Не удалось решить уравнение на отрезке [%.1f; %.1f]", a, b);
        } else {
            System.out.println("x = " + x);
        }
    }

    public static Double function(Double x) {
        return x * (x + 5) - 20;  // = 0
    }

    public static Double halfIntervalMethod(UnaryOperator<Double> func, Double a, Double b, Double dev) {
        Double aVal = func.apply(a);
        Double bVal = func.apply(b);

        if (aVal > 0 && bVal < 0) {
            return search(func, b, a, dev);
        } else if (aVal < 0 && bVal > 0) {
            return search(func, a, b, dev);
        }

        return null;
    }

    public static Double search(UnaryOperator<Double> func, Double negPoint, Double posPoint, Double dev) {
        Double midpoint = (negPoint + posPoint) / 2.0;

        if (Math.abs(negPoint - posPoint) < dev) {
            return midpoint;
        }

        Double testValue = func.apply(midpoint);
        if (testValue > 0) {
            return search(func, negPoint, midpoint, dev);
        } else if (testValue < 0) {
            return search(func, midpoint, posPoint, dev);
        }

        return midpoint;
    }
}
