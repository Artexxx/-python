# [Пути через таблицу](TODO)

## [Проблема](https://euler.jakumo.org/problems/view/15.html)


>Начиная в левом верхнем углу сетки 2×2 и имея возможность двигаться только вниз или вправо, существует ровно 6 маршрутов до правого нижнего угла сетки.
>
>![image](https://user-images.githubusercontent.com/54672403/90906176-e786c900-e3d9-11ea-888f-d98c363c7232.png)
>
>Сколько существует таких маршрутов в сетке размером gridSize?


К сожалению, я столкнулкивался с этой проблемой на уроке математики и помню решение с использованием биномиального коэффициента размера сетки:
 для `x` строк и `y` столбцов число путей решетки от начала координат `(0, 0)` выражается следующим коэффициентом:

>Это классическая задача в комбинаторики. 
>Чтобы перейти от верхнего левого угла к нижнему правому углу сетки `N*N`,
  можно ровно `N` ходов сделать вправо и `N` ходов вниз *(в любом порядке)*.

```
(  x + y  )
(    x    )
```

Для выполнения поставленной задачи x и y являются одним и теми же.

```
(    2 * gridSize  )
(    gridSize      )
```

Формула биноминального коэфицента:
```
(n k) = n!  / (k! * (n - k)!)

2*gridSize!  / (gridSize! * gridSize!)
```
    

``` python
solution   (25) # =>   126410606437752
solution   (23) # =>   8233430727600
solution   (20) # =>   137846528820
solution   (15) # =>   155117520
solution   (1)  # =>   2
```

## Общее решение (1)

```python
def binomial(n, k):
    assert 0 <= k <= n
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

def solution(gridSize):
    return binomial(n=gridSize*2, k=gridSize)
```