# [Дроби, сократимые по цифрам](TODO)

## [Проблема](https://euler.jakumo.org/problems/view/33.html)

> Дробь 49/98 является любопытной, поскольку неопытный математик, пытаясь сократить ее, будет ошибочно полагать,
> что 49/98 = 4/8, являющееся истиной, получено вычеркиванием девяток.
>
>Дроби вида 30/50 = 3/5 будем считать тривиальными примерами.
>
>Существует ровно 4 нетривиальных примера дробей подобного типа, которые меньше единицы и содержат двухзначные числа как в числителе, так и в знаменателе.
>
>Пусть произведение этих четырех дробей дано в виде несократимой дроби (числитель и знаменатель дроби не имеют общих сомножителей). Найдите знаменатель этой дроби.

``` python
solution ()  # => 100 = {16/64 26/65 19/95 49/98}
```

## Нормальное решение (1):

```python
def ReducedFraction(n, d):
    """
    Принимает дробь в виде кортежа (числитель,знаменатель) и возвращает сокращенную форму дроби.

    [*] Для сокращения дроби, используется, "Алгоритм Евклида" - для нахождения общего делителя.
    """

    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    common_divisor = gcd(n, d)
    return (n // common_divisor, d // common_divisor)


def cancel_digit(numerator, denominator):
    """
    Сокращает общую цифру в числителе и знаменателе (игнорирует 0)
    """
    numerator_digits_set = set(str(numerator))
    denominator_digits_set = set(str(denominator))
    if (('0' not in numerator_digits_set | denominator_digits_set) and
        (len(numerator_digits_set) > 1) and(len(denominator_digits_set) > 1)):
        common_digit = numerator_digits_set & denominator_digits_set
        if common_digit:
            repeat = common_digit.pop()
            numerator_cancelled = str(numerator).replace(repeat, '')
            denominator_cancelled = str(denominator).replace(repeat, '')
            return (int(numerator_cancelled), int(denominator_cancelled))
    return None


def solution():
    """
    Возвращает знаменатель произведения 4x особых дробей.

    >>> solution()
    100
    """
    result_fractions = []
    for denominator in range(12, 99):
        for numerator in range(12, denominator):
            canceled_fraction = cancel_digit(numerator, denominator)
            digits_is_canceled = canceled_fraction is not None
            if digits_is_canceled:
                arithmetics_reduced = ReducedFraction(numerator, denominator)
                if ReducedFraction(*canceled_fraction) == arithmetics_reduced:
                    result_fractions.append(arithmetics_reduced)
    product_numerators, product_denominators = (1, 1)
    for (n, d) in result_fractions:
        product_numerators *= n
        product_denominators *= d
    return ReducedFraction(product_numerators, product_denominators)[1]
```
```text
The denominator is 100 and it took 0.005460 seconds to find.
```

## Математическое решение (1): TODO

Пусть чисдитель и знаменатель будут равны  `1≤n<d≤9` соответственно, где  `n/d<1` ~> `n<d`
Найдём четыре комбинации возможных уравнений:

<img src='https://user-images.githubusercontent.com/54672403/94723605-adf29780-0361-11eb-8f20-e224c2565368.jpg' width="250px">

Пройдемся по этим уравнениям:

<img src='https://user-images.githubusercontent.com/54672403/94850730-0abc8380-0430-11eb-82f4-fe7b8dc53784.jpg' width="300px">


Первое уравнение не имеет решения из-за противоречия, возникающего из `n<d`. Переходим ко второму уравнению

<img src='https://user-images.githubusercontent.com/54672403/95353049-80f73500-08cb-11eb-9ac1-d220b00a199c.jpg' width="300px">

Второе уравнение не имеет решения по той же причине, что и первое уравнение. Рассмотрим третье уравнение:

<img src='https://user-images.githubusercontent.com/54672403/95353626-290cfe00-08cc-11eb-8316-26caff8cf8e1.jpg' width="300px">

Поскольку `n < d` правая часть должна быть положительной. 
Следовательно, левая сторона тоже должна быть положительной, а это возможно при `c < n`.

<br><img src='https://user-images.githubusercontent.com/54672403/95353411-e9dead00-08cb-11eb-8018-d5712d00a1df.jpg' width="250px">

Из `c < 9` следует `c/9 < 1`. Значение `с/9 - (cn)/(9d)` будет либо отрицательным, либо слишком малым
А это нам не подходит, потому что значение выражения в левой части содержит целое число

Давайте рассмотрим последнее уравнение:

<img src='https://user-images.githubusercontent.com/54672403/95357015-00870300-08d0-11eb-91b8-3320a7f6d751.jpg' width="300px">

Правая сторона осталась такой же, и снова должна быть положительной, в результате чего левая сторона также должна быть положительной.
Это сокращает наше пространство решений до `n < d < c ≤ 9`. Решить эту проблему сейчас довольно просто:

```python
def solution():
    """
    Возвращает знаменатель произведения 4x особых дробей.

    >>> solution()
    100
    """
    denominator, numerator = 1, 1
    for c in range(1, 10):
      for d in range(1, c):
        for n in range(1, d):
          if ((n * 10 + c) * d == (c * 10 + d) * n):
            denominator *= d
            numerator *= n
    return reduceFractionToLowestCommonTerms(numerator, denominator)[1]
``` 

Но мы можем пойти еще дальше и решить все вручную. 
Начнем с нашего последнего уравнения:

<img src='https://user-images.githubusercontent.com/54672403/95571697-84a4cc00-0a31-11eb-92b9-3e8d78b84db4.jpg' width="250px">

Чтобы `c(d - n)` делилось на 9, `c` может быть только `3`, `6` или `9`. 
Рассмотрим эти три случая:

>**Случай 1**, если `c=3`:
>
>Результатом `d-n` должно быть `3` или `6`, что невозможно.
> Поскольку `n<d<3`, то значения могут быть только такими: `n=1`, `d=2`

>**Случай 2**, если `c=6`:
>
>Результатом `d-n` должно быть `3` или `6`.
>
>Однако результат `d - n` не может быть `6`, потомучто `d<n<6`.
>Поэтому `d - n`  может быть только `3`, что приводит к 2 решениям:
>(n=1,d=4), (n=2,d=5).

>**Случай 3**, если `c=9`:
>
><img src='https://user-images.githubusercontent.com/54672403/95572837-385a8b80-0a33-11eb-934c-a11fc1ee99ae.jpg' width="250px">
>
>Чтобы значение `n` было положительным, `5≤d≤9` должно быть истинным. 
>Единственно возможными способами сделать `n` целым числом являются `d=5` и `d=8`. 
>
>При этом можно собрать следующие решения:
>(c=6,n=1,d=4),
>
>(c=6,n=2,d=5),
>
>(c=9,n=1,d=5),
>
>(c=9,n=4,d=8)

Что приводит к следующим дробям:

<img src='https://user-images.githubusercontent.com/54672403/95573159-b159e300-0a33-11eb-9ee4-2b5601ffa603.jpg' width="330px">


