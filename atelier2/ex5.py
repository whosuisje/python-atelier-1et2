def verifier(list1, dict1):
    keys = list(dict1.keys())
    result = []
    for i in keys:
        for j in list1:
            if dict1[str(i)] == j: result.append(j)
    return result

print(verifier([47, 64, 69, 37, 76, 83, 95, 97], {'ahmad':47, 'Imane':69, 'Mohammed':76, 'anas':97}))