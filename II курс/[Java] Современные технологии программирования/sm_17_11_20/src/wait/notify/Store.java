package wait.notify;

public class Store {
    private int product = 0;

    public synchronized void get() {
        while (product < 1) {
            try {
                wait();
            } catch (InterruptedException e) {

            }
        }
        product--;
        System.out.println("Клиент купил один товар");
        System.out.println("Товаров на складе " + product);
        notify();
    }

    public synchronized void put() {
        while (product >= 3) {
            try {
                wait();
            } catch (InterruptedException e) {

            }
        }
        product++;
        System.out.println("Добавили товар");
        System.out.println("Товаров на складе " + product);
        notify();
    }
}
