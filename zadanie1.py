import numpy as np


class Diagonal:
    x =np.array([])
    row = 0

    def setNumbers(self, rownumber, vector):
        self.x = vector
        self.row = rownumber

    def getNumber(self, rownumber):
        if rownumber + self.row >= 0:
            return self.x[0, rownumber - self.row]

    def copy(self, rownumber, diagonal):
        self.x = diagonal.x
        self.row = rownumber

a = Diagonal()
a.setNumbers(0,[4,8,4,3,4,5,2,8,5])

b=Diagonal()
b.setNumbers(-1,)