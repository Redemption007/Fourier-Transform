import tkinter as tkt
from variables import variables as var
from analyse import analyse

def change_state(widget=None, newstate=None, key=None):
    if key:
        var.var_dict[key]['value'] = not var.var_dict[key]['value']
    if newstate:
        if newstate!='disabled':
            widget.focus()
        else:
            widget.tk_focusPrev()
            widget['textvariable'] = 0
        widget["state"] = newstate
    elif widget:
        if ["state"] == ('normal' or 'active'):
            widget.tk_focusPrev()
            widget["state"] = 'disabled'
            widget['textvariable'] = 0
        else:
            widget.focus()
            widget["state"] = 'normal'

def set_amplitude(frame):
    amplitude = tkt.Frame(frame, width=var.w//2)

    label_amplitude = tkt.Label(amplitude, text = "A(t) = ", anchor=tkt.E)
    label_amplitude.grid(row=1, column=0)
    
    initial_amplitude = tkt.Entry(amplitude, name='initial_amp', width=4, textvariable=var.var_dict["initial_amp"]["value"], validate='focusout', validatecommand=(var.verif_mod, '%W', '%P', '%s'), invalidcommand=(var.error, '%W', '%P', '%s'))
    initial_amplitude.grid(row=1, column=1)
    
    label_exp = tkt.Label(amplitude, text = "* exp( -")
    label_exp.grid(row=1, column=2)
    
    damping = tkt.Entry(amplitude, name='damping', width=4, textvariable=var.var_dict["damping"]["value"], validate='focusout', validatecommand=(var.verif_mod, '%W', '%P', '%s'), invalidcommand=(var.error, '%W', '%P', '%s'))
    damping.grid(row=1, column=3)
    
    label_t = tkt.Label(amplitude, text = "* t )")
    label_t.grid(row=1, column=4)
    
    initial_amplitude.focus()
    amplitude.grid(row=1, column=0, sticky=tkt.EW, padx=20, pady=20, columnspan=2)
    return

def set_sinusoidale(frame):
    phase = tkt.Frame(frame, width=var.w//2)

    label_omega = tkt.Label(phase, text = "\u03c9 = ", anchor=tkt.E)
    label_omega.grid(row=0, column=0)
    
    omega = tkt.Entry(phase, name='w', width=4, textvariable=var.var_dict["w"]["value"], validate='focusout', validatecommand=(var.verif_mod, '%W', '%P', '%s'), invalidcommand=(var.error, '%W', '%P', '%s'))
    omega.grid(row=0, column=1)
    
    phase.grid(column=0, row=2, padx=20, sticky=tkt.W)
    #
    dephasage = tkt.Frame(frame, width=var.w//2)
    
    label_phi = tkt.Label(dephasage, text = "\u03c6 = ", anchor=tkt.E)
    label_phi.grid(row=0, column=3)
    
    phi = tkt.Entry(dephasage, name='phi', width=4, textvariable=var.var_dict["phi"]["value"], validate='focusout', validatecommand=(var.verif_mod, '%W', '%P', '%s'), invalidcommand=(var.error, '%W', '%P', '%s'))
    phi.grid(row=0, column=4, padx=10)
    
    dephasage.grid(column=1, row=2, sticky=tkt.W)
    return

def set_sampling(frame):
    samples = tkt.Frame(frame, width=var.w//2)

    label_samples = tkt.Label(samples, text = "Échantillonnage : ", anchor=tkt.E)
    label_samples.grid(row=0, column=0)
    sampling = tkt.Entry(samples, name='sampling', width= 4, textvariable=var.var_dict["sampling"]["value"], validate='focusout', validatecommand=(var.verif_mod, '%W', '%P', '%s'), invalidcommand=(var.error, '%W', '%P', '%s'))
    sampling.grid(row=0, column=1)

    label_periods = tkt.Label(samples, text = "Périodes : ", anchor=tkt.E)
    label_periods.grid(row=1, column=0)
    periods = tkt.Entry(samples, name='periods', width= 4, textvariable=var.var_dict["periods"]["value"], validate='focusout', validatecommand=(var.verif_mod, '%W', '%P', '%s'), invalidcommand=(var.error, '%W', '%P', '%s'))
    periods.grid(row=1, column=1)
    
    samples.grid(column=0, row=3, padx=20, sticky=tkt.EW, pady=20)

def set_infos(frame):
    infos = tkt.LabelFrame(frame, text="Informations :")

    label_samples = tkt.Label(infos, textvariable = var.samples_var, anchor=tkt.W)
    label_samples.grid(row=0, column=0)
    
    label_freq = tkt.Label(infos, textvariable = var.frequency_var, anchor=tkt.W)
    label_freq.grid(row=1, column=0)

    label_ratio = tkt.Label(infos, textvariable = var.signal_on_noise, anchor=tkt.W)
    label_ratio.grid(row=2, column=0)

    label_bin = tkt.Label(infos, textvariable = var.bins, anchor=tkt.W)
    label_bin.grid(row=3, column=0)
        
    infos.grid(column=1, row=3, padx=(0, 10), sticky='WNS')
    return

def set_options(frame):
    options_labelframe = tkt.LabelFrame(frame, text="Options :")
    
    random_holes_check = tkt.Checkbutton(options_labelframe, text='Trous aléatoires', command=lambda: change_state(random_num_entry, key='random_holes'))
    random_holes_check.grid(column=0, row=0, sticky='W')

    random_num_label = tkt.Label(options_labelframe, text="Nombre :")
    random_num_label.grid(column=1, row=0, sticky='E', padx=(20, 0))
    random_num_entry = tkt.Entry(options_labelframe, name='random_nb', width=4, textvariable=var.var_dict["random_nb"]["value"], state='disabled', validate='focusout', validatecommand=(var.verif_mod, '%W', '%P', '%s'), invalidcommand=(var.error, '%W', '%P', '%s'))
    random_num_entry.grid(column=2, row=0, sticky='W')

    def periodic_state():
        change_state(periodics_width_entry)
        change_state(periodics_freq_entry, key='periodic_holes')

    periodics_holes_check = tkt.Checkbutton(options_labelframe, text='Trous récurrents', command=lambda: periodic_state())
    periodics_holes_check.grid(column=0, row=1, sticky='W')
    
    periodics_freq_label = tkt.Label(options_labelframe, text="Fréquence :")
    periodics_freq_label.grid(column=1, row=1, sticky='E', padx=(20, 0))
    periodics_freq_entry = tkt.Entry(options_labelframe, name='periodic_f', width=4, textvariable=var.var_dict["periodic_f"]["value"], state='disabled', validate='focusout', validatecommand=(var.verif_mod, '%W', '%P', '%s'), invalidcommand=(var.error, '%W', '%P', '%s'))
    periodics_freq_entry.grid(column=2, row=1, sticky='W',)

    periodics_width_label = tkt.Label(options_labelframe, text="Largeur :")
    periodics_width_label.grid(column=1, row=2, sticky='E', padx=(20, 0))
    periodics_width_entry = tkt.Entry(options_labelframe, name='periodic_width', width=4, textvariable=var.var_dict["periodic_width"]["value"], state='disabled', validate='focusout', validatecommand=(var.verif_mod, '%W', '%P', '%s'), invalidcommand=(var.error, '%W', '%P', '%s'))
    periodics_width_entry.grid(column=2, row=2, sticky='W')
    
    zero_padding_check = tkt.Checkbutton(options_labelframe, text='Zero-Padding', command=lambda: change_state(zero_pad_entry, key='zero_padding'))
    zero_padding_check.grid(column=0, row=3, sticky='W')

    zero_pad_label = tkt.Label(options_labelframe, text="Nombre :")
    zero_pad_label.grid(column=1, row=3, sticky='E', padx=(20, 0))
    zero_pad_entry = tkt.Entry(options_labelframe, name='zp_nb', width=4, textvariable=var.var_dict["zp_nb"]["value"], state='disabled', validate='focusout', validatecommand=(var.verif_mod, '%W', '%P', '%s'), invalidcommand=(var.error, '%W', '%P', '%s'))
    zero_pad_entry.grid(column=2, row=3, sticky='W')

    barplot_check = tkt.Checkbutton(options_labelframe, text='Diagramme en barres', command=lambda: change_state(key='barplot'))
    barplot_check.grid(column=0, row=4, sticky='W')

    options_labelframe.grid(column=0, row=4, padx=20, ipadx=20, sticky=tkt.W, columnspan=2)
    return

def set_reexcitement(frame):
    reexcitement_labelframe = tkt.LabelFrame(frame, text='Ré-excitations :')
    reexcitement_labelframe.grid(column=0, row=5, columnspan=2, padx=20, ipadx=10, sticky=tkt.W, pady=20)

    randoms_frame = tkt.Frame(reexcitement_labelframe, width=var.w//2)
    randoms_frame.grid(column=1, row=1, sticky='EW')

    randoms_label = tkt.Label(randoms_frame, text="Nombre :")
    randoms_label.grid(column=0, row=0, sticky='E')
    randoms_entry = tkt.Entry(randoms_frame, name='reex_nb', width=4, textvariable=var.var_dict["reex_nb"]["value"], state='disabled', validate='focusout', validatecommand=(var.verif_mod, '%W', '%P', '%s'), invalidcommand=(var.error, '%W', '%P', '%s'))
    randoms_entry.grid(column=1, row=0, sticky='W')

    sill_frame = tkt.Frame(reexcitement_labelframe, width=var.w//2)
    sill_frame.grid(column=2, row=1, sticky='EW')

    sill_label = tkt.Label(sill_frame, text="Seuil :")
    sill_label.grid(column=0, row=0, sticky='E')
    sill_entry = tkt.Entry(sill_frame, name='reex_sill', width=4, textvariable=var.var_dict["reex_sill"]["value"], state='disabled', validate='focusout', validatecommand=(var.verif_mod, '%W', '%P', '%s'), invalidcommand=(var.error, '%W', '%P', '%s'))

    sill_entry.grid(column=1, row=0, sticky='W')

    def radio_choice():
        ch = choice.get()
        if ch==1:
            change_state(randoms_entry, newstate='normal')
            change_state(sill_entry, newstate='disabled')
            var.var_dict['reexcitement']['value'] = 'randoms'
        elif ch==2:
            change_state(sill_entry, newstate='normal')
            change_state(randoms_entry, newstate='disabled')
            var.var_dict['reexcitement']['value'] = 'periodics'
        else:
            change_state(sill_entry, newstate='disabled')
            change_state(randoms_entry, newstate='disabled')
            var.var_dict['reexcitement']['value'] = 'without'
        return

    choice = tkt.IntVar()
    radio_disabled = tkt.Radiobutton(reexcitement_labelframe, text='Désactivées', value=0, variable=choice, command=radio_choice)

    radio_randoms = tkt.Radiobutton(reexcitement_labelframe, text='Aléatoires', value=1, variable=choice, command=radio_choice)
    
    radio_periodics = tkt.Radiobutton(reexcitement_labelframe, text='En fin de période', value=2, variable=choice, command=radio_choice)

    radio_disabled.grid(column=0, row=0, ipadx=10, ipady=10)
    radio_periodics.grid(column=2, row=0, ipadx=10, ipady=10)
    radio_randoms.grid(column=1, row=0, ipadx=10, ipady=10)

    radio_disabled.select()
    return

def set_buttons(settings, window, glob):
    controls = tkt.Frame(settings, width=var.w//4, height=30)

    def begin():
        return set_graphs(glob, window)
    okay = tkt.Button(controls, text="OK", command=begin)
    okay.grid(row=0, column=0, sticky=tkt.EW)

    def exit_command():
        window.destroy()
        window.quit()
        exit(0)
    exit_button = tkt.Button(controls, text="Exit", command=exit_command)
    exit_button.grid(row=0, column=1, sticky=tkt.EW)

    controls.grid(column=0, row=6, columnspan=2)
    return

def set_settings(frame, window):
    settings = tkt.LabelFrame(frame, text="Réglages : ", height=var.h//2, width=var.w//2)

    settings.columnconfigure(0, weight=1)
    settings.columnconfigure(1, weight=1)
    
    label_signal = tkt.Label(settings, text = "Signal de la forme A(t)*sin(\u03c9*t+\u03c6)")
    label_signal.grid(row=0, column=0, columnspan=2, sticky=tkt.EW)

    set_amplitude(settings)
    set_sinusoidale(settings)
    set_sampling(settings)
    set_infos(settings)
    set_options(settings)
    set_reexcitement(settings)
    set_buttons(settings, window, frame)
    
    settings.grid(column=0, row=0, pady = (0, 10), padx = (0, 10), sticky='EWNS')
    return

def set_graphs(frame, window):

    try:
        W = window.winfo_pathname(window.focus_get().winfo_id())
    except AttributeError:
        W = '.'
    if W != '.' and W.find('canvas') == -1:
        if not var.verif_modif(W):
            return var.show_error(W)

    graphs = tkt.Frame(frame, width=var.w//2, height=var.h)
    graphs.grid(column=1, row=0, rowspan=2, sticky='EWNS')

    graphs.rowconfigure(0, minsize=var.h//2)
    graphs.rowconfigure(1, minsize=var.h//2)

    graph_1 = tkt.Frame(graphs, bg="#ff0000", width=var.w//2, height=var.h//2)
    graph_1.grid(column=0, row=0, sticky='EWNS')

    graph_2 = tkt.Frame(graphs, bg="#00ff00", width=var.w//2, height=var.h//2)
    graph_2.grid(column=0, row=1, sticky='EWNS')

    signal_graph = tkt.Frame(frame, bg="#ff0000", width=var.w//2, height=var.h//2)
    signal_graph.grid(column=0, row=1, sticky='EWNS')

    return analyse(signal_graph, graph_1, graph_2)

def set_glob(window):

    glob = tkt.Frame(window, height=var.h, width=var.w)
    
    glob.columnconfigure(0, weight=1)
    glob.columnconfigure(1, weight=1)
    glob.rowconfigure(0, minsize=int(var.h*4/7))
    glob.rowconfigure(1, minsize=int(var.h*3/7))

    set_settings(glob, window)
    set_graphs(glob, window)

    def exit_command(event=None):
        window.destroy()
        window.quit()
        exit()

    glob.grid()
    glob.bind_all('<Shift-E>', exit_command)
    return
