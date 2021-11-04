#la liste en 3 morceaux égaux et inverser chaque morceau
def trois_morceau_inverser(list):
    i = 0
    a = []
    
    #on 
    for i in range(0, 9, 3):
        a.append(list[i:i + 3])
    return a


print(trois_morceau_inverser([1, 2, 3, 4, 5, 6, 7, 8, 9]))