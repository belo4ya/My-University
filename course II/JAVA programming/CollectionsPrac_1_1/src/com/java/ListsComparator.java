package com.java;

import java.time.Duration;
import java.time.Instant;
import java.util.*;
import java.util.function.Consumer;


public class ListsComparator {

    public static void test() {
        List<Integer> arrayList = new ArrayList<>();
        List<Integer> linkedList = new LinkedList<>();

        System.out.println("Тест: добавление элементов");
        timerDecorator(arrayList, ListsComparator::addRandomElements);
        timerDecorator(linkedList, ListsComparator::addRandomElements);

        System.out.println("\nТест: вставка элементов");
        timerDecorator(arrayList, ListsComparator::insertRandomElements);
        timerDecorator(linkedList, ListsComparator::insertRandomElements);

        System.out.println("\nТест: извлечение элементов");
        timerDecorator(arrayList, ListsComparator::getRandomElements);
        timerDecorator(linkedList, ListsComparator::getRandomElements);

    }

    public static void addRandomElements(List<Integer> list) {
        int n = 1_000_000;
        Random random = new Random();
        for (int i = 0; i < n; i++) {
            list.add(random.nextInt());
        }
    }

    public static void insertRandomElements(List<Integer> list) {
        int n = 10_000;
        Random random = new Random();
        for (int i = 0; i < n; i++) {
            list.add(random.nextInt(list.size()), random.nextInt());
        }
    }

    public static void getRandomElements(List<Integer> list) {
        int n = 10_000;
        Random random = new Random();
        for (int i = 0; i < n; i++) {
            list.get(random.nextInt(list.size()));
        }
    }

    public static void timerDecorator(List<Integer> list, Consumer<List<Integer>> function) {
        Instant start = Instant.now();
        function.accept(list);
        long elapsed = Duration.between(start, Instant.now()).toMillis();

        String listType = list.getClass().toString().split("\\.")
                [list.getClass().toString().split("\\.").length - 1];
        System.out.printf("%s: %d ms\n", listType, elapsed);
    }
}
