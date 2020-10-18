package com.java.StringBuilder.Commands;


public abstract class Command {
    public StringBuilder stringBuilder;
    private String backup;

    public Command(StringBuilder stringBuilder) {
        this.stringBuilder = stringBuilder;
    }

    void backup() {
        backup = stringBuilder.toString();
    }

    public StringBuilder undo() {
        return new StringBuilder(backup);
    }

    public abstract void execute();
}