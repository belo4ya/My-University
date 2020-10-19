## Задание

Написать класс StringBuilder с оповещением других объектов-слушателей об изменении
своего состояния. Делегировать стандартные методы стандартному StringBuilder.

**Паттерн «Наблюдатель»**

## Демонстрация

```
// Создаем новый StringBuilder
PublicStringBuilder bestStringBuilder = new PublicStringBuilder("Поехали!");

// Включаем логгирование для тех операций, которые нам нужны
bestStringBuilder.activateLogging(new LoggingListener("log.txt"),
        EventType.append, EventType.appendCodePoint, EventType.delete,
        EventType.deleteCharAt, EventType.insert, EventType.replace,
        EventType.reverse, EventType.setCharAt, EventType.setLength);

bestStringBuilder.replace(bestStringBuilder.length() - 1, bestStringBuilder.length(), "  |");
bestStringBuilder.reverse();
bestStringBuilder.append("  ");
bestStringBuilder.append('|');
bestStringBuilder.reverse();
```

> ----TIME----   ----COMMAND----   ----STRING----
> 0:10:32:780    create            Поехали!      
> 0:10:32:808    replace           Поехали  |    
> 0:10:32:808    reverse           |  илахеоП    
> 0:10:32:809    append            |  илахеоП    
> 0:10:32:810    append            |  илахеоП  | 
> 0:10:32:810    reverse           |  Поехали  | 

