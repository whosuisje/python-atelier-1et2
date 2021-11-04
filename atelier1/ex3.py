#Fonction qui détermine la sommation du nombre
def somme(n):
  #condition d'arret
  if n == 0:
    return 0
#Boucle de récursivité
  else:
#Retour du résultat
    return n + somme(n - 1)
nbr = int(input("Entrez un nombre : "))
# resultat final 
print(somme(nbr))