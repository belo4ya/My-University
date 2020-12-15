package com.belo4ya.models;

import java.sql.ResultSet;
import java.sql.SQLException;

public class User {
    private final String colId = "row_id";
    private final String colFirstName = "first_name";
    private final String colLastName = "last_name";
    private final String colMiddleName = "middle_name";
    private final String colLogin = "login";
    private final String colPasswordHash = "password_hash";
    private final String colGroupId = "group_id";
    private final String colRoleId = "role_id";

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

    public String getFirstName() {
        return firstName;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public String getMiddleName() {
        return middleName;
    }

    public void setMiddleName(String middleName) {
        this.middleName = middleName;
    }

    public String getLogin() {
        return login;
    }

    public void setLogin(String login) {
        this.login = login;
    }

    public String getPasswordHash() {
        return passwordHash;
    }

    public void setPasswordHash(String passwordHash) {
        this.passwordHash = passwordHash;
    }

    public Integer getGroupId() {
        return groupId;
    }

    public void setGroupId(Integer groupId) {
        this.groupId = groupId;
    }

    public Integer getRoleId() {
        return roleId;
    }

    public void setRoleId(Integer roleId) {
        this.roleId = roleId;
    }

    public Integer getId() {
        return id;
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
