package com.java;

import com.java.StringBuilder.UndoableStringBuilder;

public class Main {

    public static void main(String[] args) {
        UndoableStringBuilder bestStringBuilder = new UndoableStringBuilder("Работает!");

        System.out.println("\nUndoableStringBuilder bestStringBuilder = new UndoableStringBuilder(\"Работает!\");");
        System.out.println(bestStringBuilder);

        bestStringBuilder.replace(8, 9, "?");

        System.out.println("\nbestStringBuilder.replace(8, 9, \"?\");");
        System.out.println(bestStringBuilder);

        bestStringBuilder.append(' ').append("не");

        System.out.println("\nbestStringBuilder.append(' ').append(\"не\");");
        System.out.println(bestStringBuilder);

        bestStringBuilder.undo();
        bestStringBuilder.append("Не трогай");

        System.out.println("\nbestStringBuilder.undo(); bestStringBuilder.append(\"Не трогай\");");
        System.out.println(bestStringBuilder);

        bestStringBuilder.reverse();
        bestStringBuilder.undo();

        System.out.println("\nbestStringBuilder.reverse(); bestStringBuilder.undo();");
        System.out.println(bestStringBuilder);

        bestStringBuilder.appendCodePoint(33);

        System.out.println("\nbestStringBuilder.appendCodePoint(33);");
        System.out.println(bestStringBuilder);

        bestStringBuilder.replace(bestStringBuilder.length() - 1, bestStringBuilder.length(), ".");

        System.out.println("\nbestStringBuilder.replace(bestStringBuilder.length() - 1, " +
                "bestStringBuilder.length(), \".\");");
        System.out.println(bestStringBuilder);

        bestStringBuilder.undo().undo().undo().undo().undo();

        System.out.println("\nbestStringBuilder.undo().undo().undo().undo().undo();");
        System.out.println(bestStringBuilder.toString().toUpperCase());
    }
}
