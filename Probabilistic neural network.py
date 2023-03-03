import math
import random

import numpy as np


def formula(input1, input2, diemension, n):
    p = 100
    q = 100
    input = np.zeros(n)
    for x in range(n):
        for y in range(diemension):
            input[x] += math.pow((input2[y] - input1[x, y]), 2)
        input[x] = math.sqrt(input[x]) / (p*q)
        input[x] = math.pow(input[x], 2)
        input[x] = math.exp(-1 * input[x])
    sum = 0
    for x in range(n):
        sum += input[x]
        sum /= n
        return sum

if __name__ == '__main__':
    diemension = 3
    n = 3
    table1 = np.zeros([n, diemension])
    table2 = np.zeros([n, diemension])
    table3 = np.zeros([n])
    for y in range(n):
        for x in range(diemension):
            table1[y][x] = random.randint(300, 400)
    for y in range(n):
        for x in range(diemension):
            table2[y][x] = random.randint(100, 200)
    for y in range(n):
        table3[y] = random.randint(0, 5)

    formula1 = formula(table1, table3, diemension, n)
    formula2 = formula(table2, table3, diemension, n)
    print(formula1)
    print(formula2)
