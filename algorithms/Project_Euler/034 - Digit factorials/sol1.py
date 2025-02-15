"""
Факториалы цифр
145 является любопытным числом, поскольку 1! + 4! + 5! = 1 + 24 + 120 = 145.

Найдите сумму всех чисел, каждое из которых равно сумме факториалов своих цифр.

Примечание: поскольку 1! = 1 и 2! = 2 не являются суммами, учитывать их не следует.
"""

factorials = {'0': 1, '1': 1, '2': 2, '3': 6, '4': 24, '5': 120, '6': 720, '7': 5040, '8': 40320, '9': 362880}


def solution():
    """
    Возвращает сумму всех чисел, равных сумме факториалов своих цифр.

    >>> solution()
    40730
    """
    sfd = lambda n: sum(factorials[c] for c in str(n))
    return sum(i for i in range(10, 1499999) if sfd(i) == i)


if __name__ == '__main__':
    from timeit import default_timer
    start_time = default_timer()
    print(solution())
    print("Time: {:.3}ms".format(default_timer() - start_time))