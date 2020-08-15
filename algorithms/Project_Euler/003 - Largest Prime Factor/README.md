# [Наибольший простой делитель](TODO)

## [Проблема](https://euler.jakumo.org/problems/view/3.html)

> Простые делители числа 13195 - это 5, 7, 13 и 29.
>
> Каков самый большой делитель числа n, являющийся простым числом?


``` python
solution (10) # => 5 
solution (17) # => 17
solution (13195) # => 29
solution (600851475143) # => 6857
```
*Решение должно работать для действительно больших чисел (`600 851 475 143`).*

----

Согласно ***фундаментальной арифметической теореме***, каждое целое число `n > 1` имеет уникальную факторизацию, как произведение простых чисел.
Другими словами, теорема гласит, что `n = p_0 * p_1 * ... * p_{m-1}`, где каждое `p_i > 1` является простым, но не обязательно уникальным.
Теперь, если мы возьмем число `n` и многократно разделим его наименьший множитель (который также должен быть простым), то последний
 множитель, который мы делим, должен быть самым большим простым множителем `n`. К примеру, `600851475143` = 71 * 839 * 1471 * 6857


1. Если число `n` простое, то у него есть только 2 делителя `17 ~> (1, 17)` => ответ начальное число `n` 
2. Каждое число `n`, которое не является простым, имеет по крайней мере один простой делитель `p`, `1 < p < sqrt(n)`

## Нормальное решение (1)

- найдите первый простой ножитель.
- разделить входное число на это новообретенное значение, повторить 1

Рекурсивно находя первое простое число, мы разбиваем входное число на все меньшие и меньшие значения. 
Если число простое, то функция определит такое значение как решение задачи.

```python
def smallest_prime_factor(n) -> int:
    assert n > 1
    if n % 2 == 0: return 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0: return i
    return n  # ~> N является простым


def solution(n):
    while True:
        p = smallest_prime_factor(n)
        if p < n:
            n /= p
        else:
            return n
```
``` text
  №      Время  Замедление                  Число         Результат
---  ---------  ------------  -------------------  ----------------
  1  9.2e-05    0.009%               600851475143      6857
  2  9.8e-05    0.00%                100000000002      1543070
  3  6.8e-05    0.00%         1000000000000000001      5882350
  4  5.4e-05    0.00%         2000000000000000001      250501
```