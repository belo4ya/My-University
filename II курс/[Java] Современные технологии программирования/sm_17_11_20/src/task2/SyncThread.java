package task2;

public class SyncThread extends Thread {
    private Object lock;

    SyncThread(Object lock) {
        this.lock = lock;
    }

    @Override
    public void run() {
        while (true) {
            synchronized (lock) {
                try {
                    System.out.println(getName());
                    lock.notify();
                    lock.wait();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        }
    }

}
