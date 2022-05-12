package com.java;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;

abstract public class Menu {
    protected HashSet<Product> products;
    protected ArrayList<Product> stopList = new ArrayList<>();

    public Menu(Product... products) {
        this.products = new HashSet<>(Arrays.asList(products));
    }

    public HashSet<Product> getProducts() {
        return products;
    }

    public ArrayList<Product> getStopList() {
        return stopList;
    }

    public Product getProduct(Product product) {
        if (products.contains(product)) {
            for (Product p : products) {
                if (p.equals(product)) {
                    return p;
                }
            }
        }
        return null;
    }

    public void addProduct(Product product) {
        if (products.contains(product)) {
            for (Product p : products) {
                if (p.equals(product)) {
                    p.updateAmount(p.getAmount() + product.getAmount());
                }
            }
        } else {
            this.products.add(product);
        }
    }

    public void removeProduct(Product product) {
        this.products.remove(product);
    }

    public void addProductToStopList(Product product) {
        this.stopList.add(product);
        this.products.remove(product);
    }

    public void removeProductOutOfStopList(Product product) {
        this.stopList.remove(product);
        this.products.add(product);
    }

    public ArrayList<Product> getSoldProducts() {
        ArrayList<Product> soldProducts = new ArrayList<>();
        for (Product p : products) {
            if (p.getAmount() == 0) {
                soldProducts.add(p);
            }
        }
        return soldProducts;
    }

    public Product orderProduct(String name) {
        for (Product p : products) {
            if (name.equals(p.getName())) {
                if (p.getAmount() > 0) {
                    p.decrementAmount();
                    return new Product(p);
                }
            }
        }
        return null;
    }

    @Override
    public String toString() {
        return "Menu{" +
                "products=" + products +
                ", stopList=" + stopList +
                '}';
    }
}
