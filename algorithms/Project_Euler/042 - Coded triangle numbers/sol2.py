"""
n-ый член последовательности треугольных чисел задается как t_n = 1/2 n (n+1).

Таким образом, первые десять треугольных чисел:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Преобразовывая каждую букву в число, соответствующее ее порядковому номеру в алфавите, и складывая эти значения, мы получим числовое значение слова.
Для примера, числовое значение слова SKY равно 19 + 11 + 25 = 55 = t_10.
Если числовое значение слова является треугольным числом, то мы назовем это слово треугольным словом.

Используя words.txt текстовый файл, содержащий около двух тысяч часто используемых английских слов, определите, сколько в нем треугольных слов.
"""
from math import sqrt

isTrNumber = lambda t: ((sqrt(1 + 8*t) - 1) / 2).is_integer()


def word_value(word):
    return sum(ord(char) - ord('A') + 1
               for char in word)


def solution(words: list):
    """
    Возвращает количество треугольных слов
    >>> solution()
    162
    """
    return sum(1
               for word in words
               if isTrNumber(word_value(word)))



if __name__ == '__main__':
    ### Run Time-Profile Table ###
    from timeit import default_timer
    start_time = default_timer()
    words = open('words.txt').read().strip('"').split('","')
    print(solution(words))
    print("Time: {:.3}ms".format(default_timer() - start_time))

