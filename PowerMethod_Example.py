# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 17:08:12 2017

@author: SoliareOfAstora
"""
import numpy as np


class diagonalArray:
    values = np.array([8, 2, 1])
    offset = np.array([0, 1, 3])

    def get(self, x, y):
        if y < 0:
            return 0
        distance = x - y
        if distance < 0:
            distance *= -1
        for i in range(np.size(self.offset)):
            if self.offset[i] == distance:
                return self.values[i]
        return 0

    def calculate(self, source, output):
        for i in range(64):
            output[i] = 0
            for j in range(-3, 4, 1):
                if 0 <= i + j < 64:
                    output[i] += self.get(self, i, i + j) * source[i + j]


arr = diagonalArray
output = np.ones(64)
while True:

    inp = np.copy(output)
    diagonalArray.calculate(arr, inp, output)
    output /= np.linalg.norm(output)

    if np.linalg.norm(output - inp) < pow(10, -7):
        break

diagonalArray.calculate(arr, inp, output)
# ============================================================
np.linalg.norm(output) # Out[4]: 13.97516637314112
output # Wektor własny
# po obliczeniu powyższych można przejśc do poszukiwania drugiej co do wielkości wartości własnej
# ============================================================
output /= np.linalg.norm(output)
x = np.copy(output)

arr = diagonalArray
output = np.ones(64)
inp = np.copy(output)
inp /= np.linalg.norm(inp)
inp -= x * (x.dot(inp))

while True:
    inp /= np.linalg.norm(inp)
    diagonalArray.calculate(arr, inp, output)
    inp = np.copy(output)
    inp -= x * (x.dot(inp))

    if np.linalg.norm(output - inp) < pow(10, -7):
        break

# ============================================================
np.linalg.norm(output) # Out[6]: 13.900452697733499
inp # Wektor własny drugi co do wielkości
# ============================================================