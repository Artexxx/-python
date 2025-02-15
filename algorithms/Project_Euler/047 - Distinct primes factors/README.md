# [Различные простые множители](TODO)

                   
## [Проблема](https://euler.jakumo.org/problems/view/47.html)


>Первые два последовательные числа, каждое из которых имеет два отличных друг от друга простых множителя:
><br>14 = 2 × 7
><br>15 = 3 × 5
>
>Первые три последовательные числа, каждое из которых имеет три отличных друг от друга простых множителя:
><br>644 = (2)^2 × 7 × 23
><br>645 = 3 × 5 × 43
><br>646 = 2 × 17 × 19.
>
>Найдите первые четыре последовательных числа, каждое из которых имеет четыре отличных друг от друга простых множителя. Каким будет первое число?                   

``` python
solution  () => 134043
```

## Частное решение (1)

```python
@memoize
def prime_factors(n) -> set:
    """Return a set of n's prime factors

    >>> prime_factors(220)
    [2, 5, 11]
    """
    i = 2
    factors = set()
    while i * i <= n:
        if n % i != 0:
            i += 1
        else:
            n //= i
            factors.add(i)
    if n > 1:
        factors.add(n)
    return factors


def solution():
    """Находит первое из первых четырех последовательных чисел, каждое из которых имеет четыре отличных друг от друга простых множителя.
    """
    number = 1
    while True:
        if      len(prime_factors(number)) == 4\
            and len(prime_factors(number + 1)) == 4 \
            and len(prime_factors(number + 2)) == 4 \
            and len(prime_factors(number + 3)) == 4:
            break
        number += 1
    return number
```
```text
  Время  Замедление    Аргумент      Результат
-------  ------------  ----------  ----------- <913330 function calls>
1.33932  133.932%               4       134043 (Ответ)
```

## Нормальное решение (1)

Сложность `O(nlg⁡lg⁡n) ~ O(n)`:
Это решение использует Решето Эратосфена для предварительного подсчета простых множителей для каждого числа.
<br>Так, например, 30 посещается 3 раза, потому что у него есть три простых множителя 2, 3, 5.



```python
def solution(LIMIT=10 ** 6):
    """Находит первое из первых четырех последовательных чисел, каждое из которых имеет четыре отличных друг от друга простых множителя.
    """
    factors  = [0] * (LIMIT + 1)  # Количество простых множителей для каждого числа
    len_sequence = 0  # Количество последовательных чисел с 4 простыми множителями

    for n in range(2, LIMIT + 1):
        if factors[n] == 0:  # `n` простое число.
            factors[n::n] = [x + 1 for x in factors[n::n]]
            continue

        elif factors[n] == 4:
            len_sequence += 1
            if len_sequence == 4:
                return n - 3
        else:
            len_sequence = 0
```
```text
  Время  Замедление    Аргумент    Результат
-------  ------------  --------    ----------- <12501 function calls>
  0.193  19,332%              4    134043 (Ответ)
```