# [Пан-цифровые произведения](TODO)

## [Проблема](https://euler.jakumo.org/problems/view/32.html)

> Каждое n-значное число, которое содержит каждую цифру от 1 до n ровно один раз, будем считать пан-цифровым; к примеру, 5-значное число 15234 является пан-цифровым, т.к. содержит цифры от 1 до 5.
>
>Произведение 7254 является необычным, поскольку равенство 39 × 186 = 7254, состоящее из множимого, множителя и произведения является пан-цифровым, т.е. содержит цифры от 1 до 9.
>
>Найдите сумму всех пан-цифровых произведений, для которых равенство "множимое × множитель = произведение" можно записать цифрами от 1 до 9, используя каждую цифру только один раз.
>
>Примечание: Некоторые произведения можно получить несколькими способами, поэтому убедитесь, что включили их в сумму лишь единожды.

``` python
solution   ()  # => 45228
```


## Частное решение (1)

```python
def is_pandigital(a, b, c) -> bool:
    """True если abc образует пан-цифровое произведение"""
    s = f'{a}{b}{c}'
    if '0' in s: return False
    return len(s) == 9 == len(set(s))


def pandigital_products_sum():
    """
    Возвращает сумму всех пан-цифровых произведений.

    >>> solution()
    45228
    """
    result_sum = 0
    for c in range(1234, 9876):
        for b in range(2, int(sqrt(c)) + 1):
            if c % b == 0:
                a = c // b
                if is_pandigital(a, b, c):
                    result_sum += c
                    break
    return result_sum

```

|Время    |Число итераций|Ответ| 
|---      |---  | --- |
| 0.03506 |32913|45228|
