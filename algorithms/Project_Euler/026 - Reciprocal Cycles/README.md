# [Обратные циклы](TODO)

## [Проблема](https://euler.jakumo.org/problems/view/26.html)

> Единичная дробь имеет 1 в числителе. 
>Десятичные представления единичных дробей со знаменателями от 2 до 10 даны ниже:
>

<blockquote>
<table><tbody><tr><td><sup>1</sup>/<sub>2</sub></td><td>=&nbsp;</td><td>0.5</td>
</tr><tr><td><sup>1</sup>/<sub>3</sub></td><td>=&nbsp;</td><td>0.(3)</td>
</tr><tr><td><sup>1</sup>/<sub>4</sub></td><td>=&nbsp;</td><td>0.25</td>
</tr><tr><td><sup>1</sup>/<sub>5</sub></td><td>=&nbsp;</td><td>0.2</td>
</tr><tr><td><sup>1</sup>/<sub>6</sub></td><td>=&nbsp;</td><td>0.1(6)</td>
</tr><tr><td><sup>1</sup>/<sub>7</sub></td><td>=&nbsp;</td><td>0.(142857)</td>
</tr><tr><td><sup>1</sup>/<sub>8</sub></td><td>=&nbsp;</td><td>0.125</td>
</tr><tr><td><sup>1</sup>/<sub>9</sub></td><td>=&nbsp;</td><td>0.(1)</td>
</tr><tr><td><sup>1</sup>/<sub>10</sub></td><td>=&nbsp;</td><td>0.1</td>
</tr></tbody></table></blockquote>

>Где 0.1(6) значит 0.166666..., и имеет повторяющуюся последовательность из одной цифры. Заметим, что 1/7 имеет повторяющуюся последовательность из 6 цифр.
>
>Найдите значение d < 1000, для которого 1/d в десятичном виде содержит самую длинную повторяющуюся последовательность цифр.

``` python
solution   (10)  # => 7
solution   (100)  # => 97
solution   (1000)  # => 983
solution   (10_000)  # => 9967
```

## Частное решение (1)

- разделив `125` на `18`. Учитывая целочисленное деление, мы получаем `6` с остатком `17`
```code
125 : 18 = 6
 17
```
- разделим `17` на `18`. Найдя значение меньше `1`, добавим `0` и вычислите вместо него `170/18`.
 Поскольку значение было недостаточным, отметьте десятичную точку на результате.
```code
125 : 18 = 6.
 170
```
- `170/18` дает `9` с остатком `8`
```code
125 : 18 = 6.9
 170
   8
```
Процесс продолжает добавлять значение, возвращаемое целочисленным делением в результате `(6.9....)`.
Это происходит до тех пор, пока остаток не достигнет `0` или не повторится.

```code
125 : 18 = 6.944
 170
   80
    80
```
В этом случае `80/18` возвращает `4` с остатком `8`. Это снова вызывает `80/18`, что означает, что `4`-это повторяющийся шаблон для `125/18`:

```code
125 : 18 = 6.9(4)
```

```python
def reciprocal_cycle_len(n):
    seen = {}
    x = 1
    for i in itertools.count():
        if x in seen:
            return i - seen[x]
        else:
            seen[x] = i
            x = x * 10 % n


def solution(N=1000):
    return max(range(1, N), key=reciprocal_cycle_len)
```
```text
  №      Время  Замедление      Число    Результат
---  ---------  ------------  -------  -----------
  1  1.11e-05   0.001%             10            7
  2  0.000297   0.03%             100           97
  3  0.0157933  1.55%            1000          983
  4  1.17498    115.92%         10000         9967
```