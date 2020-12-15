package com.belo4ya;

public class Main {

    public static void main(String[] args) {
        DataBase db = DataBase.getInstance();
        System.out.println("Преподаватели:");
        db.getTeachers();
        System.out.println("\nСтуденты:");
        db.getStudents();
    }
}
