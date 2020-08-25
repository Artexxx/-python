"""
Пусть d(n) определяется как сумма делителей n (числа меньше n, делящие n нацело).
Если d(a) = b и d(b) = a, где a ≠ b, то a и b называются дружественной парой,
а каждое из чисел a и b - дружественным числом.

Например, делителями числа 220 являются 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 и 110,
поэтому d(220) = 284. Делители 284 - 1, 2, 4, 71, 142, поэтому d(284) = 220.

Подсчитайте сумму всех дружественных чисел меньше 10000.

  №      Время  Замедление      Число    Результат
---  ---------  ------------  -------  -----------
  1  5.66e-05   0.006%            100            0
  2  0.0007475  0.07%            1000          504
  3  0.0100173  0.93%           10000        31626
  4  0.126762   11.67%         100000       852810
  5  2.08884    196.21%       1000000     25275024
"""


def solution(LIMIT):
    # Находим сумму собственных делителей для каждого числа
    sum_of_divisors = [0] * LIMIT
    for i in range(1, len(sum_of_divisors)):
        for j in range(i * 2, len(sum_of_divisors), i):
            sum_of_divisors[j] += i

    # Найдите все дружественные пары в пределах досягаемости
    total = 0
    for i in range(1, len(sum_of_divisors)):
        j = sum_of_divisors[i]
        if j != i and j < LIMIT and sum_of_divisors[j] == i:
            total += i
    return total


if __name__ == "__main__":
    print(solution(10000))
    # ### Run Time-Profile Table ###
    # import sys; sys.path.append('..')
    # from time_profile import my_time_this
    # my_time_this(compute, [100, 1000, 10_000, 100_000, 1_000_000])