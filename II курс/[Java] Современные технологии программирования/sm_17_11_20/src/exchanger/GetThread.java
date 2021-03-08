package exchanger;

import java.util.concurrent.Exchanger;

public class GetThread implements Runnable {
    Exchanger<String> exchanger;
    String message;

    GetThread(Exchanger<String> ex) {
        this.exchanger = ex;
        message = "get message";
    }

    @Override
    public void run() {
        try {
            message = exchanger.exchange(message);
            System.out.println("GetThread " + message);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
