package com.java.transportCards;

abstract public class AbstractTravelCard {
    private static long counter = 100_000_000;
    private final long id;
    private int balance = 0;
    private final String ownerName;

    public AbstractTravelCard(String ownerName) {
        this.ownerName = ownerName;
        this.id = counter++;
    }

    public long getId() {
        return id;
    }

    public int getBalance() {
        return balance;
    }

    public String getOwnerName() {
        return ownerName;
    }

    abstract public void writeOff();

    public void addFundsFromPhone(int amount) {
        this.balance += amount;
    }

    public void addFundsFromAtm(int amount) {
        this.balance += amount;
    }
}
