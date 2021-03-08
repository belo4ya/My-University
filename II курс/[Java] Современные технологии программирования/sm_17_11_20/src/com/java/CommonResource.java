package com.java;

public class CommonResource {
    int x = 1;

    synchronized void increment() {
        for(int i = 0; i < 5; i++) {
            System.out.printf("%s %d \n", Thread.currentThread().getName(), x);
            x++;
            try {
                Thread.sleep(100);
            } catch (InterruptedException e) {
                System.out.println("Thread is interrupted");
            }
        }
    }
}
