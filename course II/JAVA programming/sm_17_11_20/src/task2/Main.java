package task2;

public class Main {

    public static void main(String[] args) {
        Object lock = new Object();
        new SyncThread(lock).start();
        new SyncThread(lock).start();
    }
}
