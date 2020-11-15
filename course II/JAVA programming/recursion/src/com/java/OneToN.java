package com.java;

public class OneToN {

    public static void test(int n) {
        System.out.println(OneToN.concatenate(n));
        OneToN.print(n);
        System.out.println();
    }

    public static void print(int n) {
        if (n == 1) {
            System.out.print(n + " ");
            return;
        }
        print(n - 1);
        System.out.print(n + " ");
    }

    public static String concatenate(int n) {
        if (n == 1) {
            return "1";
        }
        return concatenate(n - 1) + " " + n;
    }
}
