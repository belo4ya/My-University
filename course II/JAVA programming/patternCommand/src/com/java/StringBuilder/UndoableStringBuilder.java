package com.java.StringBuilder;


import com.java.StringBuilder.Commands.*;

import java.util.stream.IntStream;

public class UndoableStringBuilder
        implements java.io.Serializable, Comparable<StringBuilder>, CharSequence
{
    private StringBuilder stringBuilder;
    private final CommandHistory history = new CommandHistory();

    public UndoableStringBuilder() {
        stringBuilder = new StringBuilder();
    }

    public UndoableStringBuilder(int capacity) {
        stringBuilder = new StringBuilder(capacity);
    }

    public UndoableStringBuilder(CharSequence seq) {
        stringBuilder = new StringBuilder(seq);
    }

    public UndoableStringBuilder(String str) {
        stringBuilder = new StringBuilder(str);
    }


    // no pattern Command
    public int capacity() {
        return stringBuilder.capacity();
    }

    public char charAt(int index) {
        return stringBuilder.charAt(index);
    }

    public IntStream chars() {
        return stringBuilder.chars();
    }

    public int codePointAt(int index) {
        return stringBuilder.codePointAt(index);
    }

    public int codePointBefore(int index) {
        return stringBuilder.codePointBefore(index);
    }

    public int codePointCount(int beginIndex, int endIndex) {
        return stringBuilder.codePointCount(beginIndex, endIndex);
    }

    public IntStream codePoints() {
        return stringBuilder.codePoints();
    }

    public int compareTo(StringBuilder another) {
        return stringBuilder.compareTo(another);
    }

    public void ensureCapacity(int minimumCapacity) {
        stringBuilder.ensureCapacity(minimumCapacity);
    }

    public void getChars(int srcBegin, int srcEnd, char[] dst, int dstBegin) {
        stringBuilder.getChars(srcBegin, srcEnd, dst, dstBegin);
    }

    public int indexOf(String str) {
        return stringBuilder.indexOf(str);
    }

    public int indexOf(String str, int fromIndex) {
        return stringBuilder.indexOf(str, fromIndex);
    }

    public int lastIndexOf(String str) {
        return stringBuilder.lastIndexOf(str);
    }

    public int lastIndexOf(String str, int fromIndex) {
        return stringBuilder.lastIndexOf(str, fromIndex);
    }

    public int offsetByCodePoints(int index, int codePointOffset) {
        return stringBuilder.offsetByCodePoints(index, codePointOffset);
    }

    public CharSequence subSequence(int start, int end) {
        return stringBuilder.subSequence(start, end);
    }

    public String substring(int start) {
        return stringBuilder.substring(start);
    }

    public String substring(int start, int end) {
        return stringBuilder.substring(start, end);
    }

    public void trimToSize() {
        stringBuilder.trimToSize();
    }


    // pattern Command
    public UndoableStringBuilder append(int i) {
        return execute(new AppendCommand(stringBuilder, i));
    }

    public UndoableStringBuilder append(char c) {
        return execute(new AppendCommand(stringBuilder, c));
    }

    public UndoableStringBuilder append(float f) {
        return execute(new AppendCommand(stringBuilder, f));
    }

    public UndoableStringBuilder append(double d) {
        return execute(new AppendCommand(stringBuilder, d));
    }

    public UndoableStringBuilder append(long lng) {
        return execute(new AppendCommand(stringBuilder, lng));
    }

    public UndoableStringBuilder append(boolean b) {
        return execute(new AppendCommand(stringBuilder, b));
    }

    public UndoableStringBuilder append(char[] str) {
        return execute(new AppendCommand(stringBuilder, str));
    }

    public UndoableStringBuilder append(Object obj) {
        return execute(new AppendCommand(stringBuilder, obj));
    }

    public UndoableStringBuilder append(String str) {
        return execute(new AppendCommand(stringBuilder, str));
    }

    public UndoableStringBuilder append(CharSequence s) {
        return execute(new AppendCommand(stringBuilder, s));
    }

    public UndoableStringBuilder append(StringBuffer sb) {
        return execute(new AppendCommand(stringBuilder, sb));
    }

    public UndoableStringBuilder append(char[] str, int offset, int len) {
        return execute(new AppendCommand(stringBuilder, str, offset, len));
    }

    public UndoableStringBuilder append(CharSequence s, int start, int end) {
        return execute(new AppendCommand(stringBuilder, s, start, end));
    }

    public UndoableStringBuilder appendCodePoint(int codePoint) {
        return execute(new AppendCodePointCommand(stringBuilder, codePoint));
    }

    public UndoableStringBuilder delete(int start, int end) {
        return execute(new DeleteCommand(stringBuilder, start, end));
    }

    public UndoableStringBuilder deleteCharAt(int index) {
        return execute(new DeleteCharAtCommand(stringBuilder, index));
    }

    public UndoableStringBuilder reverse() {
        return execute(new ReverseCommand(stringBuilder));
    }

    public UndoableStringBuilder insert(int offset, int i) {
        return execute(new InsertCommand(stringBuilder, offset, i));
    }

    public UndoableStringBuilder insert(int offset, char c) {
        return execute(new InsertCommand(stringBuilder, offset, c));
    }

    public UndoableStringBuilder insert(int offset, long l) {
        return execute(new InsertCommand(stringBuilder, offset, l));
    }

    public UndoableStringBuilder insert(int offset, float f) {
        return execute(new InsertCommand(stringBuilder, offset, f));
    }

    public UndoableStringBuilder insert(int offset, double d) {
        return execute(new InsertCommand(stringBuilder, offset, d));
    }

    public UndoableStringBuilder insert(int offset, boolean b) {
        return execute(new InsertCommand(stringBuilder, offset, b));
    }

    public UndoableStringBuilder insert(int offset, char[] str) {
        return execute(new InsertCommand(stringBuilder, offset, str));
    }

    public UndoableStringBuilder insert(int offset, Object obj) {
        return execute(new InsertCommand(stringBuilder, offset, obj));
    }

    public UndoableStringBuilder insert(int offset, String str) {
        return execute(new InsertCommand(stringBuilder, offset, str));
    }

    public UndoableStringBuilder insert(int dstOffset, CharSequence s) {
        return execute(new InsertCommand(stringBuilder, dstOffset, s));
    }

    public UndoableStringBuilder insert(int index, char[] str, int offset, int len) {
        return execute(new InsertCommand(stringBuilder, index, str, offset, len));
    }

    public UndoableStringBuilder insert(int dstOffset, CharSequence s, int start, int end) {
        return execute(new InsertCommand(stringBuilder, dstOffset, s, start, end));
    }

    public UndoableStringBuilder replace(int start, int end, String str) {
        return execute(new ReplaceCommand(stringBuilder, start, end, str));
    }

    public UndoableStringBuilder setCharAt(int index, char ch) {
        return execute(new SetCharAtCommand(stringBuilder, index, ch));
    }

    public UndoableStringBuilder setLength(int newLength) {
        return execute(new SetLengthCommand(stringBuilder, newLength));
    }

    public UndoableStringBuilder undo() {
        if (!history.isEmpty()) {
            stringBuilder = history.pop().undo();
        }
        return this;
    }

    public UndoableStringBuilder execute(Command command) {
        command.execute();
        history.push(command);
        return this;
    }

    @Override
    public int length() {
        return stringBuilder.length();
    }

    @Override
    public String toString() {
        return stringBuilder.toString();
    }
}
