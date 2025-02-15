# [1000-Значное число Фибоначчи](TODO)

## [Проблема](https://euler.jakumo.org/problems/view/25.html)

> Последовательность Фибоначчи определяется рекурсивным правилом:
> 
> F<sub>n</sub> = F<sub>n−1</sub> + F<sub>n−2</sub>, где F<sub>1</sub> = 1 и F<sub>2</sub>  = 1.
> Таким образом, первые 12 членов последовательности равны:
> 
> F1 = 1
> <br>F<sub>2 </sub>= 1
> <br>F<sub>3 </sub>= 2
> <br>F<sub>4 </sub>= 3
> <br>F<sub>5 </sub>= 5
> <br>F<sub>6 </sub>= 8
> <br>F<sub>7 </sub>= 13
> <br>F<sub>8 </sub>= 21
> <br>F<sub>9 </sub>= 34
> <br>F<sub>10</sub> = 55
> <br>F<sub>11</sub> = 89
> <br>F<sub>12</sub> = 144
>
> Двенадцатый член F12 - первый член последовательности, который содержит три цифры.
> 
> Каков порядковый номер первого члена после N цифр?

``` python
solution   (3)  # => 12 = (F11, 89)(F12, 144)
solution  (50)  # => 237 = (F49, 7_778_742_049)(F50, 12_586_269_025)
solution (100)  # => 476
solution (1000)  # => 4782
```

## Частное решение (1)
```python
def fibonacci(n):
    if n == 1 or type(n) is not int:
        return 0
    elif n == 2:
        return 1
    else:
        sequence = [0, 1]
        for i in range(2, n + 1):
            sequence.append(sequence[i - 1] + sequence[i - 2])
        return sequence[n]


def fibonacci_digits_index(n):
    digits = 0
    index = 2
    while digits < n:
        index += 1
        digits = len(str(fibonacci(index)))
    return index


def solution(n):
    return fibonacci_digits_index(n)
```
```text
  №      Время  Замедление      Число    Результат
---  ---------  ------------  -------  -----------
  1  0.0002482  0.025%             10           45
  2  0.0181968  1.79%             100          476
  3  2.22865    221.05%          1000         4782
```
*[-] Функция fibonacci(n)* вызывается каждый раз по новому, лучше сделать её генератором.

```python
import itertools

def fibonacci_generator():
    prev, cur = 0, 1
    while True:
        prev, cur = cur, prev + cur
        yield cur

def solution(n):
    gen = fibonacci_generator()
    for index in itertools.count(start=2):
        digits = len(str(next(gen)))
        # if digits > n:
        #     raise RuntimeError("Not found")
        if digits == n:
            return index
```
```text
  №      Время  Замедление      Число    Результат
---  ---------  ------------  -------  -----------
  1   2.81e-05  0.003%             10           45
  2   0.000335  0.03%             100          476
  3   0.031215  3.09%            1000         4782
  4  20.8278    2079.66%        10000        47847 
```

# Общее решение (TODO)

>Последовательность Фибоначчи растет экспоненциально с основанием около 1,618, так что числа в базе 10 будут удлиняться на одну цифру
после каждого log10 (1.618) ~= 4.78 шагов в среднем. Это означает, что ответ находится на индексе около 4780.

#  Похожая задача (TODO)

>Вычислить 1000 значное число фибонначчи


Из рекуррентного соотношения `a(n) = a(n-1) + a(n-2)` мы можем получить
 характеристический многочлен `r^n-r^(n-1) - r (n-2)`, решения которого будут равны:
 `r1=(1+sqrt(5))/2=~1.618` и `r2 = (1-sqrt(5))/2 =~ -0.6`
```python
r1 = (1 + sqrt(5)) / 2
r2 = (1 - sqrt(5)) / 2
```

Теперь мы знаем, что N-й член последовательности Фибоначчи равен
`a * r1^n + b * r2^n` для некоторых `a` и `b`. Мы можем найти эти `a` и `b`, используя начальные условия для
 последовательности Фибоначчи, `a(0) = 0` и `a(1) = 1`
 чтобы найти, что `0 = a*r1^0 +b*r1^0` и `1=a*r1^1 +b * r2^1`, поэтому `a=1/sqrt(5)` и `b= -a = -1/sqrt(5)`
```python
a = 1 / sqrt(5)  # ~=> 0.4472
b = -a  # ~=> -0.4472
```
Второй член в `a*r1^n + b * r2^n` очень мал для больших чисел `n`,
так что пока мы можем спокойно игнорировать его. Первый член Фибоначчи со 1001 цифрой - это первое значение,
 большее `10^1000`, поэтому мы можем использовать равенство `n = ln(10^1000 /a)/ln(r1)`, чтобы найти цифру

```python
n1 = (log(10**999 / a)) / log(r1)  # ~=> 4787.6
```

Теперь нам просто нужно округлить n
```python
n = round(n1)  # ROUND UP #~=> 4787
```
И используйте уравнение выше, чтобы найти наше число
```python
thousandDigitFibonacci = a * r1 ** n + b * r2 ** n
thousandDigitFibonacci = int(thousandDigitFibonacci)  # ROUND DOWN
```

