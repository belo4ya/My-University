package com.java.Vectors;

import java.util.Arrays;
import java.util.Random;

public class Vector {

    private double x;
    private double y;
    private double z;

    public Vector(double x, double y, double z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }

    public static void testVector() {
        Vector vec1 = new Vector(1, 2, 3);
        Vector vec2 = new Vector(4, 4, 4);

        System.out.println(vec1);
        System.out.println(vec2);

        System.out.println("|vec1| = " + vec1.length());
        System.out.println("|vec2| = " + vec2.length());

        System.out.println("Скалярное произведение vec1 и vec2: " +
                Vector.scalarProduct(vec1, vec2));
        System.out.println("Векторное произведение vec1 и vec2: " +
                Vector.vectorProduct(vec1, vec2));

        System.out.println("Косинус угла между vec1 и vec2: " +
                Vector.getCosAngle(vec1, vec2));
        System.out.println("Угол между vec1 и vec2: " +
                Vector.getAngle(vec1, vec2));

        System.out.printf("vec_3 = vec1 + vec2 = %s\n", Vector.add(vec1, vec2));
        vec1.addVector(vec2);
        System.out.printf("vec1 += vec2 = %s\n", vec1);

        System.out.printf("vec_4 = vec1 - vec2 = %s\n", Vector.sub(vec1, vec2));
        vec1.subVector(vec2);
        System.out.printf("vec1 -= vec2 = %s\n", vec1);

        int n = 4;
        System.out.print(Arrays.toString(Vector.randomVectors(n)));
    }

    public double length() {
        return Math.sqrt(x*x + y*y + z*z);
    }

    public static double scalarProduct(Vector vec_1, Vector vec_2) {
        return (vec_1.x * vec_2.x + vec_1.y * vec_2.y + vec_1.z * vec_2.z);
    }

    public static Vector vectorProduct(Vector vec_1, Vector vec_2) {
        double x = vec_1.y * vec_2.z - vec_1.z * vec_2.y;
        double y = vec_1.z * vec_2.x - vec_1.x * vec_2.z;
        double z = vec_1.x * vec_2.y - vec_1.y * vec_2.x;
        return new Vector(x, y, z);
    }

    public static double getCosAngle(Vector vec_1, Vector vec_2) {
        return scalarProduct(vec_1, vec_2) / (vec_1.length() * vec_2.length());
    }

    public static double getAngle(Vector vec_1, Vector vec_2) {
        return Math.toDegrees(Math.acos(getCosAngle(vec_1, vec_2)));
    }

    public void addVector(Vector vec) {
        this.x += vec.x;
        this.y += vec.y;
        this.z += vec.z;
    }

    public static Vector add(Vector vec_1, Vector vec_2) {
        double x = vec_1.x + vec_2.x;
        double y = vec_1.y + vec_2.y;
        double z = vec_1.z + vec_2.z;
        return new Vector(x, y, z);
    }

    public void subVector(Vector vec) {
        this.x -= vec.x;
        this.y -= vec.y;
        this.z -= vec.z;
    }

    public static Vector sub(Vector vec_1, Vector vec_2) {
        double x = vec_1.x - vec_2.x;
        double y = vec_1.y - vec_2.y;
        double z = vec_1.z - vec_2.z;
        return new Vector(x, y, z);
    }

    public static Vector[] randomVectors(int n) {
        int min = -100;
        int max = 100;
        Vector[] vec_array = new Vector[n];
        Random random = new Random();
        for (int i = 0; i < n; i++) {
            int[] coords = new int[3];
            for (int j = 0; j < 3; j++){
                coords[j] = random.nextInt((max - min) + 1) + min;
            }
            int x = coords[0]; int y = coords[1]; int z = coords[2];
            vec_array[i] = new Vector(x, y, z);
        }
        return vec_array;
    }

    public String toString() {
        return "Vector{" +
                "x=" + x +
                ", y=" + y +
                ", z=" + z +
                '}';
    }

    public double getX() {
        return x;
    }

    public double getY() {
        return y;
    }

    public double getZ() {
        return z;
    }

}
