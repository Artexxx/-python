# [Сумма последовательных простых чисел](TODO)
                   
## [Проблема](https://euler.jakumo.org/problems/view/50.html)

>Простое число 41 можно записать в виде суммы шести последовательных простых чисел:
>
>41 = 2 + 3 + 5 + 7 + 11 + 13
>
>Это - самая длинная сумма последовательных простых чисел, в результате которой получается простое число меньше одной сотни.
>
>Самая длинная сумма последовательных простых чисел, в результате которой получается простое число меньше одной тысячи, содержит 21 слагаемое и равна 953.
>
>Какое из простых чисел меньше одного миллиона можно записать в виде суммы наибольшего количества последовательных простых чисел?


``` python
solution  () => 997651
```

## Нормальное решение (1)

```python
def prime_sieve(limit) -> List[int]:
    """
    Input limit>=3, return a list of prime numbers less than `limit`.

    Example
    ========
    >>> prime_sieve(11)
    [2, 3, 5, 7, 11]
    >>> prime_sieve(17)
    [2, 3, 5, 7, 11, 13, 17]
    """
    from itertools import compress
    sieve = bit_sieve(limit+1)
    return [2, *compress(range(3, limit+1, 2), sieve[3::2])]


def solution():
    """
    Находит простое число, меньше одного миллиона, которое можно записать в виде суммы наибольшего количества последовательных простых чисел.
    """
    primes = prime_sieve(10**6)
    longest = 21
    result = 0

    for i in range(len(primes)):
        for j in range(i + longest, len(primes) - i + 1):
            temp_sum = sum(primes[i:j])
            if temp_sum > 10**6:
                break
            if temp_sum in primes:
                if len(primes[i:j]) > longest:
                    result = temp_sum
                    longest = len(primes[i:j])

    return result
```
```text
   Время  Замедление    Аргумент      Результат
--------  ------------  ----------  -----------
0.581774  58.177%                        997651 (Ответ)
```

