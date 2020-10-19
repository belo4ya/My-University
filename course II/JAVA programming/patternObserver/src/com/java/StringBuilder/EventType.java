package com.java.StringBuilder;

public enum  EventType {
    create("create"),
    append("append"),
    appendCodePoint("appendCodePoint"),
    delete("delete"),
    deleteCharAt("deleteCharAt"),
    insert("insert"),
    replace("replace"),
    reverse("reverse"),
    setCharAt("setCharAt"),
    setLength("setLength");

    private final String type;

    EventType(String type) {
        this.type = type;
    }

    public String getType() {
        return type;
    }

    @Override
    public String toString() {
        return "EventType{" +
                "type='" + type + '\'' +
                '}';
    }
}
