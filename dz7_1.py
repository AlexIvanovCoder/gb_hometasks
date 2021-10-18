class Matrix:
    def __init__(self, mtrx):
        self.mtrx = mtrx

    def __add__(self, other):
        lst_of_lsts = []
        for i in range(len(self.mtrx)):
            lst = []
            for j in range(len(self.mtrx[i])):
                a = self.mtrx[i][j] + other.mtrx[i][j]
                lst.append(a)
            lst_of_lsts.append(lst)
        return Matrix(lst_of_lsts)

    def __str__(self):
        # convert all the  elements to string for the further printing
        lst = [list(map(str, j)) for j in self.mtrx]
        # Find maximal length of all elements in list
        n = max(len(x) for l in lst for x in l)
        # Print the rows
        a = '\n'.join([''.join(x.ljust(n + 2) for x in row) for row in lst])
        return a


obj1 = Matrix([[1, 2, 3553], [4, 5, 6], [7, 8, 19]])
obj2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

print(obj1)
print(obj2)
print(obj1 + obj2)
