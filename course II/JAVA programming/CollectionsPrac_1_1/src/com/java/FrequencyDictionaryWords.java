package com.java;

import java.util.*;


public class FrequencyDictionaryWords {

    public static void test() {
        String text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, " +
                "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. " +
                "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris " +
                "nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in " +
                "reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla " +
                "pariatur. Excepteur sint occaecat cupidatat non proident, sunt in " +
                "culpa qui officia deserunt mollit anim id est laborum.";
        Map<String, Integer> dictionary = buildDictionary(text);

        ArrayList<Map.Entry<String, Integer>> entries = new ArrayList<>(dictionary.entrySet());
        entries.sort((o1, o2) -> o2.getValue() - o1.getValue());
        for (Map.Entry<String, Integer> entry : entries) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }

    }

    public static Map<String, Integer> buildDictionary(String text) {
        Map<String, Integer> dict = new HashMap<>();
        ArrayList<String> words = getWordsList(text);
        for (String word : words) {
            dict.compute(word, (key, value) -> value == null ? 1 : ++value);
        }

        return dict;
    }

    public static ArrayList<String> getWordsList(String text) {
        ArrayList<String> words = new ArrayList<>(
                Arrays.asList(
                        text.toLowerCase().replaceAll(
                                "[[\\W&&[^-]]\\d_]", " "
                        ).split("\\s")
                )
        );
        words.removeIf(word -> word.equals(""));
        return words;
    }
}
