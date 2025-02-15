"""
Треугольные, пятиугольные и шестиугольные числа вычисляются по нижеследующим формулам:

Треугольные	 	T(n) = n(n+1)/2 	1, 3, 6, 10, 15, ...
Пятиугольные	P(n) = n(3n-1)/2 	1, 5, 12, 22, 35, ...
Шестиугольные	H(n) = n(2n-1) 	 	1, 6, 15, 28, 45, ...

Можно убедиться в том, что T(285)= P(165) = H(143) = 40755.

Найдите следующее треугольное число, являющееся также пятиугольным и шестиугольным.

  №      Время  Замедление      Аргумент       Результат
---  ---------  ------------  ----------  --------------
  1  6.85e-05   0.007%                 1           40755
  2  0.0133499  1.328%             40755      1533776805 (Ответ)
  3  2.89455    288.120%      1533776805  57722156241751
"""
from itertools import count


def generate_pentagonal():
    for n in count():
        yield (n * ((3 * n) - 1)) // 2


def generate_hexagonal():
    for n in count():
        yield n * ((2 * n) - 1)


def is_triangle(num):
    n = ((1 + 8 * num) ** 0.5 - 1) / 2
    return n.is_integer()


def solution(low_limit=40755):
    """
    Возвращает следующее треугольное число, являющееся также пятиугольным и шестиугольным.

    >>> solution()
    1533776805
    """
    hexagonal = generate_hexagonal()
    pentagonal = generate_pentagonal()
    h = next(hexagonal)
    p = next(pentagonal)

    while True:
        while p < h:
            p = next(pentagonal)
        if p == h and p > low_limit and is_triangle(p):
            return p
        h = next(hexagonal)


if __name__ == '__main__':
    ### Run Time-Profile Table ###
    import sys; sys.path.append('..')
    from time_profile import TimeProfile
    TimeProfile(solution, [1, 40755, 1533776805])
