package com.java;

import com.java.StringBuilder.EventType;
import com.java.StringBuilder.LoggingListener;
import com.java.StringBuilder.PublicStringBuilder;

public class Main {

    public static void main(String[] args) {
        // Создаем новый StringBuilder
        PublicStringBuilder bestStringBuilder = new PublicStringBuilder("Поехали!");

        // Включаем логгирование для тех операций, которые нам нужны
        bestStringBuilder.activateLogging(new LoggingListener("log.txt"),
                EventType.append, EventType.appendCodePoint, EventType.delete,
                EventType.deleteCharAt, EventType.insert, EventType.replace,
                EventType.reverse, EventType.setCharAt, EventType.setLength);

        bestStringBuilder.replace(bestStringBuilder.length() - 1, bestStringBuilder.length(), "  |");
        bestStringBuilder.reverse();
        bestStringBuilder.append("  ");
        bestStringBuilder.append('|');
        bestStringBuilder.reverse();
    }
}
