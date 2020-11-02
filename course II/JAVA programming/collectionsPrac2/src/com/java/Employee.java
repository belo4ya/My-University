package com.java;

import java.io.Serializable;

abstract public class Employee implements Comparable<Employee>, Serializable {
    private static final long serialVersionUID = 1L;

    private static long counter = 0;
    private final long id;
    private final String name;

    protected Employee(String name) {
        this.name = name;
        id = ++counter;
    }

    public long getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    abstract public double getPayroll();

    @Override
    public int compareTo(Employee o) {
        return name.compareTo(o.getName());
    }

    @Override
    public String toString() {
        return "Employee{" +
                "name='" + name + "', " +
                "id='" + id + '\'' +
                '}';
    }
}
