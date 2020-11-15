package com.java;

import com.java.Matrix.Exceptions.ArrayNotRectangularException;
import com.java.Matrix.Exceptions.MatrixBadExponentNum;
import com.java.Matrix.Exceptions.MatrixNotAgreeException;
import com.java.Matrix.Exceptions.MatrixSizeNotEqualException;
import com.java.Matrix.Matrix;
import com.java.RandomWeight.RandomWeight;
import com.java.Task1.Task1;
import com.java.Vectors.Vector;

public class Main {

    public static void main(String[] args)
            throws ArrayNotRectangularException, MatrixSizeNotEqualException,
            MatrixNotAgreeException, MatrixBadExponentNum {

        Task1.testTask();
        System.out.println("\n");

        Vector.testVector();
        System.out.println("\n");

        Matrix.testMatrix();
        System.out.println("\n");

        RandomWeight.testRandomWeight();
    }

}
