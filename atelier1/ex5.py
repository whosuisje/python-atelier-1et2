#compter les chiffres d'un nombre
def compter(number) :
#condition d'arret
     if number<10 :
      return 1 
     else :
      return 1 + compter(number/10)\
#demender une nombre
nbr = int(input("Entrez un nombre : "))
#afficher resultat
print(compter(nbr))
