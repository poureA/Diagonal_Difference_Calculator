import numpy as np
class Diagonal(object):
    '''class docstring'''
    def __init__(self,matrix)->None:
        self.m = matrix
    def corners(self)->int:
        '''sum of corners values'''
        return self.m[0][0]+self.m[0][-1]+self.m[-1][0]+self.m[-1][-1]
    def avgvalue(self)->float:
        '''average value of all values'''
        Sum = 0
        c = 0
        for i in self.m :
            for j in i :
                Sum+=j
                c+=1
        return Sum/c
matrix = []
carrier = []
row = int(input('enter number of rows :'))
col = int(input('enter number of columns :'))
for i in range(row):
    for j in range(col):
        ask =  int(input('number :'))
        carrier.append(ask)
    matrix.append(carrier)
    carrier = []
mtrx = np.array(matrix)
print(mtrx)
sample = Diagonal(mtrx)
print(sample.corners(),sample.avgvalue(),sep='  ')
exit = input('enter any key to exit :')
