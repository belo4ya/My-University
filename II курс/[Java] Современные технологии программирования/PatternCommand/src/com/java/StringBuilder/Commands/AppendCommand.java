package com.java.StringBuilder.Commands;

public class AppendCommand extends Command {
    private final int status;
    private Object obj;
    private CharSequence s;
    private char[] str;
    private int offset;
    private int len;
    private int start;
    private int end;

    public AppendCommand(StringBuilder stringBuilder, Object obj) {
        super(stringBuilder);
        this.obj = obj;
        status = 1;
    }

    public AppendCommand(StringBuilder stringBuilder, char[] str, int offset, int len) {
        super(stringBuilder);
        this.str = str;
        this.offset = offset;
        this.len = len;
        status = 2;
    }

    public AppendCommand(StringBuilder stringBuilder, CharSequence s, int start, int end) {
        super(stringBuilder);
        this.s = s;
        this.start = start;
        this.end = end;
        status = 3;
    }

    public void execute() {
        backup();
        switch (status) {
            case 1 -> stringBuilder.append(obj);
            case 2 -> stringBuilder.append(str, offset, len);
            case 3 -> stringBuilder.append(s, start, end);
        }
    }

}
