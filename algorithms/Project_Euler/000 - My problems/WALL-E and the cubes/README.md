**Задача:**
<br>
Робот WALL-E пытается упорядочить груду кубиков.
В зоне его ответственности есть n расположенных друг за другом столбиков,
 каждый состоит из кубиков, стоящих друг на друге (в i-м столбике содержится h_i кубиков, столбики нумеруются слева направо).
Робот действует по следующему алгоритму: он ищет самый левый столбик с номером i, в котором кубиков больше, чем в предыдущем, то есть h_{i-1} < h_i.
Далее он берет верхний кубик столбика номер i и сбрасывает его на столбик номер i−1.
Если существует столбик с номером i−2 и в нем теперь меньше чем в i−1-м столбике, то данный кубик перемещается далее на i−2-й столбик.
И так до тех пор, пока этот кубик либо не дойдет до верха первого столбика либо не упрется в более высокий столбик слева.
Далее эта последовательность операций повторяется до тех пор, пока есть два рядом стоящих столбика таких, что h_{i-1} < h_ih
По значениям высот исходных n столбиков вывести высоты упорядоченных n столбиков.

**Формат входных данных**

1. N — количество столбиков. `1 ≤ N ≤ 10^5`

2. Массив из N чисел h_1, h_2, ..., h_N , соответствующих высотам соответствующих столбиков `1 ≤ h_i ≤ 10^9`

**Формат выходных данных**

Вывести N чисел через пробел, соответствующих высотам столбиков, после того, как WALL-E закончит работу.

**Пояснение к примеру.**

Следующая серия иллюстраций показывает, куда и какие кубики попали в процессе упорядочивания столбиков:

1. Стартовая ситуация


<img src="https://user-images.githubusercontent.com/54672403/95760261-78c83c80-0cb3-11eb-8660-876c0396c08f.png">

2. Упорядочили столбик 3

<img src="https://user-images.githubusercontent.com/54672403/95760286-7f56b400-0cb3-11eb-8c15-b1b3c283605b.png">


3. Упорядочили столбик 4

<img src="https://user-images.githubusercontent.com/54672403/95760305-867dc200-0cb3-11eb-91b4-0781882ec352.png">


4. Упорядочили столбик 6

<img src="https://user-images.githubusercontent.com/54672403/95760314-88e01c00-0cb3-11eb-815b-34ce1b61bb96.png">

5. Упорядочили столбик 8

<img src="https://user-images.githubusercontent.com/54672403/95760324-8bdb0c80-0cb3-11eb-8072-d369c7248b5f.png">

6. Упорядочили столбик 9

<img src="https://user-images.githubusercontent.com/54672403/95760329-8ed5fd00-0cb3-11eb-8623-8049c18053d9.png">


7. Упорядочили столбик 10, итоговое расположение кубиков

<img src="https://user-images.githubusercontent.com/54672403/95760772-191e6100-0cb4-11eb-9cd5-ba8982b9768a.png">


**Пример запуска программы:**
<br>
```python
>>> solution(10, [2 1 6 8 1 2 1 3 5 4])
```
**Выхлоп:**
<br>
```python
>>> [5 4 4 4 3 3 3 3 2 2]
```
