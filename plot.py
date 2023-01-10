import matplotlib.pyplot as plt
from numpy import argmax, amax
from math import trunc

def graph(f_freq, f_y, x, signal, amp_max, time, nu):
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
    axes1.plot(x, signal, linewidth=2, label="y(t) = sin(w*t+phi)", color='#0000ff')
    axes1.set(xlim=(0, time), ylim=(amp_max-0.4, amp_max+0.4), xlabel='t (en s)', title='Signal sinusoïdal simple')

    axes2.plot(f_freq, f_y.real, linewidth=2, label= "Re(F(y))", color='#00ff00')
    axes2.set(xlim=(-2*nu, 2*nu), xlabel='Fréquence v (en Hz)', ylabel='Amplitude (unité arbitraire)', title='Partie réelle de la transformée\nde Fourier de y(t)')

    axes3.plot(f_freq, f_y.imag, linewidth=2, label= "Im(F(y))", color='#ff0000')
    axes3.set(xlim=(-2*nu, 2*nu), xlabel='Fréquence v (en Hz)', ylabel='Amplitude (unité arbitraire)', title='Partie imaginaire de la transformée\nde Fourier de y(t)')

    axes4.plot(f_freq, f_y.imag, linewidth=2, label= "Im(F(y))", color='#ff0000')
    axes4.plot(f_freq, f_y.real, linewidth=2, label= "Re(F(y))", color='#00ff00')
    axes4.set(xlim=(-2*nu, 2*nu), xlabel='Fréquence v (en Hz)', ylabel='Amplitude (unité arbitraire)', title='Transformée de Fourier de y(t)')

    ajust_axes([axes1, axes2, axes3, axes4])

    plt.show()

def transfo_fourier(f_freq, f_y, N, nu, f_freq_id, f_y_id):
    # On garde les fréquences positives et on s'intéresse à leurs amplitude en valeur absolue
    freq = f_freq[:int(N/2)]
    amp = abs(f_y[:int(N/2)])
    freq_id = f_freq_id[:int(N/2)]
    amp_id = abs(f_y_id[:int(N/2)])
    # Affichage de la transformée finale
    plt.plot(freq_id, amp_id, 'x-r')
    plt.plot(freq, amp, 'x-k')

    # Signalisation du pic fréquentiel, partie verticale
    plt.stem(freq[argmax(amp)], amax(amp), markerfmt='rx', linefmt='k--', orientation='vertical')
    plt.text(freq[argmax(amp)], 0, '{}'.format(trunc(1000*freq[argmax(amp)])/1000), horizontalalignment = 'center', verticalalignment = 'top')
    # Signalisation du pic fréquentiel, partie horizontale
    plt.stem(amax(amp), freq[argmax(amp)], markerfmt='rx', linefmt='k--', orientation='horizontal')
    plt.text(0, amax(amp), '{}'.format(trunc(1000*amax(amp))/1000), horizontalalignment = 'left', verticalalignment = 'bottom')

    plt.xlim(0, 5*nu)
    plt.grid()
    plt.xlabel("Fréquence v (Hz)")
    plt.ylabel("Amplitude A(v)")
    plt.title("Transformée de Fourier positive normalisée par  a=1/N={}".format(trunc(10000/N)/10000))
    plt.show()
