package philosophers;

public class Forks {
    private boolean[] used = {false, false, false, false, false};

    public synchronized void takeFork() {
        Philosopher p = (Philosopher) Thread.currentThread();
        int id = p.id;
        while(used[id] || used[(id + 1) % 5]) {
            try {
                wait();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        System.out.println("Философ " + id + " сел за стол : взял вилки!");
        used[id] = true;
        used[(id + 1) % 5] = true;
    }

    public synchronized void putFork() {
        Philosopher p = (Philosopher) Thread.currentThread();
        int id = p.id;
        System.out.println("Философ " + id + " : положил вилки! Вышел из-за стола");
        used[id] = false;
        used[(id + 1) % 5] = false;
        notifyAll();
    }
}
