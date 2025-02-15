"""
Функция Эйлера, φ(n) [иногда ее называют фи-функцией] используется для определения количества чисел, меньших n,
которые взаимно просты с n. К примеру, т.к. 1, 2, 4, 5, 7 и 8 меньше девяти и взаимно просты с девятью, φ(9) = 6.
Число 1 считается взаимно простым для любого положительного числа, так что φ(1) = 1.

Интересно, что φ(87109) = 79180, и, как можно заметить, 87109 является перестановкой 79180.

Найдите такое значение n, 1<n<10^7, при котором φ(n) является перестановкой n, а отношение n/φ(n) является минимальным.

  №       Время  Замедление      Аргумент    Результат
---  ----------  ------------  ----------  -----------
  1   0.0731314  7.313%            100000        75841
  2   0.956609   88.348%          1000000       783169
  3  10.4914     953.475%        10000000      8319823
"""
from typing import List


def get_totients(limit: int) -> List[int]:
    """
    Calculates a list of totients from 0 to `limit` exclusive, using the
    definition of Euler's product formula.

    >>> get_totients(5)
    [0, 1, 1, 2, 2]
    >>> get_totients(10)
    [0, 1, 1, 2, 2, 4, 2, 6, 4, 6]
    """
    phi = list(range(limit + 1))

    for p in range(2, len(phi)):
        if phi[p] == p:  # p is prime
            for i in range(p, limit + 1, p):
                phi[i] -= phi[i] // p
    return phi


def has_same_digits(num1: int, num2: int) -> bool:
    """
    Return True if `num1` and `num2` have the same frequency of every digit, False otherwise.

    >>> has_same_digits(123456789, 987654321)
    True
    >>> has_same_digits(1234566, 123456)
    False
    """
    return sorted(str(num1)) == sorted(str(num2))


def solution(limit=10 ** 7):
    """
    Находит такое значение n, 1 < n < `limit`, при котором φ(n) является
    перестановкой n, а отношение n/φ(n) является минимальным.

    >>> solution(100)
    21
    >>> solution(10000)
    4435
    """
    min_numerator = 1
    min_denominator = 0
    totients = get_totients(limit)

    for i in range(2, limit):
        phi_i = totients[i]
        if (i * min_denominator < min_numerator * phi_i and
                has_same_digits(i, phi_i)):
            min_numerator = i
            min_denominator = phi_i
    return min_numerator


if __name__ == '__main__':
    ### Run Time-Profile Table ###
    import sys; sys.path.append('..')
    from time_profile import TimeProfile
    TimeProfile(solution, [10**5, 10**6, 10**7])
