#la fréquence d’un caractère dans une chaîne
def fequence(str,val):
   cmpt = 1
   for i in range(len(str)):
       if str[i]==val:
#si une trouve un caractere on acremente nontre compteur
           cmpt+=1
   return cmpt
str = input("Entrez un chaine de caractere : ")
val=input("Entrez une lettre : ")
print("nombre d'accurance  est")
# afficher notre frequence
print(fequence(str,val)-1)
