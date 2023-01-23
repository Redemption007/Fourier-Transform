def damping(A):
    if (A!=0):
        print("\n\nLe signal est amorti. Le coefficient d'amortissement est de {}. On remarque qu'une multitude de petits pics apparaissent sur la transformée normalisée positive, formant un bruit".format(A))
def phases(Z):
    if (int(Z)!=Z):
        print("\n\nOn observe que quand le temps de mesure n'est pas un multiple de la période (Le nombre de périodes observé est ici de {}), le signal devient plus difficile à analyser.\nSi maximum atteint reste à la bonne fréquence, il suffit que le signal comporte une légère incertitude pour que les résultats aient une incertitude amplifié.\nLes déformations commencent à apparaître au bout d'environ 5 échantillons de trop.".format(Z))
def holes(nb_holes):
    if (nb_holes>0):
        print("\n\nOn remarque plusieurs conséquences à la présence de {} zéros dans le code.\nPremièrement, le signal se déforme et la continuité disparaît ; les transformées de Fourier perdent leur continuité et de leur symétrie.\nDeuxième chose, conséquences des deux autres : La tranformé de Fourier perd sa régularité et devient plus imprévisible.\nTroisième chose, la transformée n'est pas la même selon que ces trous soient aléatoires ou régulier : dans le premier cas, quelques petits pics apparaîtront à intervalle irrégulier, tandis que dans le second cas on observe une régularité de pics de bruits.".format(nb_holes))

def concludes(A, Z, nb_holes):
    damping(A)
    phases(Z)
    holes(nb_holes)