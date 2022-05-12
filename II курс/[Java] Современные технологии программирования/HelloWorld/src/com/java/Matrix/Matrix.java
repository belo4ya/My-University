package com.java.Matrix;

import com.java.Matrix.Exceptions.ArrayNotRectangularException;
import com.java.Matrix.Exceptions.MatrixBadExponentNum;
import com.java.Matrix.Exceptions.MatrixNotAgreeException;
import com.java.Matrix.Exceptions.MatrixSizeNotEqualException;

import java.util.Arrays;

public class Matrix {

    private double[][] matrix;
    private int[] size = new int[2];

    public Matrix(double[][] matrix)
            throws ArrayNotRectangularException {

        int prevLen = matrix[0].length;
        for (double[] row : matrix) {
            if (prevLen != row.length) {
                throw new ArrayNotRectangularException(
                        "Массив должен быть прямоугольным!");
            }
            prevLen = row.length;
        }

        this.matrix = matrix;
        this.size[0] = matrix.length;
        this.size[1] = matrix[0].length;
    }

    public static void testMatrix()
            throws ArrayNotRectangularException, MatrixSizeNotEqualException,
            MatrixNotAgreeException, MatrixBadExponentNum {
        double[][] arr1 = {{1., 1}, {2, -2.}};
        Matrix matrix1 = new Matrix(arr1);
        System.out.println(Arrays.toString(matrix1.size()));

        double[][] arr2 = {{3., 3.}, {3, 1}};
        Matrix matrix2 = new Matrix(arr2);
        System.out.println(Arrays.toString(matrix2.size()));

        Matrix resAdd = Matrix.add(matrix1, matrix2);
        System.out.println(resAdd);

        Matrix resSub = Matrix.sub(matrix1, matrix2);
        System.out.println(resSub);

        Matrix resMulByNumber = Matrix.mulByNumber(matrix2, 3);
        System.out.println(resMulByNumber);

        double[][] arr3 = {{1,0,0,0}, {0,1,0,0}, {0,0,0,0}, {0,1,0,0}, {0,1,0,0}};
        double[][] arr4 = {{1,2,3}, {1,1,1}, {0,0,0}, {2,1,0}};
        Matrix matrix3 = new Matrix(arr3);
        Matrix matrix4 = new Matrix(arr4);

        Matrix resMul = Matrix.mul(matrix3, matrix4);
        System.out.println(resMul);

        System.out.println(resMul.transpose());
        System.out.println(Matrix.transpose(resMul));

        System.out.println(Matrix.exponentiationOf(matrix2, 4));
    }

    public int[] size() {
        return this.size;
    }

    public int rows() {
        return this.size[0];
    }

    public int columns() {
        return this.size[1];
    }

    public static Matrix add(Matrix matrix1, Matrix matrix2)
            throws MatrixSizeNotEqualException, ArrayNotRectangularException {

        if (!Arrays.equals(matrix1.size, matrix2.size)) {
            throw new MatrixSizeNotEqualException(
                    "Матрицы должны быть одинаковых размеров!");
        }

        double[][] res = new double[matrix1.rows()][matrix1.columns()];
        for (int i = 0; i < matrix1.rows(); i++) {
            for (int j = 0; j < matrix1.columns(); j++) {
                res[i][j] = matrix1.matrix[i][j] + matrix2.matrix[i][j];
            }
        }

        return new Matrix(res);
    }

    public static Matrix sub(Matrix matrix1, Matrix matrix2)
            throws MatrixSizeNotEqualException, ArrayNotRectangularException {

        if (!Arrays.equals(matrix1.size, matrix2.size)) {
            throw new MatrixSizeNotEqualException(
                    "Матрицы должны быть одинаковых размеров!");
        }

        double[][] res = new double[matrix1.rows()][matrix1.columns()];
        for (int i = 0; i < matrix1.rows(); i++) {
            for (int j = 0; j < matrix1.columns(); j++) {
                res[i][j] = matrix1.matrix[i][j] - matrix2.matrix[i][j];
            }
        }

        return new Matrix(res);
    }

    public static Matrix mulByNumber(Matrix matrix, double num)
            throws ArrayNotRectangularException {

        double[][] res = new double[matrix.rows()][matrix.columns()];
        for (int i = 0; i < matrix.rows(); i++) {
            for (int j = 0; j < matrix.columns(); j++) {
                res[i][j] = matrix.matrix[i][j] * num;
            }
        }

        return new Matrix(res);
    }

    public static Matrix mul(Matrix matrix1, Matrix matrix2)
            throws ArrayNotRectangularException, MatrixNotAgreeException {
        if (matrix1.columns() != matrix2.rows()) {
            throw new MatrixNotAgreeException("Матрицы должны быть согласованными: " +
                    "количество столбцов в матрице A должно совпадать с количеством строк в матрице B");
        }

        double[][] res = new double[matrix1.rows()][matrix2.columns()];
        for (int i = 0; i < matrix1.rows(); i++) {
            for (int j = 0; j < matrix2.columns(); j++) {
                for (int k = 0; k < matrix1.columns(); k++) {
                    res[i][j] += matrix1.matrix[i][k] * matrix2.matrix[k][j];
                }
            }
        }

        return new Matrix(res);
    }

    public static Matrix transpose(Matrix matrix)
            throws ArrayNotRectangularException {

        double[][] res = new double[matrix.columns()][matrix.rows()];
        for (int i = 0; i < matrix.rows(); i++) {
            for (int j = 0; j < matrix.columns(); j++) {
                res[j][i] = matrix.matrix[i][j];
            }
        }

        return new Matrix(res);
    }

    public Matrix transpose() {
        double[][] temp = new double[this.columns()][this.rows()];
        for (int i = 0; i < this.rows(); i++) {
            for (int j = 0; j < this.columns(); j++) {
                temp[j][i] = this.matrix[i][j];
            }
        }

        this.size[0] = temp.length;
        this.size[1] = temp[0].length;
        this.matrix = Arrays.copyOf(temp, temp.length);
        return this;
    }

    public static Matrix exponentiationOf(Matrix matrix, int num)
            throws MatrixBadExponentNum, MatrixNotAgreeException, ArrayNotRectangularException {

        if (num < 2) {
            throw new MatrixBadExponentNum("В качестве степени матрицы можно " +
                    "вводить целые неотрицательные числа большие единицы!");
        }

        Matrix res = matrix;
        for (int i = 0; i < num - 1; i++) {
            res = mul(matrix, res);
        }

        return res;
    }

    public double[][] toArray() {
        return matrix;
    }

    public String toString() {
        StringBuilder matrixString = new StringBuilder();
        for (int i = 0; i < this.rows(); i++) {
            for (int j = 0; j < this.columns(); j++) {
                matrixString.append(matrix[i][j]).append(" ");
            }
            matrixString.append("\n");
        }
        return matrixString.toString();
    }
}