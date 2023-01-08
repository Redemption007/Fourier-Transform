def damping(A):
    if (A!=0):
        print("\n\nLe signal est amorti. Le coefficient d'amortissement est de {}. On remarque que la tranformée de Fourier devient choatique, et une multitude de petits pics apparaissent sur la transformée normalisée positive.".format(A))
def phases(Z):
    if (int(Z)!=Z):
        print("\n\nOn observe que quand le temps de mesure n'est pas un multiple de la période (Le nombre de périodes observé est ici de {}), la transformée de Fourier n'est plus un outil pertinent pour étudier une fonction périodique.\nSi maximum atteint reste à la bonne fréquence, il suffit que le signal comporte une légère incertitude pour que les résultats ne soient plus exploitables ensuite.\nLes déformations commencent à apparaître au bout d'environ 5 échantillons de trop".format(Z))
def holes(nb_holes):
    if (nb_holes>0):
        print("\n\nOn remarque plusieurs conséquences à la présence de {} zéros dans le code.\nPremièrement, le signal se déforme et la continuité disparaît.\nDeuxièmement, et comme conséquence du premier point, les transformées de Fourier perdent leur continuité et de leur symétrie.\nTroisième chose, conséquences des deux autres : La tranformé de Fourier perd sa régularité".format(nb_holes))

def concludes(A, Z, nb_holes):
    damping(A)
    phases(Z)
    holes(nb_holes)