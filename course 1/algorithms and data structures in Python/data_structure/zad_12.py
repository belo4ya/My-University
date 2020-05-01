# Пусть элементы списка/массива хранят символы предложения. Замените каждое вхождение слова
# "itmathrepetitor" на "silence".

import array as ar

from additions.tester import time_test, memory_test


@time_test
def foo(subj):
    res = subj[:]
    for i in range(len(subj)-14):
        if ''.join(subj[i:i+15]) == 'itmathrepetitor':
            res[i:i+15] = ar.array('u', 'silence&&&&&&&&')
    for i in range(len(subj)-7):
        if ''.join(res[i:i + 8]) == '&&&&&&&&':
            for _ in range(8):
                res.pop(i)
    return res


if __name__ == '__main__':
    s = "I don't know what itmathrepetitor is and so I'm a itmathrepetitor!"
    a = [i for i in s]
    b = ar.array('u', s)
    # c = np.array(a)
    for i in [a, b]:
        memory_test(i)
        result = foo(i)
        print()
    print('result =', result)
    print('post_res = ', ''.join(result))
