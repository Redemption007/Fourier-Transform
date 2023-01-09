#%%
import numpy as np
from random import random
import plot
import interface
import corrupteur
from conclusions import concludes

# On définit notre amplitude arbitrairement :
A, B = interface.ask_amplitude()
# On définit la pulsation aléatoirement à 10ˆ-3 près
w = int(1000*(1+2*random()))/1000
# On définit à partir de celle-ci la fréquence
nu = w/(2*np.pi)
# Puis le déphasage aléatoirement à 10ˆ-3 près
phi = int(1000*random()/nu)/1000

# Temps de mesure dépendant de l'utilisateur
Z = interface.ask_phases()
total_time = Z/nu
#Période d'échantillonnage :
sampling = 0.010

#Nombre d'échantillons :
N = int(total_time/sampling) + 1

# Nombre de trous :
nb_holes = interface.ask_holes(N)

t = np.linspace(0, total_time, N)
# On définit notre fonction y
y = lambda x: np.exp(-x*A)*np.sin(w*x+phi)
# On corrompt notre fonction en y ajoutant des trous arbitraires et aléatoires
signal = corrupteur.corruption(y, nb_holes, t)

print("\nOn travaille avec l'équation suivante :\ny(x) = exp({}*x) * sin({} * x + {})\ny(x) = A*sin(w*x+phi)".format(A, w, phi))

# Fréquences de la transformée de Fourier
f_freq = np.fft.fftfreq(signal.size, sampling)

# On calcule la transformée de Fourier de la fonction y
f_y = np.fft.fft(signal)

plot.graph(f_freq, f_y, t, signal, total_time, nu)

print("La fréquence de cette sinusoïde est de nu = {} Hz. Intéressons-nous alors plus précisément au spectre de fréquences.".format(int(nu*1000)/1000))

plot.transfo_fourier(f_freq, f_y, N, nu)

concludes(A, Z, nb_holes)

#%%

'''
Prochaines étapes :

- faire du zéro padding (se renseigner)
'''