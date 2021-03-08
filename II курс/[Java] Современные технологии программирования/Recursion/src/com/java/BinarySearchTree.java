package com.java;

public class BinarySearchTree {
    private Node root;

    BinarySearchTree() {
        root = null;
    }

    public boolean find(int data) {
        return search(this.root, data);
    }

    public void add(int data) {
        this.root = insert(this.root, data);
    }

    public void remove(int data) {
        this.root = delete(this.root, data);
    }

    public void preorder() {
        System.out.println("Прямой (префиксный) обход:");
        preOrder(this.root);
        System.out.println();
    }

    public void postorder() {
        System.out.println("Концевой (постфиксный) обход:");
        postOrder(this.root);
        System.out.println();
    }

    public void inorder() {
        System.out.println("Обратный (инфиксный) обход:");
        inOrder(this.root);
        System.out.println();
    }

    private boolean search(Node node, int data) {
        if (node == null) {
            return false;
        } else if (node.data == data) {
            return true;
        } else if (node.data > data) {
            return search(node.left, data);
        } else {
            return search(node.right, data);
        }
    }

    private Node insert(Node node, int data) {
        if (node == null) {
            node = new Node(data);
        } else if (node.data > data) {
            node.left = insert(node.left, data);
        } else if (node.data < data) {
            node.right = insert(node.right, data);
        }
        return node;
    }

    private Node delete(Node node, int data) {
        if (node == null) {
            System.out.println("Нет такого значения");
        } else if (node.data > data) {
            node.left = delete(node.left, data);
        } else if (node.data < data) {
            node.right = delete(node.right, data);
        } else {
            if (node.right == null && node.left == null) { // если это лист
                node = null;
            } else if (node.left == null) { // если только правый узел
                Node temp = node.right;
                node.right = null;
                node = temp;
            } else if (node.right == null) { // если только левый узел
                Node temp = node.left;
                node.left = null;
                node = temp;
            } else { // если два дочерних узла
                Node temp = node.right;
                // поиск крайнего левого дочернего узла правого поддерево
                while (temp.left != null) {
                    temp = temp.left;
                }
                node.data = temp.data;
                node.right = delete(node.right, temp.data);
            }
        }
        return node;
    }

    private void preOrder(Node node) {
        if (node == null) {
            return;
        }
        System.out.print(node.data + " ");
        if (node.left != null) {
            preOrder(node.left);
        }
        if (node.right != null) {
            preOrder(node.right);
        }
    }

    private void postOrder(Node node) {
        if (node == null) {
            return;
        }
        if (node.left != null) {
            postOrder(node.left);
        }
        if (node.right != null) {
            postOrder(node.right);
        }
        System.out.print(node.data + " ");
    }

    private void inOrder(Node node) {
        if (node == null) {
            return;
        }
        if (node.left != null) {
            inOrder(node.left);
        }
        System.out.print(node.data + " ");
        if (node.right != null) {
            inOrder(node.right);
        }
    }

    private static class Node {
        int data;
        Node left;
        Node right;

        Node(int d) {
            data = d;
            left = null;
            right = null;
        }
    }
}
