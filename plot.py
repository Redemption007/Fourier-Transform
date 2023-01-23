from variables import signal_on_noise
import matplotlib

matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from numpy import argmax, amax, absolute, arange

# Ajustement des axes d'un graphique à l'origine
def ajust_axes(ax):
    ax.spines['right'].set_position('zero')
    ax.spines['top'].set_position('zero')
    ax.spines['left'].set_color('none')
    ax.spines['bottom'].set_color('none')
    ax.legend()
    ax.grid()

def graph_signal(graph, x, signal, amp_max, time):

    old_graphs = plt.get_fignums()
    for g in old_graphs:
        plt.close(g)
    print("{} graphs closed.".format(old_graphs.__len__()))

    # Construction de la figure
    fig = plt.figure()
    axes = fig.add_subplot(111)

    #Affichage du subplot
    axes.plot(x, signal, linewidth=2, label="y(t) = sin(w*t+phi)", color='#0000ff')
    axes.set(xlim=(0, time), ylim=(-amp_max-0.4, amp_max+0.4), xlabel='t (en s)', title='Signal sinusoïdal')

    ajust_axes(axes)
    
    plt.gcf().subplots_adjust(left = 0.088, bottom = 0.55, right = 0.96, top = 0.9)

    figure_canvas = FigureCanvasTkAgg(fig, master=graph)

    figure_canvas.get_tk_widget().grid(sticky='EWNS')

def graph_details(graph, x, y, nu):
    # Construction de la figure
    fig = plt.figure()
    axes = fig.add_subplot(111)

    #Affichage du subplot
    axes.plot(x, y.imag, linewidth=2, label= "Im(F(y))", color='#ff0000')
    axes.plot(x, y.real, linewidth=2, label= "Re(F(y))", color='#00ff00')
    axes.set(xlim=(0, 2*nu), xlabel='Fréquence v (en Hz)', ylabel='Amplitude (unité arbitraire)', title='Transformée de Fourier de y(t)')

    ajust_axes(axes)
    plt.gcf().subplots_adjust(left = 0.088, bottom = 0.37, right = 0.993, top = 0.95)

    figure_canvas = FigureCanvasTkAgg(fig, master=graph)

    figure_canvas.get_tk_widget().grid(sticky='EWNS')

def transfo_fourier(graph, barplot, x, y, nu, Z, x_id, y_id):
    fig = plt.figure()
    axes = fig.add_subplot(111)
    # On passe le tout en densité spectrale de puissance
    #psd = (absolute(absolute(y))**2)*nu/Z
    #psd_id = (absolute(absolute(y_id))**2)*nu/int(Z)
    psd = absolute(y)
    psd_id = absolute(y_id)
    if barplot:
        axes.bar(x=arange(x_id.size), height=psd_id.tolist(), width=int(1/nu), align='center')
        axes.bar(x=arange(x.size), height=psd.tolist(), align='center')
    else:
        # Affichage de la transformée finale
        axes.plot(x_id, psd_id, '-r')
        axes.plot(x, psd, 'x-k')

    pic(x, psd)
    signal_on_noise.set("Ratio Signal/Bruit : {}".format("%.3E"%ratio(psd)))

    axes.set(xlim=(0, 5*nu), xlabel="Fréquence v (Hz)", ylabel="Densité spectrale de puissance psd(v)", title="Densité spectrale de puissance normalisée")
    axes.grid()

    plt.gcf().subplots_adjust(left = 0.088, right = 0.993, top = 0.848, bottom=0.2)

    figure_canvas = FigureCanvasTkAgg(fig, master=graph)
    figure_canvas.get_tk_widget().grid(sticky='EW')

def pic(x, y):
    # Signalisation du pic fréquentiel, partie verticale
    plt.stem(x[argmax(y)], amax(y), markerfmt='rx', linefmt='k--', orientation='vertical')
    plt.text(x[argmax(y)], 0, '\n\n{}'.format('%.3f'%x[argmax(y)]), horizontalalignment = 'center', verticalalignment = 'top')

    # Signalisation du pic fréquentiel, partie horizontale
    plt.stem(amax(y), x[argmax(y)], markerfmt='rx', linefmt='k--', orientation='horizontal')
    plt.text(0, amax(y), '   {}'.format('%.3f'%amax(y)), horizontalalignment = 'left', verticalalignment = 'bottom')

def ratio(y):
    average = 0
    center = margin = y.size//100
    if argmax(y)<y.size/2:
        center = argmax(y)+y.size//2-margin
    else:
        center = argmax(y)-y.size//2+margin
    noise = y[center-margin:center+margin:1]
    for i in noise:
        average += i
    average /= 2*margin
    signal = argmax(y)
    return signal/average