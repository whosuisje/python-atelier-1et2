# trier un tableau à l’aide de l’algorithme de tri par insertion
def tri_insertion(tab): 
        # Parcour de 1 à la taille du tab
    for i in range(len(tab)): 
        k = tab[i] 
        j = i-1
        while j >= 0 and k < tab[j] : 
                tab[j + 1] = tab[j] 
                j -= 1
        tab[j + 1] = k
tab = [98, 22, 15, 32, 10, 68, 65,17]
tri_insertion(tab) 
print ("Le tableau trié est:")
for i in range(len(tab)): 
    print ("% d" % tab[i],end=" ")
