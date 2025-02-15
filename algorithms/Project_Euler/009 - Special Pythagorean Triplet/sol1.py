"""
Пифагорова Тройка - три натуральных числа a < b < c, для которых выполняется равенство a^2 + b^2 = c^2

Одна такая тройка - 3, 4, 5. Для этой задачи будет дано значение 12 в качестве аргумента функции, а затем она вернет 60.
3^2 + 4^2 = 5^2 так как 9 + 16 = 25 и тогда их произведение (3 * 4 * 5) - это 60.

Найдите произведение a,b,c такое, что a + b + c = N.


  №      Время  Замедление      Число    Результат
---  ---------  ------------  -------  -----------
  1  1.25e-05   0.001%             12           60
  2  0.0044432  0.44%             234       453960
  3  0.0649851  6.05%            1000     31875000
  4  6.67482    660.98%         10000  31875000000
"""


def solution(pyth_sum):
    """Возвращает произведение чисел a,b,c, удовлетворяющих условиям:
     1. a < b < c
     2. a**2 + b**2 = c**2
     3. a + b + c = pyth_sum

    >>> solution(12)
    60
    >>> solution(1000)
    31_875_000
    """
    for a in range(1, int((pyth_sum-3) / 3) + 1):
        for b in range(a + 1, int(2*(pyth_sum-3) / 3) + 1):
            c1 = pyth_sum - (a + b)
            c2 = (a ** 2 + b ** 2) ** 0.5
            if c1 == c2:
                # print(a, b, c1, sep=" * ")
                return a * b * c1
    return "Ответа не найдено"


if __name__ == "__main__":
    print(solution(int(input())))
    # ### Run Time-Profile Table ###
    # import sys; sys.path.append('..')
    # from time_profile import my_time_this
    # my_time_this(solution, [12, 234, 1000, 10000])



