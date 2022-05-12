# 10. Даны числа a и b. Определите, сколько существует последовательностей
# из a нулей и b единиц, в которых никакие два нуля не стоят рядом


def foo(a, b):
    new_one = b - 1
    new_oh = a - 1
    if a > b + 1:
        return 0
    elif a == 0:
        return 1
    elif b == 0:
        return 1
    else:
        return foo(a, new_one) + foo(new_oh, new_one)


a = int(input('a (кол-во нулей) = '))
b = int(input('b (кол-во единиц) = '))
print(foo(a, b))
