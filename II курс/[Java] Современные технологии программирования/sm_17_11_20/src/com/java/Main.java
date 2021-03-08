package com.java;

public class Main {

    public static void main(String[] args) {
        System.out.println("Main thread started...");
        CommonResource commonResource = new CommonResource();
        for (int i = 0; i < 5; i++) {
            Thread t = new Thread(new CountThread(commonResource), "Thread" + i);
            t.start();
        }
        System.out.println("Main thread finished");
    }
}
