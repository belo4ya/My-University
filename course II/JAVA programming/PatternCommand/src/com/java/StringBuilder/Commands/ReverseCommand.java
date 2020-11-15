package com.java.StringBuilder.Commands;

public class ReverseCommand extends Command {

    public ReverseCommand(StringBuilder stringBuilder) {
        super(stringBuilder);
    }

    public void execute() {
        backup();
        stringBuilder.reverse();
    }
}
