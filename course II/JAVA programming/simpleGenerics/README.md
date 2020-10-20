## Знакомство с Genegic'ами

Создать метод *filter*, который применяет переданную lambda-функцию к переданному массиву.

Создать метод *fill*, который заполняет переданный массив на основании переданной lambda-функции.

## Демонстрация

```
String[] strings = new String[] {"Длинная строка", "строка", "стр"};
System.out.println(Arrays.toString(
        filter(strings, s -> s.length() > 3)
));

String[] strings1 = new String[100];
System.out.println(Arrays.toString(
        fill(strings1, s -> s + "!")
));
```

> [Длинная строка, строка]
> [0!, 1!, 2!, 3!, 4!, 5!, 6!, 7!, 8!, 9!, 10! ... ]
