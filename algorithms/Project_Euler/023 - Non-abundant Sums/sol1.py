"""
Идеальным числом называется число, у которого сумма его делителей равна самому числу. Например, сумма делителей числа `28`
 равна `1 + 2 + 4 + 7 + 14 = 28`, что означает, что число `28` является идеальным числом.

Число `n` называется недостаточным, если сумма его делителей меньше `n`, и называется избыточным, если сумма его делителей больше `n`.

Так как число `12` является наименьшим избыточным числом (`1 + 2 + 3 + 4 + 6 = 16`), наименьшее число, которое может быть
записано как сумма двух избыточных чисел, равно 24. Используя математический анализ, можно показать, что все целые числа больше
`28123 `могут быть записаны как сумма двух избыточных чисел. Эта граница не может быть уменьшена дальнейшим анализом,
даже несмотря на то, что наибольшее число, которое не может быть записано как сумма двух избыточных чисел, меньше этой границы.

Найдите сумму всех положительных чисел, которые не могут быть записаны как сумма двух избыточных чисел.

  №    Время  Замедление      Число    Результат
---  -------  ------------  -------  -----------
  1  0.458249  45.825%       28124      4 179 871
"""


def solution(LIMIT = 28124) -> int:
    """ Возращает сумму всех положительных чисел, которые не могут быть записаны как сумма двух избыточных чисел"""
    sumDivs = [0] * LIMIT
    # Находим сумму собственных делителей для каждого числа
    for i in range(1, LIMIT):
        for j in range(i * 2, LIMIT, i):
            sumDivs[j] += i

    abundants = set()
    result_sum = 0
    for n in range(1, LIMIT):
        # check if n is an abundant number
        if sumDivs[n] > n:
            abundants.add(n)

        # check if n is the sum of any abundant number pairs seen so far
        if not any((n - a in abundants) for a in abundants):
            result_sum += n
    return result_sum


if __name__ == "__main__":
    print(solution())