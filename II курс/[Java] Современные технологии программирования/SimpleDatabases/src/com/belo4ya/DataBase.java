package com.belo4ya;

import com.belo4ya.models.User;

import java.sql.*;

public class DataBase {
    private static DataBase instance;

    private static Connection con;
    private static Statement stmt;
    private static ResultSet rs;

    private DataBase() {
        try {
            Class.forName("org.postgresql.Driver");
            con = DriverManager.getConnection(
                    "jdbc:postgresql://127.0.0.1:5432/docker",
                    "postgres",
                    "docker"
            );
            stmt = con.createStatement();
        } catch (ClassNotFoundException | SQLException e) {
            e.printStackTrace();
        }
    }

    public static DataBase getInstance() {
        if (instance == null) {
            instance = new DataBase();
        }
        return instance;
    }

    public void close() {
        try {
            con.close();
            stmt.close();
            rs.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void addUser(User user) {
        String query = "insert into \"user\" " +
                "(row_id, first_name, last_name, middle_name, login, password_hash, group_id, role_id) " +
                "values " +
                "(%s, \"%s\", \"%s\", \"%s\", \"%s\", \"%s\", %s, %s)";

        try {
            stmt.executeUpdate(String.format(
                    query,
                    user.getId(),
                    user.getFirstName(),
                    user.getLastName(),
                    user.getMiddleName(),
                    user.getLogin(),
                    user.getPasswordHash(),
                    user.getGroupId(),
                    user.getRoleId()));
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void getTeachers() {
        String query = "select * from \"user\" where role_id = 2";

        try {
            rs = stmt.executeQuery(query);
            while (rs.next()) {
                System.out.println(new User(rs));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void getStudents() {
        String query = "select * from \"user\" where role_id = 3";

        try {
            rs = stmt.executeQuery(query);
            while (rs.next()) {
                System.out.println(new User(rs));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void getTests(Integer userId) {

    }

}
