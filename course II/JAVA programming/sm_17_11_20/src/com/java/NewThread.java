package com.java;

public class NewThread extends Thread {

    NewThread(String name) {
        super(name);
    }

    public void run() {
        System.out.printf("%s started\n", Thread.currentThread().getName());
        int counter = 1;
        while (!isInterrupted()) {
            System.out.println("Loop" + counter++);
            try {
                Thread.sleep(100);
            } catch (InterruptedException e) {
                System.out.printf("%s has been interrupted\n", Thread.currentThread().getName());
                interrupt();
            }
        }
        System.out.printf("Thread %s is finished\n", Thread.currentThread().getName());
    }
}
