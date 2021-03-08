package com.java;


public class Main {

    public static void main(String[] args) {
    	System.out.println("Дано натуральное число 12. Выведите все числа от 1 до 12.");
		int n = 12;
		OneToN.test(n);

		System.out.println("\nСравнение двоичного поиска и линейного:");
	    SearchComparator.test();

	    System.out.println("\nНайдите корень уравнения на отрезке [0;10] с точностью по x не хуже 0.001.");
	    double a = 0;
		double b = 10;
		double dev = 0.001;

		EquationSolver.test(x -> x * (x + 5) - 20, a, b, dev);

		System.out.println("\nДвоичное дерево поиска:");
		binaryTreeSearchTest();
    }

    public static void binaryTreeSearchTest() {
    	BinarySearchTree bst = new BinarySearchTree();
		bst.add(8);
		bst.add(3);
		bst.add(6);
		bst.add(1);
		bst.add(10);
		bst.add(14);
		bst.add(13);
		bst.add(4);
		bst.add(7);
		bst.add(5);
		/*
		        8
               / \
              3   10
             / \    \
            1   6    14
               / \   /
              4   7 13
               \
                5
		*/
		bst.preorder();
		bst.inorder();
		bst.postorder();

		System.out.println("\n6 in bst: " + bst.find(6));
		System.out.println("9 in bst: " + bst.find(9));

		System.out.println("\nУдаление 3\n");
		bst.remove(3);
		/*
		        8
               / \
              4   10
             / \    \
            1   6    14
               / \   /
              5   7 13
		*/
		bst.preorder();
		bst.inorder();
		bst.postorder();
	}

}
