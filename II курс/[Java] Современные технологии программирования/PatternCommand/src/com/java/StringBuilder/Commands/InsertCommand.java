package com.java.StringBuilder.Commands;

public class InsertCommand extends Command {
    private final int status;
    int offset;
    Object obj;
    int index;
    char[] str;
    int len;
    CharSequence s;
    int start;
    int end;

    public InsertCommand(StringBuilder stringBuilder, int offset, Object obj) {
        super(stringBuilder);
        this.offset = offset;
        this.obj = obj;
        status = 1;
    }

    public InsertCommand(StringBuilder stringBuilder, int index, char[] str, int offset, int len) {
        super(stringBuilder);
        this.index = index;
        this.str = str;
        this.offset = offset;
        this.len = len;
        status = 2;
    }

    public InsertCommand(StringBuilder stringBuilder, int offset, CharSequence s, int start, int end) {
        super(stringBuilder);
        this.offset = offset;
        this.s = s;
        this.start = start;
        this.end = end;
        status = 3;
    }

    public void execute() {
        backup();
        switch (status) {
            case 1 -> stringBuilder.insert(offset, obj);
            case 2 -> stringBuilder.insert(index, str, offset, len);
            case 3 -> stringBuilder.insert(offset, s, start, end);
        }
    }

}
