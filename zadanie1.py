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

    def copy(self, rownumber, diagonal):
        self.x = diagonal.x
        self.row = rownumber



a = Diagonal()
a.setNumbers(0, [4, 8, 4, 3, 4, 5, 2, 8, 5])

b = Diagonal()
b.setNumbers(-1, [2, 1, 1, 2, 1, 2, 1, 2])

c = Diagonal()
c.copy(0, b)

result = np.array([1,2,3,4,5,6,7,8,9])

for x in range(0, 9):
    print(x
          ,b.getNumber(x)
     ,a.getNumber(x)
    ,c.getNumber(x))
