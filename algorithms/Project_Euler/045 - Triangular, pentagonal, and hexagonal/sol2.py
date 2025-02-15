"""
Треугольные, пятиугольные и шестиугольные числа вычисляются по нижеследующим формулам:

Треугольные	 	T(n) = n(n+1)/2 	1, 3, 6, 10, 15, ...
Пятиугольные	P(n) = n(3n-1)/2 	1, 5, 12, 22, 35, ...
Шестиугольные	H(n) = n(2n-1) 	 	1, 6, 15, 28, 45, ...

Можно убедиться в том, что T(285)= P(165) = H(143) = 40755.

Найдите следующее треугольное число, являющееся также пятиугольным и шестиугольным.

    Время  Замедление         Число       Результат
---------  ------------  ----------  --------------
5.28e-05   0.005%                 1           40755
0.0097281  0.968%             40755      1533776805  (Ответ)
1.92689    191.716%      1533776805  57722156241751
"""


def generate_polygonal(type_number):
    """Генерирует фиругные числа

    >>> generate_polygonal(type_number=3)
    1 3 6 10 15 21 28 36  [...]
    >>> generate_polygonal(type_number=4)
    1 4 9 16 25 36 49 64  [...]
    """
    c = type_number - 2
    a = b = 1
    while True:
        yield a
        b += c
        a += b


def is_triangle(num):
    n = ((1 + 8 * num) ** 0.5 - 1) / 2
    return n.is_integer()


def solution(low_limit=40755):
    """
    Возвращает следующее треугольное число, являющееся также пятиугольным и шестиугольным.

    >>> solution()
    1533776805
    """
    hexagonal = generate_polygonal(type_number=6)
    pentagonal = generate_polygonal(type_number=5)
    h = next(hexagonal)
    p = next(pentagonal)

    while True:
        while p < h:
            p = next(pentagonal)
        if p == h and p > low_limit and is_triangle(p) :
            return p
        h = next(hexagonal)


if __name__ == '__main__':
    ### Run Time-Profile Table ###
    import sys; sys.path.append('..')
    from time_profile import TimeProfile
    TimeProfile(solution, [1, 40755, 1533776805], DynamicTimer=True)
