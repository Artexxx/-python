"""
Постоянная Чамперноуна
Дана иррациональная десятичная дробь, образованная объединением положительных целых чисел:

0.12345678910{1}112131415161718192021...

Видно, что 12-ая цифра дробной части - 1.

Также дано, что d_n представляет собой n-ую цифру дробной части. Найдите значение следующего выражения:

d_1 × d_10 × d_100 × d_1000 × d_10000 × d_100000 × d_1000000
"""


def solution():
    """
    >>> solution()
    ... 210 # =>   PROD{1, 5, 3, 7, 2, 1, 210}
    """
    result_product = 1
    fraction = '0.' + ''.join([str(n) for n in range(1, 200000)])
    for power in range(2, 7):
        result_product *= int(fraction[10 ** power + 1])
    return result_product


if __name__ == '__main__':
    from timeit import default_timer
    start_time = default_timer()
    print(solution())
    print("Time: {:.5}ms".format(default_timer() - start_time))