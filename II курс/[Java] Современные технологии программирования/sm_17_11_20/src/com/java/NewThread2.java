package com.java;

public class NewThread2 implements Runnable {
    private boolean isActive;

    NewThread2() {
        isActive = true;
    }

    public void disable() {
        isActive = false;
    }

    @Override
    public void run() {
        System.out.printf("%s started\n", Thread.currentThread().getName());
        while (isActive) {
            try {
                Thread.sleep(200);
            } catch (InterruptedException e) {
                System.out.println("Thread is interrupted");
            }
        }

        System.out.printf("Thread %s is finished\n", Thread.currentThread().getName());
    }
}
