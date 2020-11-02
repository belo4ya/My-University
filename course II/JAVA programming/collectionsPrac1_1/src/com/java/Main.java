package com.java;

import java.util.ArrayList;
import java.util.Collection;
import java.util.HashSet;
import java.util.LinkedList;

public class Main {

    public static void main(String[] args) {
        ArrayList<String> testArrayList = new ArrayList<>();
        testArrayList.add("str");
        testArrayList.add("str");
        testArrayList.add("str");
        testArrayList.add("uniq");
        testArrayList.add("primary");

        System.out.println(removeDuplicates(testArrayList));

        int[] result = buildDictionary("Lorem ipsum dolor sit amet, consectetur adipiscing elit. " +
                "Nam eu dui lacus. Pellentesque ac fringilla felis. Cras lectus nisi, " +
                "congue sit amet dictum a, sodales et dui. Praesent sollicitudin, est " +
                "non vestibulum auctor, justo mauris pretium ex, volutpat porttitor ma" +
                "gna eros congue enim. Duis elit orci, efficitur pellentesque facilisi" +
                "s sed, luctus at massa. Nam ipsum massa, convallis in lorem id, porta" +
                " luctus turpis. Etiam.");

        for(int i = 0; i < result.length; i++){
            System.out.print((char) (i + 'а') + " = " + result[i] + ", ");
        }
        System.out.println();

        compare2Lists();
    }

    public static <T> Collection<T> removeDuplicates(Collection<T> collection) {
        return new HashSet<>(collection);
    }

    public static int[] buildDictionary(String text){
        text = text.toLowerCase();

        int[] result = new int['z' - 'a' + 1];
        for(int i = 0; i < text.length(); i++){
            char ch = text.charAt(i);
            if(ch >= 'a' && ch <= 'z'){
                result[ch - 'a']++;
            }
        }
        return result;
    }

    public static void compare2Lists() {
        ArrayList<Double> arrayList = new ArrayList<>();
        LinkedList<Double> linkedList = new LinkedList<>();
        final int N = 1_000_000;
        final int M = 100_000;
        long startTime = System.currentTimeMillis();
        for (int i = 0; i < N; i++) {
            arrayList.add(Math.random());
        }
        System.out.println("add: ArrayList: " + (System.currentTimeMillis() - startTime) + " ms");

        startTime = System.currentTimeMillis();
        for (int i = 0; i < N; i++) {
            linkedList.add(Math.random());
        }
        System.out.println("add: LinkedList: " + (System.currentTimeMillis() - startTime) + " ms");

        startTime = System.currentTimeMillis();
        for (int i = 0; i < M; i++) {
            arrayList.get(i);
        }
        System.out.println("get: ArrayList: " + (System.currentTimeMillis() - startTime) + " ms");

        startTime = System.currentTimeMillis();
        for (int i = 0; i < M; i++) {
            linkedList.get(i);
        }
        System.out.println("get: LinkedList: " + (System.currentTimeMillis() - startTime) + " ms");
    }
}
