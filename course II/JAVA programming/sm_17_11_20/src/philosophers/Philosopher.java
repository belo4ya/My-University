package philosophers;

public class Philosopher extends Thread {
    private int thinkingtimes = 0;
    private int eatingtimes = 0;
    int id;
    static int currentid = 0;
    private Forks fork;

    public Philosopher(Forks fork) {
        id = currentid;
        currentid++;
        this.fork = fork;
    }

    public void run() {
        while(true) {
            thinking();
            fork.takeFork();
            eating();
            fork.putFork();
        }
    }

    private void thinking() {
        thinkingtimes++;
        System.out.println("Философ " + id + " : начал думать!  Счетчик : " + thinkingtimes);
        try {
            sleep(1000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    private void eating()
    {
        eatingtimes++;
        System.out.println("Философ " + id + " : начал есть!  Счетчик : " + eatingtimes);
        try {
            sleep(1000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
