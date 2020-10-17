library(stringi)  # подключает пакет package

from <- -6
to <- 6
by <- 0.5
print(seq(from, to, by = by))  # генерирует последовательность числел от from до to с шагом by

from <- -10
to <- 50
len <- 6
print(seq(from, to, len = len))  # генерирует последовательность числел от from до to длины len

x <- 7
times <- 3
rep(x, times)  # повторяет x ровно times раз

list("string", 12L, 12.2, FALSE, NULL)  # создаёт список объектов

x <- 1:10
rev(x)  # реверсирует порядок элементов

sort(x)  # сортирует элементы объекта по возрастанию

breaks <- 5
cut(x, breaks)  # делит вектор на равные интервалы

y <- seq(0, 9, by = 2)
match(y, x)  # ищет элементы x, которые есть в y

x <- rep(1:4, 5)
unique(x) # исключает из объекта повторяющиеся элементы