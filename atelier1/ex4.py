#la série Fibonacci
def fibonacci(n):
 #condition d'arret
    if(n <= 1):
#Retour du résultat
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))
#demender nombre de termes 
n = int(input("Entrez le nombre de termes:"))
print("Suite de Fibonacci :")
#afficher resultat
for i in range(n):
    print(fibonacci(i),end=" ")