#Fonction convertir le nombre en binaire inversé
def dec_to_bin(n):
    #condition 
    if n > 1:
        dec_to_bin(n // 2)
    print(n % 2,end=" ")
    #demender le nombre binaire
nbr = int(input("Entrez un nombre decimal: ",))
#appliquer notre fonction
dec_to_bin(nbr )