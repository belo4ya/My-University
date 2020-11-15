package com.java;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.HashSet;


public class DuplicateRemover {

    public static void test() {
        ArrayList<String> list = new ArrayList<>(Arrays.asList(
                "str", "str", "str", "string", "uniq", "primary"
        ));
        System.out.println("Исходный ArrayList:");
        System.out.println(list);
        System.out.println("ArrayList (HashSet<String>) после удаления дупликатов:");
        System.out.println(removeDuplicates(list));
    }

    public static <T> Collection<T> removeDuplicates(Collection<T> collection) {
        return new HashSet<>(collection);
    }
}
