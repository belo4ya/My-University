# 2. Дано натуральное число N. Выведите слово YES, если число N
# является точной степенью двойки, или слово NO в противном случае.
# Операцией возведения в степень пользоваться нельзя!


# Вариант 1
def foo(n, i=1):
    if n == i:
        print('YES')
    elif i > n:
        print('NO')
    else:
        foo(n, i*2)


# Вариант 2
def bar(n):
    if n == int(n) == 1:
        print('YES')
    elif n != int(n):
        print('NO')
    else:
        bar(n / 2)


n = int(input('n = '))
foo(n)
bar(n)
