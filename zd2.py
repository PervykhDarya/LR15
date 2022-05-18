#!/usr/bin/env python 3
# -*- coding: utf-8 -*-


class BitString:

    #Инициализация
    def __init__(self, x):
        self.size = x
        self.x = [0] * self.size

    #Установка значения
    def set(self, x):
        self.x = list(map(int, f'{x:b}'.rjust(self.size, '0')))

    #Оператор not (~)
    def __invert__(self):
        self.x = [int(not i) for i in self.x]
        return self

    #Оператор or (|)
    def __or__(self, other):
        x = [a | b for a, b in zip(self.x, other.x)]
        return ''.join(map(str, x))

    #Оператор xor (^)
    def __xor__(self, other):
        x = [a ^ b for a, b in zip(self.x, other.x)]
        return ''.join(map(str, x))

    #Оператор and (&)
    def __and__(self, other):
        x = [a & b for a, b in zip(other.x, self.x)]
        return ''.join(map(str, x))

    #Оператор сдвиг влево (<<)
    def __lshift__(self, x):
        del (self.x[0:x])
        self.x += [0] * x
        return self

    #Оператор сдвиг вправо (>>)
    def __rshift__(self, x):
        del (self.x[len(self.x) - x:])
        self.x = [0] * x + self.x
        return self

    #Вывод результата в консоль
    def __str__(self):
        return ''.join(map(str, self.x))


if __name__ == "__main__":
    x = BitString(8)  # Размер списка 1 - 8 бит
    y = BitString(8)  # Размер списка 2 - 8 бит

    x.set(55)  # Первая цифра 00110111
    print(x)
    y.set(27)  # Вторая цифра 00011011
    print(y)

    print(f'{x} and {y} = {x & y}')
    print(f'{x} or {y} = {x | y}')
    print(f'{x} xor {y} = {x ^ y}')
    print(f'{x} not = {~x}')
    print(f'{y} >> 1 = {y >> 1}')
    print(f'{x} << 2 = {x << 2}')