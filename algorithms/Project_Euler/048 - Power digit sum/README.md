# [Собственные степени](TODO)

                   
## [Проблема](https://euler.jakumo.org/problems/view/48.html)


>Сумма 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
>
>Найдите последние десять цифр суммы 1^1 + 2^2 + 3^3 + ... + 1000^1000.
                   
``` python
solution  () => 
```

## Частное решение (1)

```python
def solution(n=1):
    """Находит последние десять цифр суммы 1^1 + 2^2 + 3^3 + ... + n^n.
    """
    return sum(i ** i for i in range(1, n + 1)) % (10**10)
```
```text
  №      Время  Замедление      Аргумент    Результат
---  ---------  ------------  ----------  -----------
  1  0.0081473  0.815%              1000   9110846700 (ответ)
  2  4.50355    449.540%           10000   6237204500
```

## Нормальное решение (1) 

Свойство [модульной арифметики](https://en.wikipedia.org/wiki/Modular_arithmetic), которое я использовал: 
```text
(a+b) % c = ((a % c) + (b % c) )% c
```

```python
def solution(n=1000):
    """Находит последние десять цифр суммы 1^1 + 2^2 + 3^3 + ... + n^n.
    """
    c = 10 ** 10
    return sum(a ** a % c for a in range(1, n+1)) % c
```
```text
  №      Время  Замедление      Аргумент    Результат
---  ---------  ------------  ----------  -----------
  1  0.0015154  0.152%              1000   9110846700 (ответ)
  2  0.0198508  1.834%             10000   6237204500
  3  0.247869   22.802%           100000   3031782500
```