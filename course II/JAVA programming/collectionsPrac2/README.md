## Задание

Создать 3 класса(базовый и 2 предка) которые описывают некоторых работников с
почасовой оплатой (один из предков) и фиксированой оплатой (второй предок).
a. Описать в базовом классе абстрактный метод для расчета среднемесячной
зарплаты.
b. Для «почасовщиков» формула для расчета такая: «среднемесячная зарплата =
20.8*8*ставка в час»,
c. для работников с фиксированой оплатой «среднемесячная зарплата =
фиксированой месячной оплате».
i. a)Упорядочить всю последовательность рабочих по убыванию
среднемесячной зарплаты.
ii. При совпадении зарплаты – упорядочить данные в алфавитном порядке по
имени. Вывести идентификатор работника,
iii. имя и среднемесячную зарплату для всех елементов списка.
iv. b)Вывести первые 5 имен работников из полученого выше списка
(задача А).
v. c)Вывести последние 3 идентификаторы работников из полученого више
списка (задача А).
vi. d)Организовать запись и чтение колекции в/из файл(а)
vii. e)Организовать обработку некоректного формата входного файла


## Демонстрация

```
Сортировка по имени:
Employee{name='August Neal', id='7'}: 1996,80$
Employee{name='Blaze Holland', id='3'}: 1600,00$
Employee{name='Douglas Hicks', id='10'}: 3993,60$
Employee{name='Harold Pitts', id='9'}: 1996,80$
Employee{name='Homer Lester', id='1'}: 2100,00$
Employee{name='Justin Nelson', id='4'}: 1800,00$
Employee{name='Lionel Ray', id='8'}: 1996,80$
Employee{name='Marvin Peters', id='6'}: 1996,80$
Employee{name='Roland Logan', id='11'}: 3328,00$
Employee{name='Rudolf Parker', id='2'}: 1600,00$
Employee{name='Vincent Brooks', id='5'}: 1800,00$

Сортировка по убыванию зарплаты:
Employee{name='Douglas Hicks', id='10'}: 3993,60$
Employee{name='Roland Logan', id='11'}: 3328,00$
Employee{name='Homer Lester', id='1'}: 2100,00$
Employee{name='August Neal', id='7'}: 1996,80$
Employee{name='Harold Pitts', id='9'}: 1996,80$
Employee{name='Lionel Ray', id='8'}: 1996,80$
Employee{name='Marvin Peters', id='6'}: 1996,80$
Employee{name='Justin Nelson', id='4'}: 1800,00$
Employee{name='Vincent Brooks', id='5'}: 1800,00$
Employee{name='Blaze Holland', id='3'}: 1600,00$
Employee{name='Rudolf Parker', id='2'}: 1600,00$

Составная сортировка - по убыванию зарплаты и в алфовитном порядке по имени:
Employee{name='Douglas Hicks', id='10'}: 3993,60$
Employee{name='Roland Logan', id='11'}: 3328,00$
Employee{name='Homer Lester', id='1'}: 2100,00$
Employee{name='August Neal', id='7'}: 1996,80$
Employee{name='Harold Pitts', id='9'}: 1996,80$
Employee{name='Lionel Ray', id='8'}: 1996,80$
Employee{name='Marvin Peters', id='6'}: 1996,80$
Employee{name='Justin Nelson', id='4'}: 1800,00$
Employee{name='Vincent Brooks', id='5'}: 1800,00$
Employee{name='Blaze Holland', id='3'}: 1600,00$
Employee{name='Rudolf Parker', id='2'}: 1600,00$

Первые 5 имён работников из текущего списка
Работник: Douglas Hicks
Работник: Roland Logan
Работник: Homer Lester
Работник: August Neal
Работник: Harold Pitts

Последние 3 id работников из текущего списка
id: 2
id: 3
id: 5

Последние-последние 3 id работников из текущего списка
id: 11
id: 10
id: 9

Запишем в файл и прочитаем, что у нас получилось:
newEmployees = [Employee{name='Roland Logan', id='11'}, Employee{name='Douglas Hicks', id='10'}, Employee{name='Harold Pitts', id='9'}, Employee{name='Lionel Ray', id='8'}, Employee{name='August Neal', id='7'}, Employee{name='Marvin Peters', id='6'}, Employee{name='Vincent Brooks', id='5'}, Employee{name='Justin Nelson', id='4'}, Employee{name='Blaze Holland', id='3'}, Employee{name='Rudolf Parker', id='2'}, Employee{name='Homer Lester', id='1'}]
class java.util.ArrayList
```
