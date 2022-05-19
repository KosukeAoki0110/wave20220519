import matplotlib.pyplot as plt
import numpy as np

#reading NOWPHAS data and cutting data (20min each to 3H each)

table = np.loadtxt('SH604e.s2112.txt')
i = 0
for i in range(0,2231):
    P = table[i]
    hoge = P[0]
    Y1 = P[2]
    if hoge == 9:
        Pold = table[i-1]
        Pnew = table[i+1]
        Y1 = (Pold[2] + Pnew[2]) / 2
    Y1 = str(Y1)
    Y2 = P[3]
    if hoge == 9:
        Pold = table[i-1]
        new = table[i+1]
        Y2 = (Pold[3] + Pnew[3]) / 2
    Y2 = str(Y2)
    J = np.mod(i,9)
    if J == 0:
        f = open('Z_RUM12.txt', 'a')
        f.write(Y1)
        f.write(' ')
        f.write(Y2)
        f.write('\n')
    i += 1



