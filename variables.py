from numpy import pi
from tkinter import Tk, messagebox, StringVar, IntVar, DoubleVar

window = Tk()

w = window.winfo_screenwidth()
h = window.winfo_screenheight()

var_dict = {
    'barplot': {'value': False, 'type': bool, 'cond': ['boolean']},

    'initial_amp': {'value': DoubleVar(value=5), 'type': float, 'cond':['positive']},

    'damping': {'value': DoubleVar(value=0), 'type': float, 'cond':['posinull']},

    'w': {'value': DoubleVar(value=1), 'type': float, 'cond':['positive']},

    'phi': {'value': DoubleVar(value=pi), 'type': float, 'cond':['posinull', 'periodic']},

    'sampling': {'value': DoubleVar(value=0.01), 'type': float, 'cond':['positive']},

    'periods': {'value': DoubleVar(value=30), 'type': float, 'cond':['positive']},

    'random_holes': {'value': False, 'type': bool, 'cond':['boolean']},

    'random_nb': {'value': IntVar(value=30), 'type': float, 'cond':['positive', 'integer', 'in scale']},

    'periodic_holes': {'value': False, 'type': bool, 'cond':['boolean']},

    'periodic_f': {'value': IntVar(value=500), 'type': float, 'cond':['positive', 'integer', 'non constant', 'in scale']},

    'periodic_width': {'value': IntVar(value=10), 'type': float, 'cond':['positive', 'integer', 'in scale']},

    'zero_padding': {'value': False, 'type': bool, 'cond':['boolean']},

    'zp_nb': {'value': IntVar(value=5), 'type': float, 'cond':['positive', 'integer']},

    'reexcitement': {'value': StringVar(value='without'), 'type': str, 'cond': ['compatible', 'signal damped']},

    'reex_nb': {'value': IntVar(value=1), 'type': float, 'cond':['positive', 'integer', 'signal damped']},

    'reex_sill': {'value': DoubleVar(value=0.5), 'type': float, 'cond':['positive', 'reachable', 'signal damped']}
}

periods = (var_dict['periods']['value']).get()
omega = (var_dict['w']['value']).get()
sampling = (var_dict['sampling']['value']).get()
frequency = omega/(2*pi)
samples = int(periods/(frequency*sampling))
samples_var = StringVar(value="Échantillons : {}".format(samples))
frequency_var = StringVar(value="Fréquence : {}".format('%.3f'%frequency))
signal_on_noise = StringVar(value="Ratio Signal/Bruit :")
bins = StringVar(value="Fréquence de bin :")

def verif_modif(W, value=None, before=None, show=False):
    widget = window.nametowidget(W)
    name = W.split('.')[-1]
    if widget['state']=='disabled':
        return True
    if not value:
        value = widget.get()
    #accessing properties of the variable
    v_type = var_dict[name]['type']
    v_cond = var_dict[name]['cond']

    try:
        v = v_type(value)
    except ValueError:
        if show:
            return 'type'
        return False
    conditions = {
        'positive': v > 0,
        'posinull': v >= 0,
        'integer': v.is_integer(),
        'periodic': v < 2*pi,
        'boolean': v == ('True'or 'False'),
        'compatible': v == ('without' or 'randoms' or 'periodics'),
        'in scale': v < samples,
        'non constant': v > (var_dict["periodic_width"]['value']).get(),
        'reachable': v < (var_dict["initial_amp"]['value']).get(),
        'signal damped': (var_dict['damping']['value']).get()>0
    }
    for c in v_cond:
        if not conditions[c]:
            if show:
                return c
            return False
    if before != v:
        liste = ['periods', 'w', 'sampling']
        if name in liste:
            periods_updated = (var_dict['periods']['value']).get()
            omega_updated = (var_dict['w']['value']).get()
            sampling_updated = (var_dict['sampling']['value']).get()
            frequency_updated = omega_updated/(2*pi)
            samples_updated = int(periods_updated/(frequency_updated*sampling_updated))
            samples_var.set("Total : {} échantillons".format(samples_updated))
            frequency_var.set("Fréquence : {} Hz".format('%.3f'%frequency_updated))
    return True

def show_error(W, value=None, before=None):
    widget = window.nametowidget(W)
    name = W.split('.')[-1]
    if not value:
        value = widget.get()
    descriptions = {
        'positive': "Le nombre entré doit nécessairement être strictement positif.",
        'posinull': "Le nombre entré doit nécessairement être positif ou nul.",
        'integer': "Le nombre entré doit être un entier.",
        'periodic': "Le nombre entré doit être inférieur à 2\u03c0.",
        'boolean': "Il faut entrer un booléen.",
        'compatible': "La valeur doit être 'without' ou 'randoms' ou 'periodics'.",
        'in scale': "Le nombre entré doit être plus petit que le nombre total d'échantillons ({}).".format(int((var_dict['periods']['value']).get()*2*pi/((var_dict['w']['value']).get()*(var_dict['sampling']['value']).get()))),
        'non constant': "Le nombre entré doit être supérieur à la largeur des trous périodiques.",
        'reachable': "Le nombre entré doit être inférieur à l'amplitude initiale.",
        'signal damped': "Vous devez d'abord fixer un amortissement strictement positif !",
        'type': "Le type ({}) ne correspond pas. Type attendu : {}".format(type(value), var_dict[name]['type'])
    }
    origin = verif_modif(W, show=True)
    widget.focus()
    if before:
        (var_dict[name]['value']).set(before)
    return messagebox.showerror(title="Valeur incorrecte !", icon=messagebox.WARNING,
    message="Oups !\n{} n'est pas une valeur possible pour {} !\n\n{}".format(value, name, descriptions[origin]))

def get_values():
    values = {}
    for key in var_dict:
        try:
            values[key] = (var_dict[key]['value']).get()
        except AttributeError:
            values[key] = var_dict[key]['value']

    values['freq'] = values['w']/(2*pi)
    values['samples'] = int(values['periods']/(values['freq']*values['sampling']))
    return values

verif_mod = window.register(verif_modif)
error = window.register(show_error)

class Object():
    "Just a wrapper"
variables = Object()
variables.h = h
variables.w = w
variables.var_dict = var_dict
variables.samples_var = samples_var
variables.frequency_var = frequency_var
variables.signal_on_noise = signal_on_noise
variables.bins = bins
variables.verif_mod = verif_mod
variables.error = error
variables.verif_modif = verif_modif
variables.show_error = show_error
