from numpy import array, concatenate, where, arange
from random import random

def random_reexcitement(num, max) :
    #on refixe brutalement l'amplitude à A(0) en des points randoms
    liste = [0]
    for i in range(0, num):
        point = int(random()*(max-1))
        liste.append(point)
    liste.sort()
    liste.append(max-1)
    return liste

def periodic_reexcitement(seuil, max) :
    #on se donne un seuil tel qu'au delà de ce seuil, l'amplitude revienne brutalement au maximum
    nb = max//seuil
    liste = []
    for i in range(0, nb+1):
        point = seuil*i
        liste.append(point)
    liste.append(max-1)
    return liste

def reexcitement(a, t, val) :
    reex = val['reexcitement']
    nb = val['reex_nb']
    sill = val['reex_sill']
    #on récupère une liste de points des fonctions ci-dessus et on boucle en applicant a(t-i)
    # (d'où la nécessité que la liste finisse toujours par le dernier échantillon)
    if reex=='without':
        liste = [0, t.size]
    elif reex=='randoms':
        liste = random_reexcitement(nb, t.size)
    else :
        a_p = a(t)
        seuil = where(a_p<sill)
        liste = periodic_reexcitement(seuil[0][0], t.size)
    print("La liste des points de réexcitation est : {}".format(liste))
    i=0
    amp = array([a(0)])
    for index in liste :
        if index==0:
            continue
        interval = t[1:index-liste[i]+1]
        a_i = a(interval)
        amp = concatenate((amp, a_i))
        i+=1
    return amp