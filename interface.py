from re import search
def ask_amplitude():
    answer = input("Le signal doit-il être amorti ?\nRéponses acceptées :\nOui, Yes, Y, 1\nNo, Non, N, 0, Cancel")
    non = search("^(((N|n)*((O|o)*)*(N|n)*)|0*|(Cancel)?)$", answer)
    if (non):
        print("Le signal n'est pas amorti.")
        return 0
    lamb = 0
    s=''
    while lamb==0 or lamb<0:
        try:
            lamb = float(input("{}Saisissez la valeur souhaitée de l'amortissement : ce nombre doit être décimal, strictememt supérieur à 0".format(s)))
        except ValueError:
            pass
        finally:
            s = 'Vous devez nécessairement entrer un nombre en chiffres, strictement supérieur à 0. Exemples : 13.55 ou 0.003\n'
    print("Le coefficient d'amortissement sera de {}. L'amplitude dépendant du temps sera donc égale à exp(-{}t)".format(lamb, lamb))
    return lamb

def ask_phases():
    Z = 0
    s = ''
    while Z==0 or Z<0 :
        try:
            answer = input("{}Saisissez le nombre (décimal ou entier) de périodes que vous souhaitez mesurer :\n".format(s))
            Z = float(answer)
        except ValueError:
            if (answer==''):
                Z = 3
        finally:
            s = 'Vous devez nécessairement entrer un nombre en chiffres, strictement supérieur à 1. Exemples : 0.5 ou 15\n'
    if (Z==1):
        s = ''
    else:
        s = 's'
    print("On observera {} période{} de la sinusoïdale étudiée.".format(Z, s))
    return Z

def ask_holes(nb):
    T = 0
    s = ''
    while T==0 or T>nb or 0>T :
        try:
            answer = input("{}Saisissez le nombre entier de trous que vous souhaitez insérer.\nNOMBRE TOTAL D'ÉCHANTILLONS : {}\n".format(s, nb))
            T = int(answer)
        except ValueError:
            if (answer==''):
                print("Le signal ne sera pas corrompu.")
                return 0
        finally:
            s = 'Vous devez nécessairement entrer un nombre entier en chiffres, supérieur ou égal à 1, mais inférieur au nombre total d\'échantillons. Exemples : {} ou {}\n'.format(int(nb/3 +1), int(nb/1.4 +1))
    if (T==1):
        s = ''
    else:
        s = 's'
    print("On corrompt le signal ({} points) avec {} trou{}.".format(nb, T, s))
    return T