# [Словарные перестановки](TODO)

## [Проблема](https://euler.jakumo.org/problems/view/24.html)


> ***Перестановка*** - это упорядоченная выборка объектов. 
> 
> К примеру, 3124 является одной из возможных перестановок из цифр 1, 2, 3 и 4. 
> Если все перестановки приведены в порядке возрастания или алфавитном порядке, то такой порядок будем называть словарным.
>  Словарные перестановки из цифр 0, 1 и 2 представлены ниже:
> 
> 012   021   102   120   201   210
> 
> Какова миллионная словарная перестановка из цифр `0, 1, 2, 3, 4, 5, 6, 7, 8 и 9`?

``` python
solution   ()  # => 2_783_915_460
```

## Частное решение (0)
```python
def solution():
    result = list(map("".join, permutations("0123456789")))
    return result[999999]


# Аналогичное решение
solution2 = ''.join(list(permutations('0123456789'))[999999])
```

## Общее решение (1)

```python
factorial(10) # => 3_628_800
```
Мы знаем, что существует три с лишним миллиона способов упорядочить числа.
Однако если бы мы зафиксировали первую цифру, например, `1`, то это число свелось бы к:

```python
factorial(9)  # =>  362_880
```
Если мы знаем это, мы приходим к пониманию, что есть `362880` возможности, прежде чем мы исчерпаем каждую строку, начинающуюся с `1`.
Другими словами, число `1023456789` находится на `362881` месте в серии.

Число `2013456789` должно находиться на `362880 * 2 + 1 = 725761` позиции.

<br>Давайте рассмотрим как из индекса числа найти с какой цифры оно начинается:
<br>Возьмем `699999-е` число и докажем, что оно начинается с `1`;
- вычисляем факториал `9`: `362880`
- вычисляем целочисленное деление между заданным числом и факториалом: `int(699999 / 362880) = 1`
- вычисляем разницу: `699999 - 362880 = 337119` 

Учитывая это, мы уже знаем, что строка начинается с `1`. 
<br>Более того, мы начинаем искать первую цифру `337119-е` числа, полученного из оставшихся цифр (`0-9 без 1`).
- вычисляем факториал `8`: `40320`
- вычисляем целочисленное деление между заданным числом и факториалом: `int(337119 / 40320) = 8`
- вычисляем разницу: `699999 - 362880 = 337119` 
<br>
Примечание: Мы уже использовали цифру `1` поэтому восьмое значение на самом деле `9`.

|Индекс  | Факториал|Целочисленное деление| Последовательность-Результат|	Оставшиеся цифры|	Разница             |
| ------ | --------- | ----------------  | ----------                  | ---------         | --------------------- |
| 699999+ | 362880    | 1                | 1                           | 023456789         | `699999 - 362880 * 1` |
| 337119+ | 40320     | 8                | 19                          | 02345678          | `337119 - 40320 * 8`  |
| 14559+  | 5040      | 2                | 193                         | 0245678           | `14559 - 5040 * 2`    |
| 4479+   | 720       | 6                | 1938                        | 024567            | `4479 - 720 * 6`      |
| 159+    | 120       | 1                | 19382                       | 04567             | `159 - 120 * 1`       |
| 39+     | 24        | 1                | 193824                      | 0567              | `39 - 24 * 1`         |
| 15+     | 6         | 2                | 1938246                     | 057               | `15 - 6 * 2`          |
| 3+      | 2         | 1                | 19382465                    | 07                | `3 - 2 * 1`           |
| 1+      | 1         | 1                | 193824657                   | 0                 | `1 - 1 * 1`           |
| 0+      | 1         | 0                | 1938246570                  |                   | `0`                   |

Итак, `699999-е`  число в серии это `1938246570`.

```python
def solution(N) -> int:
    """Возвращает N словарную перестановка из цифр 0, 1, 2, 3, 4, 5, 6, 7, 8 и 9.

     >>> solution()
     2_783_915_460
     """
    # отрегулирован номер перестановки, чтобы он был проиндексирован на ноль
    n = N - 1
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    # Определяется каждая цифра N-й лексикографической перестановки
    digit_count = len(digits)
    permutation_digits = []
    # for i in range(digit_count, 0, -1):
    for i in range(1, digit_count):
        digit, n = divmod(n, factorial(digit_count - i))
        permutation_digits.append(digits[digit])
        del digits[digit]

    # добавляется оставшаяся цифра
    permutation_digits.append(digits[0])
    return int(''.join(permutation_digits))

def solution_1(POS):
    """ Аналогичное решение """
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    permutation_digits = []

    # Индекс позиции - это как в списке. N-й элемент - это элемент с индексом n-1
    pos = POS - 1
    for i in reversed(range(len(digits))):
        c = pos // factorial(i)  # math.floor
        permutation_digits.append(digits[c])
        digits.remove(digits[c])
        pos = pos - c * factorial(i)
    return int(''.join(permutation_digits))

```


