package com.java;

import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) {
        ArrayList<Employee> employees = new ArrayList<>();
        employees.add(new FullTimeEmployee("Homer Lester", 2100));
        employees.add(new FullTimeEmployee("Rudolf Parker", 1600));
        employees.add(new FullTimeEmployee("Blaze Holland", 1600));
        employees.add(new FullTimeEmployee("Justin Nelson", 1800));
        employees.add(new FullTimeEmployee("Vincent Brooks", 1800));
        employees.add(new PartTimeEmployee("Marvin Peters", 12));
        employees.add(new PartTimeEmployee("August Neal", 12));
        employees.add(new PartTimeEmployee("Lionel Ray", 12));
        employees.add(new PartTimeEmployee("Harold Pitts", 12));
        employees.add(new PartTimeEmployee("Douglas Hicks", 24));
        employees.add(new PartTimeEmployee("Roland Logan", 20));

        System.out.println("Сортировка по имени:");
        Collections.sort(employees);
        for (Employee employee: employees) {
            System.out.printf("%s: %.2f$\n", employee, employee.getPayroll());
        }

        System.out.println("\nСортировка по убыванию зарплаты:");
        employees.sort(new Comparator<Employee>() {
            @Override
            public int compare(Employee o1, Employee o2) {
                return (int) (o2.getPayroll() - o1.getPayroll());
            }
        });
        for (Employee employee: employees) {
            System.out.printf("%s: %.2f$\n", employee, employee.getPayroll());
        }

        System.out.println("\nСоставная сортировка - по убыванию зарплаты и в алфовитном порядке по имени:");
        employees.sort((o1, o2) -> (  // захотел применить тернарный оператор, а так бы я не стал нарушать границы! (точно)
                (int) (o2.getPayroll() - o1.getPayroll()) == 0 ? o1.getName().compareTo(o2.getName()) : (int) (o2.getPayroll() - o1.getPayroll()))
        );
        for (Employee employee: employees) {
            System.out.printf("%s: %.2f$\n", employee, employee.getPayroll());
        }

        System.out.println("\nПервые 5 имён работников из текущего списка");
        for (int i = 0; i < 5; i++) {
            System.out.println("Работник: " + employees.get(i).getName());
        }

        System.out.println("\nПоследние 3 id работников из текущего списка");
        for (int i = employees.size() - 1; i > employees.size() - 4; i--) {
            System.out.println("id: " + employees.get(i).getId());
        }

        // не совсем понял, что значит Последние 3 id и ещё раз решил применить искусство сортировки
        System.out.println("\nПоследние-последние 3 id работников из текущего списка");
        employees.sort((o1, o2) -> (int) (o2.getId() - o1.getId()));
        for (int i = 0; i < 3; i++) {
            System.out.println("id: " + employees.get(i).getId());
        }

        System.out.println("\nЗапишем в файл и прочитаем, что у нас получилось:");
        // сериализация коллекции и запись в файл
        String path = "employees.txt";
        try {
            FileOutputStream outputStream = new FileOutputStream(path);
            ObjectOutputStream objectOutputStream = new ObjectOutputStream(outputStream);

            objectOutputStream.writeObject(employees);
            objectOutputStream.close();
        } catch (IOException e) {
            e.printStackTrace();
        }

        // чтение из файла и десериализация
        ArrayList<?> newEmployees = null;
//        ArrayList<Employee> newEmployees = null;
        try {
            FileInputStream inputStream = new FileInputStream(path);
            ObjectInputStream objectInputStream = new ObjectInputStream(inputStream);

            newEmployees = (ArrayList<?>) objectInputStream.readObject();
//            newEmployees = (ArrayList<Employee>) objectInputStream.readObject();
            objectInputStream.close();
        } catch (IOException | ClassNotFoundException e) {
            e.printStackTrace();
        }

        assert newEmployees != null;
        System.out.println("newEmployees = " + newEmployees);
        System.out.println(newEmployees.getClass());
    }
}
