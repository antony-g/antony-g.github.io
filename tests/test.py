import pytest
import sys
import math

# Функция, задающая последовательность Фибоначчи
fib = lambda n: fib(n - 1) + fib(n - 2) if n > 2 else 0 if n < 1 else 1

x = -1
y = 256
z = 2**29

a = [2**i for i in range(1, 11)]
# a = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

b = [i**2 for i in range(0, 11)]
# b = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

c = [fib(i) for i in range(0, 12)]
# c = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


"""Негативный тест на взятие логарифма от отрицательного числа (не выдает ошибку)"""
def test_1():
    try:
        assert math.log(x, math.exp(1))
    except ValueError:
        pass

"""Тест на нестрогое сравнение чисел типов int и float"""
def test_2():
    y1 = y/1
    y2 = y//1
    assert (y1 == y2)


"""Тест на критическое значение степени (2**28) для числа типа float в Python"""
def test_3():
    assert math.log2(z) > sys.getsizeof(z)


"""Тест на делимость геометрической прогрессии с множителем 2"""
def test_4():
    for i in a:
        assert i % 2 == 0


"""Тест на квадраты чисел с параметризацией (проверка на квадрат от '-1' и взятие индекса '-1' в Python)"""
@pytest.mark.parametrize("test_input", [-1, 0, 1, 2, 5, 10])
def test_5(test_input):
    b_list = list(b)
    b_list.sort()
    assert test_input**2 == b_list[test_input]


"""Тест на последовательность Фибоначчи"""
def test_6():
    c_list = list(c)
    c_list.sort()
    for i in range(len(c_list) - 2):
        assert c_list[i] + c_list[i+1] == c_list[i+2]
