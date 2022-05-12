package com.java;

abstract class Car {
    private String color;
    private double speed;
    private int transmissionType;  // поменять на byte
    private double currentSpeed;
    private double price;

    public Car(String color, double speed, int transmissionType, double currentSpeed, double price) {
        this.color = color;
        this.speed = speed > 0 ? speed : 0;
        this.transmissionType = transmissionType == 1 ? transmissionType : 0;  // 0 - механика, 1 - автомат
        this.currentSpeed = currentSpeed > 0 && currentSpeed <= this.speed ? currentSpeed : 0;
        this.price = price > 0 ? price : 0;
    }

    public void start() {
        if (this.currentSpeed == 0) {
            this.speed = 20;
        }
    }

    public void stop() {
        this.currentSpeed = 0;
    }

    public void accelerate(int speed) {
        if (this.currentSpeed + speed <= this.speed) {
            this.currentSpeed += speed;
        }
    }

    public String getColor() {
        return color;
    }

    public double getSpeed() {
        return speed;
    }

    public int getTransmissionType() {
        return transmissionType;
    }

    public double getCurrentSpeed() {
        return currentSpeed;
    }

    public double getPrice() {
        return price;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public void setCurrentSpeed(double currentSpeed) {
        this.currentSpeed = currentSpeed <= this.speed ? currentSpeed : this.currentSpeed;
    }

    public void setPrice(double price) {
        this.price = price > 0 ? price : this.price;
    }

    public void setSpeed(double speed) {
        this.speed = speed > 0 ? speed : this.speed;;
    }

    public void setTransmissionType(int transmissionType) {
        this.transmissionType = transmissionType;
    }

    @Override
    public String toString() {
        return "Car{" +
                "color='" + color + '\'' +
                ", speed=" + speed +
                ", transmissionType=" + transmissionType +
                ", currentSpeed=" + currentSpeed +
                ", price=" + price +
                '}';
    }
}
