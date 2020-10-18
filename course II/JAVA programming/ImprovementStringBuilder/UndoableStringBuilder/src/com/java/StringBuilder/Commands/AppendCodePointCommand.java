package com.java.StringBuilder.Commands;

public class AppendCodePointCommand extends Command{
    private final int codePoint;

    public AppendCodePointCommand(StringBuilder stringBuilder, int codePoint) {
        super(stringBuilder);
        this.codePoint = codePoint;
    }

    public void execute() {
        backup();
        stringBuilder.appendCodePoint(codePoint);
    }
}
