#compter l'occurrence de chaque élément
def occurence(list):
    #créer un dictionnaire
    a = {}
    for i in list:
        #montrer le nombre de chaque élément.
        if str(i) in a:
            a[str(i)] = a.pop(str(i)) + 1
        else:
            a[str(i)] = 1
    return a
#afficher solution
print(occurence([1, 2, 3, 4, 5,]))