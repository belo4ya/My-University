package com.belo4ya;

import com.belo4ya.models.User;

public class Main {

    public static void main(String[] args) {
        DataBase db = DataBase.getInstance();

        User userTeacher = new User(4);
        User userStudent = new User(5);
        User userAdministrator = new User(6);
        userTeacher.setFirstName("teacher").setRoleId(2);
        userStudent.setFirstName("student").setRoleId(3);
        userAdministrator.setFirstName("administrator").setRoleId(1);

        db.addUser(userTeacher);
        db.addUser(userStudent);
        db.addUser(userAdministrator);

        System.out.println("Преподаватели:");
        db.getTeachers();
        System.out.println("\nСтуденты:");
        db.getStudents();
    }
}
