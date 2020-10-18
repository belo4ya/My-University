package com.java.StringBuilder.Commands;

public class SetCharAtCommand extends Command {
    private final int index;
    private final char ch;

    public SetCharAtCommand(StringBuilder stringBuilder, int index, char ch) {
        super(stringBuilder);
        this.index = index;
        this.ch = ch;
    }

    public void execute() {
        backup();
        stringBuilder.setCharAt(index, ch);
    }
}
