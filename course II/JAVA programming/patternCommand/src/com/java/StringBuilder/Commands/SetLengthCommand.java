package com.java.StringBuilder.Commands;

public class SetLengthCommand extends Command {
    private final int newLength;

    public SetLengthCommand(StringBuilder stringBuilder, int newLength) {
        super(stringBuilder);
        this.newLength = newLength;
    }

    public void execute() {
        backup();
        stringBuilder.setLength(newLength);
    }
}
