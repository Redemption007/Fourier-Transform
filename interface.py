from re import search
def ask_amplitude():
    answer = input("Le signal doit-il être amorti ?\nRéponses acceptées :\nOui, Yes, Y, 1\nNo, Non, N, 0, Cancel")
    non = search("^(((N|n)*((O|o)*)*(N|n)*)|0*|(Cancel)?)$", answer)
    s=''
    lamb = 0
    if (non):
        print("Le signal n'est pas amorti.")
    else:
        while lamb<=0:
            try:
                lamb = float(input("{}Saisissez la valeur souhaitée de l'amortissement : ce nombre doit être décimal, strictememt supérieur à 0".format(s)))
            except ValueError:
                pass
            finally:
                s = 'Vous devez nécessairement entrer un nombre en chiffres, strictement supérieur à 0. Exemples : 13.55 ou 0.003\n'
                print("Le coefficient d'amortissement sera de {}.".format(lamb))
        s = ''
    amp_t0 = 0
    while amp_t0<=0:
        try:
            amp_t0 = float(input("{}Saisissez la valeur souhaitée de l'amplitude à l'origine : ce nombre doit être décimal, strictememt supérieur à 0".format(s)))
        except ValueError:
            pass
        finally:
            s = 'Vous devez nécessairement entrer un nombre en chiffres, strictement supérieur à 0. Exemples : 13.55 ou 0.003\n'
    print("L'amplitude à l'origine sera de {}. L'amplitude dépendant du temps sera donc égale à {}*exp(-{}t)".format(amp_t0, amp_t0, lamb))
    return amp_t0, lamb

def ask_phases():
    Z = 0
    s = ''
    while Z<=0 :
        try:
            answer = input("{}Saisissez le nombre (décimal ou entier) de périodes que vous souhaitez mesurer :\n".format(s))
            Z = float(answer)
        except ValueError:
            if (answer==''):
                Z = 30
        finally:
            s = 'Vous devez nécessairement entrer un nombre en chiffres, strictement supérieur à 1. Exemples : 0.5 ou 15\n'
    if (Z==1):
        s = ''
    else:
        s = 's'
    print("On observera {} période{} de la sinusoïdale étudiée.".format(Z, s))
    return Z

def ask_holes(nb):
    choice = choose()
    a = b = c = 0
    if choice%2==0 :
        #trous aléatoires
        a = randoms(nb)
    if choice>2 :
        #trous fixes
        b, c = predictables(nb)
    return a, b, c

def choose():
    chosen = 0
    s = ''
    while not (0<chosen<5) :
        try:
            answer = input("{}Comment voulez-vous corrompre le signal ? Répondre le numéro correspondant à la réponse.\n\n1 - Ne pas corrompre le signal.\n2 - Corrompre le signal par des trous aléatoires.\n3 - Corrompre le signal par un nombre de trous fixes.\n4 - Corrompre le signal par un mélange de trous aléatoires et de trous fixes.".format(s))
            chosen = int(answer)
        except ValueError:
            if (answer==''):
                print("Le signal ne sera pas corrompu.")
                return 1
        finally:
            s = 'Vous devez nécessairement entrer un entier correspondant à l\'une des 4 propositions'
    return chosen

def randoms(nb):
    T = -1
    s = ''
    while not (0<T<nb) :
        try:
            answer = input("{}Saisissez le nombre entier de trous aléatoires que vous souhaitez insérer.\nNOMBRE TOTAL D'ÉCHANTILLONS : {}\n".format(s, nb))
            T = int(answer)
        except ValueError:
            pass
        finally:
            s = 'Vous devez nécessairement entrer un nombre entier en chiffres, supérieur ou égal à 1, mais inférieur au nombre total d\'échantillons. Exemples : {} ou {}\n'.format(int(nb/3)+1, int(nb/1.4)+1)
    if (T==1):
        s = ''
    else:
        s = 's'
    print("On corrompt le signal ({} points) avec {} trou{}.".format(nb, T, s))
    return T

def predictables(nb):
    #on demande la largeur des trous
    width = 0
    s = ''
    while not (0<width<nb//4) :
        try:
            answer = input("{}Saisissez la largeur des bandes blanches que vous souhaitez insérer.\nLARGEUR MAXIMALE DES TROUS : {}\n".format(s, nb//4))
            width = int(answer)
        except ValueError:
            pass
        finally:
            s = 'Vous devez nécessairement entrer un nombre entier en chiffres, supérieur ou égal à 1, mais inférieur à la longueur maximale d\'un trou (équivalente à un quart de la longueur totale de mesure). Exemples : {} ou {}\n'.format(int(nb/12)+1, int(nb/5.6)+1)
    #on demande le nombre de trous ou leur fréquence d'apparition ? Le deuxième choix semble plus indiqué, car il permet de donner les mêmes trous à différents échantillons de mesure de longueur différent (3 et 7.5 périodes par exemple)
    freq = 0
    s = ''
    while not (width<freq<=nb-width) :
        try:
            answer = input("{}Saisissez la fréquence à vous souhaitez insérer vos bandes blanches (Tous les X trous).\nFréquence maximale : une bande tous les {} trous\nFréquence minimale (pour avoir 2 bandes): une bande tous les {} trous".format(s, width+1, nb-width))
            freq = int(answer)
        except ValueError:
            pass
        finally:
            s = 'Vous devez nécessairement entrer un nombre entier en chiffres, supérieur ou égal à 1, mais inférieur au nombre total d\'échantillons.'
    return width, freq