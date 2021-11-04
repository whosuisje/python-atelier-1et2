#factorial fonction 
def fact(num):
 if num ==0:
    return 1
#déterminer la factorielle par récursivité
 else:
     return (num *(num-1))
#somme demende    
som= fact(1)/1+fact(2)/2+fact(3)/3+fact(4)/4+fact(5)/5
# affichage de la resultat final
print(som)