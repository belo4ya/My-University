## Задание

Реализовать класс обертку StringBuilder с поддержкой undo. Делегировать стандартные
методы стандартному StringBuilder.

**Паттерн «Команда»**

## Демонстрация

```
UndoableStringBuilder bestStringBuilder = new UndoableStringBuilder("Работает!");
Работает!

bestStringBuilder.replace(8, 9, "?");
Работает?

bestStringBuilder.append(' ').append("не");
Работает? не

bestStringBuilder.undo(); bestStringBuilder.append("Не трогай");
Работает? Не трогай

bestStringBuilder.reverse(); bestStringBuilder.undo();
Работает? Не трогай

bestStringBuilder.appendCodePoint(33);
Работает? Не трогай!

bestStringBuilder.replace(bestStringBuilder.length() - 1, bestStringBuilder.length(), ".");
Работает? Не трогай.

bestStringBuilder.undo().undo().undo().undo().undo();
РАБОТАЕТ!

Process finished with exit code 0
```

