package com.java.RandomWeight;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class RandomWeight {
    private final double[] values;
    private final int[] weights;
    private final int total;

    public static void testRandomWeight() {
        double[] arr1 = new double[]{1, 2, 3};
        int[] arr2 = new int[]{3, 7, 10};
        Double[] arr3 = new Double[100];
        RandomWeight generator = new RandomWeight(arr1, arr2);

        for (int i = 0; i < 100; i++) {;
            arr3[i] = generator.getValue();
        }

        Map<Double, Integer> counter = new HashMap<Double, Integer>();

        for (Double tempChar : arr3) {
            if (!counter.containsKey(tempChar)) {
                counter.put(tempChar, 1);
            } else {
                counter.put(tempChar, counter.get(tempChar) + 1);
            }
        }

        System.out.println(counter.toString());

        Arrays.sort(arr3);
        System.out.println(Arrays.toString(arr3));
    }

    public RandomWeight(double[] values, int[] weights) {
        this.values = values;
        this.weights = weights;
        this.total = Arrays.stream(weights).sum();
    }

    public double[] getValues() {
        return values;
    }

    public int[] getWeights() {
        return weights;
    }

    public int getTotal() {
        return total;
    }

    public Double getValue() {
        double rndWeight = Math.random() * total;
        double currentWeight = 0;
        for (int i = 0; i < values.length; i ++) {
            currentWeight += weights[i];
            if (currentWeight >= rndWeight) {
                return values[i];
            }
        }
        return null;
    }
}
