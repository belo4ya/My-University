# 4*. Дано слово, состоящее только из строчных латинских букв.
# Проверьте, является ли это слово палиндромом. Выведите YES или NO.
# При решении этой задачи нельзя пользоваться циклами
# и нельзя использовать срезы с шагом, отличным от 1


# Вариант 1
def foo(w):
    if len(w) < 2:
        print('YES')
        return
    if w[0] != w[-1]:
        print('NO')
        return
    foo(w[1:-1])


# Вариант 2
def bar(w, i=-1, nw=''):
    if w == nw:
        print('YES')
    elif len(nw) < len(w):
        bar(w, i-1, nw=nw+w[i])
    else:
        print('NO')


word = str(input('Введите слово:\n>>> '))
bar(word)
foo(word)
