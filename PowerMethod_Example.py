# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 17:08:12 2017

@author: SoliareOfAstora
"""
import numpy as np
import math


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
temp = np.ones(64)
output = np.ones(64)
i = 0
while True:

    temp = np.copy(output)
    diagonalArray.calculate(arr, temp, output)
    output /= np.linalg.norm(output)

    if np.linalg.norm(output - temp) < pow(10, -7):
        break

diagonalArray.calculate(arr, temp, output)
np.linalg.norm(output)

# ============================================================
arr = diagonalArray
temp = np.ones(64)
output = np.ones(64)
diagonalArray.calculate(arr, temp, output)
x = np.random.randn(64)
x -= x.dot(output) * output / np.linalg.norm(output) ** 2
while True:
    x -= x.dot(output) * output / np.linalg.norm(output) ** 2
    temp = np.copy(output)
    temp -= x*x.dot(temp)
    diagonalArray.calculate(arr, temp, output)
    output /= np.linalg.norm(output)
    temp /= np.linalg.norm(temp)
    if np.linalg.norm(output - temp) < pow(10, -5):
        break

diagonalArray.calculate(arr, temp, output)
np.linalg.norm(output)


13.97516637314112


13.901095366671019