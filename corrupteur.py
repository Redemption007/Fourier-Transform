from numpy import nonzero, delete, tile
from random import random

def corruption(func, x, nb_trous=0, width=0, freq=0):
    corr = temp = func(x)
    if width :
        index = 0
        while index<corr.size :
            if index+width>corr.size :
                #on remplace le nombre restant de points par des zéros
                hole = tile(0, corr.size-index)
                corr[index:] = hole
                continue
            #on remplace le nombre width de points par 0
            hole = tile(0, width)
            corr[index:index+width] = hole
            index+=freq
    if nb_trous :
        while (corr.size-temp.size<nb_trous):
            index1 = int(random()*temp.size)
            index2 = nonzero(corr == temp[index1])[0][0]
            corr[index2] = 0
            temp = delete(temp, index1)
    return corr
    