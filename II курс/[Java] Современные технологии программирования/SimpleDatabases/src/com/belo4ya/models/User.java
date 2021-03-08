package com.belo4ya.models;

import java.sql.ResultSet;
import java.sql.SQLException;

public class User {
    public static final String colId = "row_id";
    public static final String colFirstName = "first_name";
    public static final String colLastName = "last_name";
    public static final String colMiddleName = "middle_name";
    public static final String colLogin = "login";
    public static final String colPasswordHash = "password_hash";
    public static final String colGroupId = "group_id";
    public static final String colRoleId = "role_id";

    private Integer id;
    private String firstName;
    private String lastName;
    private String middleName;
    private String login;
    private String passwordHash;
    private Integer groupId;
    private Integer roleId;

    public User(ResultSet rs) throws SQLException {
        id = rs.getInt(colId);
        firstName = rs.getString(colFirstName);
        lastName = rs.getString(colLastName);
        middleName = rs.getString(colMiddleName);
        login = rs.getString(colLogin);
        passwordHash = rs.getString(colPasswordHash);
        groupId = rs.getInt(colGroupId);
        roleId = rs.getInt(colRoleId);
    }

    public User(Integer id) {
        this.id = id;
    }

    public String getFirstName() {
        return firstName;
    }

    public User setFirstName(String firstName) {
        this.firstName = firstName;
        return this;
    }

    public String getLastName() {
        return lastName;
    }

    public User setLastName(String lastName) {
        this.lastName = lastName;
        return this;
    }

    public String getMiddleName() {
        return middleName;
    }

    public User setMiddleName(String middleName) {
        this.middleName = middleName;
        return this;
    }

    public String getLogin() {
        return login;
    }

    public User setLogin(String login) {
        this.login = login;
        return this;
    }

    public String getPasswordHash() {
        return passwordHash;
    }

    public User setPasswordHash(String passwordHash) {
        this.passwordHash = passwordHash;
        return this;
    }

    public Integer getGroupId() {
        return groupId;
    }

    public User setGroupId(Integer groupId) {
        this.groupId = groupId;
        return this;
    }

    public Integer getRoleId() {
        return roleId;
    }

    public User setRoleId(Integer roleId) {
        this.roleId = roleId;
        return this;
    }

    public Integer getId() {
        return id;
    }

    public User setId(Integer id) {
        this.id = id;
        return this;
    }

    @Override
    public String toString() {
        return "User{" +
                "id=" + id +
                ", firstName='" + firstName + '\'' +
                ", lastName='" + lastName + '\'' +
                ", middleName='" + middleName + '\'' +
                ", login='" + login + '\'' +
                ", passwordHash='" + passwordHash + '\'' +
                ", groupId=" + groupId +
                ", roleId=" + roleId +
                '}';
    }
}
