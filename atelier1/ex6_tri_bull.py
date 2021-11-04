# trier un tableau à l’aide de l’algorithme de tri a bull
def tri_bulle(tab):
    number = len(tab)
# Traverser tous les éléments du tableau
    for i in range(number):
        for j in range(0, number-i-1):
             # échanger si l'élément trouvé est plus grand que le suivant
            if tab[j] > tab[j+1] :
                tab[j] = tab[j+1]
                tab[j+1]= tab[j]
#tester notre code
tab = [98, 22, 15, 32, 10, 68, 65,17]
tri_bulle(tab) 
print ("Le tableau trié est:")
for i in range(len(tab)): 
    print ("% d" % tab[i],end=" ")



