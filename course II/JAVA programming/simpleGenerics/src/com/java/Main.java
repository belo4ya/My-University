package com.java;

import java.util.Arrays;
import java.util.function.Function;

public class Main {

    public static void main(String[] args) {
        String[] strings = new String[] {"Длинная строка", "строка", "стр"};
        System.out.println(Arrays.toString(
                filter(strings, s -> s.length() > 3)
        ));

        String[] strings1 = new String[100];
        System.out.println(Arrays.toString(
                fill(strings1, s -> s + "!")
        ));

    }

    public static <T> T[] filter(T[] array, Function<? super T, Boolean> filter) {
        int offset = 0;

        for (int i = 0; i < array.length; i++) {
            if(!filter.apply(array[i]))
                offset++;
            else
                array[i - offset] = array[i];
        }

        return Arrays.copyOf(array, array.length - offset);
    }

    public static <T> T[] fill(T[] array, Function<Integer, ? extends T> function) {
        for(int i = 0; i < array.length; i++){
            array[i] = function.apply(i);
        }

        return Arrays.copyOf(array, array.length);
    }

}
