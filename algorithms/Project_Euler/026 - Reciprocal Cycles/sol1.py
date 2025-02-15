"""
Единичная дробь имеет 1 в числителе.
Десятичные представления единичных дробей со знаменателями от 2 до 10 даны ниже:

 1/2 = 0.5
 1/3 = 0.(3)
 1/4 = 0.25
 1/5 = 0.2
 1/6 = 0.1(6)
 1/7 = 0.(142857)
 1/8 = 0.125
 1/9 = 0.(1)
 1/10 = 0.1

Где 0.1(6) значит 0.166666..., и имеет повторяющуюся последовательность из одной цифры. Заметим, что 1/7 имеет повторяющуюся последовательность из 6 цифр.

Найдите значение d < 1000, для которого 1/d в десятичном виде содержит самую длинную повторяющуюся последовательность цифр.


  №      Время  Замедление      Аргумент    Результат
---  ---------  ------------  ----------  -----------
  1  0.0085238  0.852%              1000          983 <Ответ>
  2  0.511187   50.266%            10000         9967
  3  4.13974    362.856%           30000        29989
"""
import itertools, sympy


def reciprocal_cycle_len1(d):
    # "Long division" until remainder is 1
    # finds next remainder (without actually doing long division)
    L = 1  # Repteated part startes with length of 1
    while 10**L % d != 1:
        L += 1
    return L

def reciprocal_cycle_len2(d):
    r = 1  # initial remainder
    reminders = []
    while r not in reminders:
        reminders.append(r)
        r = r * 10 % d
    return len(reminders) - reminders.index(r)


def reciprocal_cycle_len3(n):
    seen = {}
    r = 1
    for i in itertools.count():
        if r in seen:
            return i - seen[r]
        else:
            seen[r] = i
            r = r * 10 % n


def solution(N=1000):
    """
    Возвращает значение d < N, для которого 1/d в десятичном виде содержит самую длинную повторяющуюся последовательность цифр.

    >>> solution(10)
    7
    >>> solution(100)
    97
    >>> solution(1000)
    983
    """
    return max(sympy.primerange(1, N), key=reciprocal_cycle_len3)


if __name__ == "__main__":
    ### Run Time-Profile Table ###
    import sys;sys.path.append('..')
    from time_profile import TimeProfile

    TimeProfile(solution, [1000, 10000, 30000])
