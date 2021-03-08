package com.java;

public class CountThread implements Runnable {
    CommonResource res;

    CountThread(CommonResource res) {
        this.res = res;
    }

    @Override
    public void run() {
        res.increment();
    }
}
