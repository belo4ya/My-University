package com.java.StringBuilder.Commands;

public class ReplaceCommand extends Command {
    private final int start;
    private final int end;
    private final String str;

    public ReplaceCommand(StringBuilder stringBuilder, int start, int end, String str) {
        super(stringBuilder);
        this.start = start;
        this.end = end;
        this.str = str;
    }

    public void execute() {
        backup();
        stringBuilder.replace(start, end, str);
    }
}
