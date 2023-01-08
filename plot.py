import matplotlib.pyplot as plt
from numpy import argmax, amax
from math import trunc

def graph(f_freq, f_y, x, signal, time, nu):
    # Construction de la figure et subdivision en trois graphiques
    fig = plt.figure(layout='constrained')
    axes1 = fig.add_subplot(221)
    axes2 = fig.add_subplot(223)
    axes3 = fig.add_subplot(224)
    axes4 = fig.add_subplot(222)

    # Ajustement des axes d'un graphique au centre
    def ajust_axes(axs):
        for ax in axs:
            ax.spines['right'].set_position('zero')
            ax.spines['top'].set_position('zero')
            ax.spines['left'].set_color('none')
            ax.spines['bottom'].set_color('none')
            ax.legend()
            ax.grid()

    #Affichage des subplots
    axes1.plot(x, signal, linewidth=2, label="y = sin(w*x+phi)", color='#0000ff')
    axes1.set(xlim=(0, time), ylim=(-1.4, 1.4), xlabel='x (en s)', title='Signal sinusoïdal simple')

    axes2.plot(f_freq, f_y.real, linewidth=2, label= "Re(F(y))", color='#00ff00')
    axes2.set(xlim=(-2*nu, 2*nu), xlabel='Fréquence v (en Hz)', ylabel='Amplitude (unité arbitraire)', title='Partie réelle de la transformée\nde Fourier de y(x)')

    axes3.plot(f_freq, f_y.imag, linewidth=2, label= "Im(F(y))", color='#ff0000')
    axes3.set(xlim=(-2*nu, 2*nu), xlabel='Fréquence v (en Hz)', ylabel='Amplitude (unité arbitraire)', title='Partie imaginaire de la transformée\nde Fourier de y(x)')

    axes4.plot(f_freq, f_y.imag, linewidth=2, label= "Im(F(y))", color='#ff0000')
    axes4.plot(f_freq, f_y.real, linewidth=2, label= "Re(F(y))", color='#00ff00')
    axes4.set(xlim=(-2*nu, 2*nu), xlabel='Fréquence v (en Hz)', ylabel='Amplitude (unité arbitraire)', title='Transformée de Fourier de y(x)')

    ajust_axes([axes1, axes2, axes3, axes4])

    plt.show()

def transfo_fourier(f_freq, f_y, N, nu):
    # On garde les fréquences positives et on s'intéresse à leurs amplitude en valeur absolue
    freq = f_freq[:int(N/2)]
    amp = abs(f_y[:int(N/2)])
    # Cette amplitude doit être normalisée pour correspondre à notre amplitude de départ A_0=1, qu'elle atteindra en 𝜈 = w .
    amp_normale = amp/amax(amp)

    # Affichage de la transformée finale
    plt.plot(freq, amp_normale)
    plt.stem(freq[argmax(amp_normale)], amax(amp_normale), markerfmt='k+', linefmt='k--')
    plt.text(freq[argmax(amp_normale)], 0, '{}'.format(trunc(1000*freq[argmax(amp_normale)])/1000), horizontalalignment = 'center', verticalalignment = 'top')
    plt.xlim(0, 5*nu)
    plt.grid()
    plt.xlabel("Fréquence v (Hz)")
    plt.ylabel("Amplitude A(v)")
    plt.title("Transformée de Fourier positive normalisée par  a={}".format((trunc(10000/amax(amp)))/10000))
    plt.show()
