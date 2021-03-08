package wait.notify;

public class Producer implements Runnable {
    Store store;

    Producer(Store store) {
        this.store = store;
    }

    @Override
    public void run() {
        for (int i = 0; i < 10; i ++) {
            store.put();
        }
    }

}
