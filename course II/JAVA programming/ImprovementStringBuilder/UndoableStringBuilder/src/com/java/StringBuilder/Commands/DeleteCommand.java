package com.java.StringBuilder.Commands;

public class DeleteCommand extends Command {
    private final int start;
    private final int end;

    public DeleteCommand(StringBuilder stringBuilder, int start, int end) {
        super(stringBuilder);
        this.start = start;
        this.end = end;
    }

    public void execute() {
        backup();
        stringBuilder.delete(start, end);
    }
}
