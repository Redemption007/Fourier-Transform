from numpy import nonzero, delete
from random import random

def corruption(func, nb_trous, x):
    corr = temp = func(x)
    while (corr.size-temp.size<nb_trous):
        index1 = int(random()*temp.size)
        index2 = nonzero(corr == temp[index1])[0][0]
        corr[index2] = 0
        temp = delete(temp, index1)
    return corr
