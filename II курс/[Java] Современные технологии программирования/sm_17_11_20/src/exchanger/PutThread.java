package exchanger;

import java.util.concurrent.Exchanger;

public class PutThread implements Runnable {
    Exchanger<String> exchanger;
    String message;

    PutThread(Exchanger<String> ex) {
        this.exchanger = ex;
        message = "put message";
    }

    @Override
    public void run() {
        try {
            message = exchanger.exchange(message);
            System.out.println("PutThread " + message);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
