package com.java.StringBuilder.Commands;

public class DeleteCharAtCommand extends Command {
    private final int index;

    public DeleteCharAtCommand(StringBuilder stringBuilder, int index) {
        super(stringBuilder);
        this.index = index;
    }

    public void execute() {
        backup();
        stringBuilder.deleteCharAt(index);
    }
}
