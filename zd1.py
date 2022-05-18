#!/usr/bin/env python 3
# -*- coding: utf-8 -*-


class Num:

    def __init__(self, first, second):
        self.first = first
        self.second = second
        if self.first == 0:
            raise ValueError

    def __pow__(self, other):
        a = self.first + self.second
        b = other.first + other.second
        return a ** b


if __name__ == "__main__":
    num1 = Num(5.5, 0)
    num2 = Num(2, 0)
    print(f"Результат: {num1 ** num2}")