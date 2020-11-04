"""
Двухосновные палиндромы
Десятичное число 585 = 1001001001 (в двоичной системе), является палиндромом по обоим основаниям.

Найдите сумму всех чисел меньше миллиона, являющихся палиндромами по основаниям 10 и 2.

(Пожалуйста, обратите внимание на то, что палиндромы не могут начинаться с нуля ни в одном из оснований).

  №       Время  Замедление        Число    Результат
---  ----------  ------------  ---------  -----------
  1   0.0022488  0.225%            10000        18228
  2   0.231982   22.97%          1000000       872187
  3  23.9195     2368.76%      100000000     39347399
"""


def is_double_base_palindrome(num: int) -> bool:
    """
    Возвращает True, если число `num` по основанию {10} и {2} является полиндромом.
    num (int) - натуральное число в 10 системе счисления
    >>> is_double_base_palindrome(585)
    ... True #585 = 1001001001 (binary)
    """
    num_str = str(num)
    bin_num_str = bin(num)[2:]
    return num_str == num_str[::-1] and bin_num_str == bin_num_str[::-1]


def solution(LIMIT=10 ** 6):
    """
    Возращает сумму двухосновныч палиндромов меньше миллиона.

    >>> solution(10**6)
    872187
    """
    return sum(n for n in range(3, LIMIT, 2)
               if is_double_base_palindrome(n)) + 1


if __name__ == '__main__':
    print(solution())
    # import sys; sys.path.append('..')
    # from time_profile import my_time_this
    # my_time_this(solution, [10**4, 10**6, 10**8])