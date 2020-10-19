package com.java.StringBuilder;

import java.util.stream.IntStream;

public class PublicStringBuilder
        implements java.io.Serializable, Comparable<StringBuilder>, CharSequence
{
    private StringBuilder stringBuilder;
    private EventManager eventManager = new EventManager(
            EventType.create,
            EventType.append, EventType.appendCodePoint, EventType.delete,
            EventType.deleteCharAt, EventType.insert, EventType.replace,
            EventType.reverse, EventType.setCharAt, EventType.setLength
    );

    public PublicStringBuilder() {
        stringBuilder = new StringBuilder();
    }

    public PublicStringBuilder(int capacity) {
        stringBuilder = new StringBuilder(capacity);
    }

    public PublicStringBuilder(CharSequence seq) {
        stringBuilder = new StringBuilder(seq);
    }

    public PublicStringBuilder(String str) {
        stringBuilder = new StringBuilder(str);
    }

    // event management
    public void activateLogging(EventListener logger, EventType... events) {
        eventManager.subscribe(EventType.create, logger);

        for (EventType event: events) {
            eventManager.subscribe(event, logger);
        }

        eventManager.notify(EventType.create, stringBuilder.toString());
    }

    // тут могут быть exceptions
    public void deactivateLogging(EventListener logger, EventType... events) {
        eventManager.unsubscribe(EventType.create, logger);

        for (EventType event: events) {
            eventManager.unsubscribe(event, logger);
        }
    }
    // ----------------

    public PublicStringBuilder append(int i) {
        stringBuilder.append(i);
        eventManager.notify(EventType.append, stringBuilder.toString());
        return this;
    }

    public PublicStringBuilder append(char c) {
        stringBuilder.append(c);
        eventManager.notify(EventType.append, stringBuilder.toString());
        return this;
    }

    public PublicStringBuilder append(float f) {
        stringBuilder.append(f);
        eventManager.notify(EventType.append, stringBuilder.toString());
        return this;
    }

    public PublicStringBuilder append(double d) {
        stringBuilder.append(d);
        eventManager.notify(EventType.append, stringBuilder.toString());
        return this;
    }

    public PublicStringBuilder append(long lng) {
        stringBuilder.append(lng);
        eventManager.notify(EventType.append, stringBuilder.toString());
        return this;
    }

    public PublicStringBuilder append(boolean b) {
        stringBuilder.append(b);
        eventManager.notify(EventType.append, stringBuilder.toString());
        return this;
    }

    public PublicStringBuilder append(char[] str) {
        stringBuilder.append(str);
        eventManager.notify(EventType.append, stringBuilder.toString());
        return this;
    }

    public PublicStringBuilder append(Object obj) {
        stringBuilder.append(obj);
        eventManager.notify(EventType.append, stringBuilder.toString());
        return this;
    }

    public PublicStringBuilder append(String str) {
        stringBuilder.append(str);
        eventManager.notify(EventType.append, stringBuilder.toString());
        return this;
    }

    public PublicStringBuilder append(CharSequence s) {
        stringBuilder.append(s);
        eventManager.notify(EventType.append, stringBuilder.toString());
        return this;
    }

    public PublicStringBuilder append(StringBuffer sb) {
        stringBuilder.append(sb);
        eventManager.notify(EventType.append, stringBuilder.toString());
        return this;
    }

    public PublicStringBuilder append(char[] str, int offset, int len) {
        stringBuilder.append(str, offset, len);
        eventManager.notify(EventType.append, stringBuilder.toString());
        return this;
    }

    public PublicStringBuilder append(CharSequence s, int start, int end) {
        stringBuilder.append(s, start, end);
        eventManager.notify(EventType.append, stringBuilder.toString());
        return this;
    }

    public PublicStringBuilder appendCodePoint(int codePoint) {
        stringBuilder.appendCodePoint(codePoint);
        eventManager.notify(EventType.appendCodePoint, stringBuilder.toString());
        return this;
    }

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

    public PublicStringBuilder delete(int start, int end) {
        stringBuilder.delete(start, end);
        eventManager.notify(EventType.delete, stringBuilder.toString());
        return this;
    }

    public PublicStringBuilder deleteCharAt(int index) {
        stringBuilder.deleteCharAt(index);
        eventManager.notify(EventType.deleteCharAt, stringBuilder.toString());
        return this;
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

    public PublicStringBuilder insert(int offset, int i) {
        stringBuilder.insert(offset, i);
        eventManager.notify(EventType.insert, stringBuilder.toString());
        return this;
    }

    public PublicStringBuilder insert(int offset, char c) {
        stringBuilder.insert(offset, c);
        eventManager.notify(EventType.insert, stringBuilder.toString());
        return this;
    }

    public PublicStringBuilder insert(int offset, long l) {
        stringBuilder.insert(offset, l);
        eventManager.notify(EventType.insert, stringBuilder.toString());
        return this;
    }

    public PublicStringBuilder insert(int offset, float f) {
        stringBuilder.insert(offset, f);
        eventManager.notify(EventType.insert, stringBuilder.toString());
        return this;
    }

    public PublicStringBuilder insert(int offset, double d) {
        stringBuilder.insert(offset, d);
        eventManager.notify(EventType.insert, stringBuilder.toString());
        return this;
    }

    public PublicStringBuilder insert(int offset, boolean b) {
        stringBuilder.insert(offset, b);
        eventManager.notify(EventType.insert, stringBuilder.toString());
        return this;
    }

    public PublicStringBuilder insert(int offset, char[] str) {
        stringBuilder.insert(offset, str);
        eventManager.notify(EventType.insert, stringBuilder.toString());
        return this;
    }

    public PublicStringBuilder insert(int offset, Object obj) {
        stringBuilder.insert(offset, obj);
        eventManager.notify(EventType.insert, stringBuilder.toString());
        return this;
    }

    public PublicStringBuilder insert(int offset, String str) {
        stringBuilder.insert(offset, str);
        eventManager.notify(EventType.insert, stringBuilder.toString());
        return this;
    }

    public PublicStringBuilder insert(int dstOffset, CharSequence s) {
        stringBuilder.insert(dstOffset, s);
        eventManager.notify(EventType.insert, stringBuilder.toString());
        return this;
    }

    public PublicStringBuilder insert(int index, char[] str, int offset, int len) {
        stringBuilder.insert(index, str, offset, len);
        eventManager.notify(EventType.insert, stringBuilder.toString());
        return this;
    }

    public PublicStringBuilder insert(int dstOffset, CharSequence s, int start, int end) {
        stringBuilder.insert(dstOffset, s, start, end);
        eventManager.notify(EventType.insert, stringBuilder.toString());
        return this;
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

    public PublicStringBuilder replace(int start, int end, String str) {
        stringBuilder.replace(start, end, str);
        eventManager.notify(EventType.replace, stringBuilder.toString());
        return this;
    }

    public PublicStringBuilder reverse() {
        stringBuilder.reverse();
        eventManager.notify(EventType.reverse, stringBuilder.toString());
        return this;
    }

    public PublicStringBuilder setCharAt(int index, char ch) {
        stringBuilder.setCharAt(index, ch);
        eventManager.notify(EventType.setCharAt, stringBuilder.toString());
        return this;
    }

    public PublicStringBuilder setLength(int newLength) {
        stringBuilder.setLength(newLength);
        eventManager.notify(EventType.setLength, stringBuilder.toString());
        return this;
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

    @Override
    public int length() {
        return stringBuilder.length();
    }

    @Override
    public String toString() {
        return stringBuilder.toString();
    }
}
