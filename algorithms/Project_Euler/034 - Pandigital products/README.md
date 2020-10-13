# [Факториалы цифр](TODO)

## [Проблема](https://euler.jakumo.org/problems/view/34.html)

>145 является любопытным числом, поскольку 1! + 4! + 5! = 1 + 24 + 120 = 145.
>
>Найдите сумму всех чисел, каждое из которых равно сумме факториалов своих цифр.
>
>Примечание: поскольку 1! = 1 и 2! = 2 не являются суммами, учитывать их не следует.

``` python
solution   ()  # => 40730 = {145, 40585}
```

Определяем значение верхней границы:

Если взять число `n`, то можно привязать к нему количество цифр `d`

<img src = 'https://user-images.githubusercontent.com/54672403/95584618-b2e0d680-0a46-11eb-9ddc-4afaf8dc3358.jpg' width="200px"> 

Надо определить d-значное число (максимальное ~~> состоит только из 9-ток),  сумма его факториальных цифр будет равна `9!d` и, следовательно,

<img src = 'https://user-images.githubusercontent.com/54672403/95584630-b5433080-0a46-11eb-92b9-1e490845fb98.jpg' width="200px"> 

Из этого вывода следует, что максимальная верхняя граница может иметь не более 7 цифр и потерпит неудачу для любого d > 7, что дает верхнюю границу 9999999, 7-значное число из всех 9.
Но мы знаем, что 7⋅9!=25401607⋅9!=2540160, так что у нас есть лучшая верхняя граница.
Итак, мы знаем, что верхняя граница должна быть длиной 7 цифр, а первая цифра верхней границы-не более 2, в результате чего двумя возможными способами может быть сформировано 6-значное число 9,
 так что новая верхняя граница становится 2!+6⋅9!.
Это означает, что если `n` - 7-значное число, то либо вторая цифра должна быть 0 или 1, либо последняя цифра - 1.

Если первая цифра равна 2 и, следовательно, вторая цифра равна 0 или 1, то числа ограничены 2!+1!+5⋅9! = 1814403 - 
что противоречит первой цифре, равной 2.
Таким образом, 7-значное число может быть не более 1999999.

Другое наблюдение состоит в том, что все факториалы цифр выше 4 будут иметь 2 и 5 в качестве фактора и, таким образом, заканчиваться на 0.
Если все, кроме первой цифры 7-значного числа, равны по меньшей мере 5, то последняя цифра будет равна 1, исходя из 1! первой цифры, что противоречит утверждению,
 что все 6 цифр равны по меньшей мере 5. Это означает, что по крайней мере одна из 6 оставшихся цифр может быть не более 4, что снова уменьшает верхнюю границу: 1!+4!+5⋅9!=1814425. Если мы предположим, что nn-это 7-значное число, то вторая цифра будет не более 8. Если вторая цифра теперь равна 5, то одна из оставшихся цифр должна быть не более 4. Это подразумевает верхнюю границу 1!+8!+4!+4\cdot 9!=14918651!+8!+4!+4⋅9!=1491865, что противоречит тому, что вторая цифра должна быть не менее 5.
 Поэтому вторая цифра может быть не более 4, а новая верхняя граница-1499999.
 


## Частное решение (1)

```python
factorials = {'0': 1, '1': 1, '2': 2, '3': 6, '4': 24, '5': 120, '6': 720, '7': 5040, '8': 40320, '9': 362880}

def solution():
    result = 0
    for i in [2, 3, 4, 5, 6, 7]:
        for number in combinations_with_replacement(range(10), i):
            candidate = sum(factorials[i] for i in number)
            if sorted(map(int, str(candidate))) == sorted(number):
                result += candidate
    return result
```

|Число итераций|Ответ|
|---  | --- |
|19437|40730|


## Частное решение (1)

```python

factorials = {'0': 1, '1': 1, '2': 2, '3': 6, '4': 24, '5': 120, '6': 720, '7': 5040, '8': 40320, '9': 362880}

def solution():
    sfd = lambda n: sum(factorials[c] for c in str(n))
    return sum(i for i in range(10, 1499999) if sfd(i) == i)
```

|Число итераций|Ответ|
|---  | --- |
|1499989|40730|


