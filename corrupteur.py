from numpy import nonzero, delete, tile
from random import random

def corruption(func, x, val):
    random_holes = val['random_holes']
    periodic_holes = val['periodic_holes']
    random_nb = val['random_nb']
    periodic_f = val['periodic_f']
    periodic_width = val['periodic_width']
    corr = temp = func(x)
    if periodic_holes :
        index = 0
        while index<corr.size :
            if index+periodic_width>corr.size :
                #on remplace le nombre restant de points par des zéros
                hole = tile(0, corr.size-index)
                corr[index:] = hole
                continue
            #on remplace le nombre width de points par 0
            hole = tile(0, periodic_width)
            corr[index:index+periodic_width] = hole
            index+=periodic_f
    if random_holes :
        while (corr.size-temp.size<random_nb):
            index1 = int(random()*temp.size)
            index2 = nonzero(corr == temp[index1])[0][0]
            corr[index2] = 0
            temp = delete(temp, index1)
    return corr
    