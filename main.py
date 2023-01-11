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
nb_holes, holes_width, holes_freq = interface.ask_holes(N)

t = np.linspace(0, total_time, N)
t_ideal = np.linspace(0, int(Z)/nu, N)
# On définit notre fonction y
y = lambda x: A*np.exp(-x*B)*np.sin(w*x+phi)
# On corrompt notre fonction en y ajoutant des trous arbitraires et aléatoires
# On corrompt notre fonction en y ajoutant éventuellement des trous
signal = corrupteur.corruption(y, t, nb_holes, holes_width, holes_freq)
signal_ideal = A*np.sin(w*t+phi)

print("\nOn travaille avec l'équation suivante :\ny(t) = {}*exp(-{}*t) * sin({} * t + {})\ny(t) = A(t)*sin(w*t+phi)".format(A, B, w, phi))

# Fréquences de la transformée de Fourier
f_freq = np.fft.fftfreq(signal.size, sampling)
f_freq_ideal = np.fft.fftfreq(signal_ideal.size, sampling)

# On calcule la transformée de Fourier de la fonction y
f_y = np.fft.fft(signal, norm="forward")
f_y_ideal = np.fft.fft(signal_ideal, norm="forward")
# Utilisation d'une normalisation par 1/n via le mot-clé "forward"

plot.graph(f_freq, f_y, t, signal, A, total_time, nu)

print("La fréquence de cette sinusoïde est de nu = {} Hz. Intéressons-nous alors plus précisément au spectre de fréquences.".format(int(nu*1000)/1000))

plot.transfo_fourier(f_freq, f_y, N, nu, f_freq_ideal, f_y_ideal)

concludes(A, Z, nb_holes)

#%%

'''
Prochaines étapes :

- faire du zéro padding (se renseigner)
'''