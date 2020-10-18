package com.java.Task1;

public class Task1 {

    public static void testTask() {
        helloWorld();
        intVar();
        increment();
        swap(3, 10);
        getHypotenuse(4, 3);
        lastNum(1234);
        decCount(123456);
        decCount(23, true);
        subtract21(1337);
        arithmeticMean(10, 15);
        geometricMean(20, 11);
        distanceBetweenPoints(2.2f, 2.2f, 4.4f, 4.4f);
    }
    // задание 1
    public static void helloWorld() {
        System.out.println("Hello, World!");
    }
    // задание 2
    public static void intVar() {
        byte a = 10;
        System.out.println(a);
    }
    // задание 3
    public static void increment() {
        int a = 99999999;
        a++;
        System.out.println(a);
        ++a;
        System.out.println(a);
        a += 1;
        System.out.println(a);
    }
    // задание 4
    public static void swap(int a, int b) {
        int c;  // temp
        c = a;
        a = b;
        b = c;
        System.out.println("a = " + a + ", b = " + b);
        a = a^b^(b = a);
        System.out.println("a = " + a + ", b = " + b);
        a = a + b;
        b = a - b;
        a = a - b;
        System.out.println("a = " + a + ", b = " + b);
        a = -(a - b - (b = a));
        System.out.println("a = " + a + ", b = " + b);
    }
    // задание 5
    public static void getHypotenuse(int a, int b) {
        double c = Math.pow((a*a + b*b), 0.5);
        System.out.printf("a = %s, b = %s, c = %s\n", a, b, c);
    }
    // задание 6
    public static void lastNum(int n) {
        int last_num_int = n % 10;
        System.out.printf("Вариант 1: n = %s, last_num = %s\n", n, last_num_int);
        String last_num_str = Integer.toString(n);
        System.out.printf("Вариант 2: n = %s, last_num = %s\n", n,
                last_num_str.charAt(last_num_str.length()-1));
    }
    // задание 7
    public static void decCount(int n) {
        String n_str = Integer.toString(n);
        System.out.printf("n = %s, dec_value = %s\n", n_str,
                n_str.charAt(n_str.length() - 2));
    }
    // задание 8
    public static void decCount(int n, boolean flag) {
        String n_str = Integer.toString(n);
        if (n_str.length() == 2) {
            decCount(n);
        }
    }
    // задание 9
    public static int subtract21(int n) {
        int sub = n - 21;
        System.out.println(sub);
        return sub;
    }
    // задание 10
    public static float arithmeticMean(int a, int b) {
        float res = ((float) a + b) / 2;
        System.out.printf("Среднее арифтметическое %s и %s: %s\n", a, b, res);
        return res;
    }
    // задание 11
    public static double geometricMean(int a, int b) {
        double res = Math.sqrt(a * b);
        System.out.printf("Среднее геометрическое %s и %s: %s\n", a, b, res);
        return res;
    }
    // задание 12
    public static double distanceBetweenPoints(double x_1, double y_1, double x_2, double y_2) {
        double res = Math.sqrt(Math.pow((x_2 - x_1), 2) + Math.pow(y_2 - y_1, 2));
        System.out.printf("|A(%.2f, %.2f), B((%.2f, %.2f)| = %f\n",
                x_1, y_1, x_2, y_2, res);
        return res;
    }

}
