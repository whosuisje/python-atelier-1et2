#inverser une chaine de caractere
def inverser(str):
  length=len(str)
#  itérer dans la chaine de caractere depuis la fin 
  for i in str:
# inverser nitre chaine
   invstr=str[length::-1]
  return invstr
#afficher notre chaineah
str = (input("Entrez une chaine de caractere: "))
print(inverser(str))