package com.java;

import java.time.Duration;
import java.time.Instant;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;


public class SearchComparator {

    public static void test() {
        List<Integer> list = new ArrayList<>();
        for (int i = 0; i < 10_000_000; i ++) {
            list.add(i);
        }
        int target = new Random().nextInt(10_000_000);

        System.out.println("contains " + target + ": " + list.contains(target));
        timerDecorator("linerSearch", list, target, SearchComparator::linerSearch);
        timerDecorator("binarySearch", list, target, SearchComparator::binarySearch);
    }

    public static boolean linerSearch(List<Integer> list, Integer target) {
        for (Integer t : list) {
            if (target.equals(t)) {
                return true;
            }
        }
        return false;
    }

    public static boolean binarySearch(List<Integer> list, Integer target) {
        if (list.size() == 0) {
            return false;
        }

        int midpoint = list.size() / 2;
        if (list.get(midpoint).equals(target)) {
            return true;
        }

        if (target < list.get(midpoint)) {
            return binarySearch(list.subList(0, midpoint), target);
        }
        else {
            return binarySearch(list.subList(midpoint + 1, list.size()), target);
        }
    }

    public static void timerDecorator(String title, List<Integer> list, Integer target, Function function) {
        Instant start = Instant.now();
        boolean result = function.accept(list, target);
        long elapsed = Duration.between(start, Instant.now()).toMillis();

        System.out.printf("%s %b: %d ms\n", title, result, elapsed);
    }

    @FunctionalInterface
    public interface Function {
        boolean accept(List<Integer> list, Integer target);
    }
}
