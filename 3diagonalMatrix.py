import numpy as np


class Diagonal:
    x = np.array([])
    row = 0

    def setNumbers(self, rownumber, vector):
        self.x = vector
        self.row = rownumber

    def getNumber(self, rownumber):
        temp = rownumber + self.row
        if temp >= 0:
            if temp < np.size(self.x):
                return self.x[temp]
            else:
                return 0
        else:
            return 0


d1 = Diagonal()
d1.setNumbers(0, [4, 8, 4, 3, 4, 5, 2, 8, 5])

d0 = Diagonal()
d0.setNumbers(-1, [2, 1, 1, 2, 1, 2, 1, 2])

b = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

a = np.zeros((9,9))

for x in range(0, 9):
    a[x,x]=d1.getNumber(x)
    if x>0:
        a[x-1,x]=d0.getNumber(x)
        a[x,x-1]=d0.getNumber(x)
        