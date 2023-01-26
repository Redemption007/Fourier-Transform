import numpy as np
import plot
import corrupteur
import excitement
from variables import get_values


def analyse(signal_graph, graph_1, graph_2):
    val = get_values()

    if not val['zero_padding']:
        val['zp_nb'] = 0
    total_time = val['periods']/val['freq']
    N = int(total_time/val['sampling'])
    t = np.linspace(0, total_time, N)
    t_ideal = np.linspace(0, int(val['periods'])/val['freq'], N)
    # On définit notre fonction y
    y = lambda x: np.sin(val['w']*x+val['phi'])
    # On définit notre amplitude dépendante du temps
    a = lambda x: val['initial_amp']*np.exp(-x*val['damping'])

    # On corrompt notre fonction en y ajoutant éventuellement
    # des trous ou des réexcitations
    signal = excitement.reexcitement(a, t, val) * corrupteur.corruption(y, t, val)
    signal_ideal = val['initial_amp']*np.sin(val['w']*t_ideal+val['phi'])
    # On zero pad le signal si besoin
    if val['zero_padding'] :
        t = np.linspace(0, total_time*(1+val['zp_nb']), N*(1+val['zp_nb']))
        signal = np.concatenate((signal, np.tile(0, signal.size*val['zp_nb'])))
        signal_ideal = np.concatenate((signal_ideal, np.tile(0, signal_ideal.size*val['zp_nb'])))
        total_time *= val['zp_nb']+1

    # Fréquences de la transformée de Fourier
    f_freq = np.fft.rfftfreq(signal.size, val['sampling'])
    f_freq_ideal = np.fft.rfftfreq(signal_ideal.size, val['sampling'])

    # On calcule la transformée de Fourier de la fonction y
    f_y = np.fft.rfft(signal, norm="forward")*(val['zp_nb']+1)
    f_y_ideal = np.fft.rfft(signal_ideal, norm="forward")*(val['zp_nb']+1)
    # Utilisation d'une normalisation par 1/n via le mot-clé "forward"

    plot.graph_signal(signal_graph, t, signal, val['initial_amp'], total_time)

    plot.graph_details(graph_2, f_freq, f_y, val['freq'])

    plot.graph_psd(graph_1, val['barplot'], f_freq, f_y, val['freq'], val['periods'], f_freq_ideal, f_y_ideal)
