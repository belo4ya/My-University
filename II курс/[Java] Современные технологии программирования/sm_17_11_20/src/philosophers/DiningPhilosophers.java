package philosophers;

public class DiningPhilosophers {
    public static void main(String[] args) {
        Forks f = new Forks();
        new Philosopher(f).start();
        new Philosopher(f).start();
        new Philosopher(f).start();
        new Philosopher(f).start();
        new Philosopher(f).start();
    }
}
