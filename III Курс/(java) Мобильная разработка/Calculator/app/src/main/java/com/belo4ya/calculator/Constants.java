package com.belo4ya.calculator;

import java.util.HashSet;

public class Constants {
    public static final String ZERO = "0";
    public static final String ONE = "1";
    public static final String TWO = "2";
    public static final String THREE = "3";
    public static final String FOUR = "4";
    public static final String FIVE = "5";
    public static final String SIX = "6";
    public static final String SEVEN = "7";
    public static final String EIGHT = "8";
    public static final String NINE = "9";
    public static final HashSet<String> NUMBERS = new HashSet<>();

    public static final String ADD = "+";
    public static final String SUB = "-";
    public static final String MUL = "*";
    public static final String DIV = "/";
    public static final HashSet<String> OPERATIONS = new HashSet<>();

    static {
        NUMBERS.add(ZERO);
        NUMBERS.add(ONE);
        NUMBERS.add(TWO);
        NUMBERS.add(THREE);
        NUMBERS.add(FOUR);
        NUMBERS.add(FIVE);
        NUMBERS.add(SIX);
        NUMBERS.add(SEVEN);
        NUMBERS.add(EIGHT);
        NUMBERS.add(NINE);
    }

    static {
        OPERATIONS.add(ADD);
        OPERATIONS.add(SUB);
        OPERATIONS.add(MUL);
        OPERATIONS.add(DIV);
    }
}
