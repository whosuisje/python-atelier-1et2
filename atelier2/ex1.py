
def index (list):
    pair=[]
    impaire=[]
    for i in list:
       if (i%2 == 0):
           pair.append(i)
       else:
           impaire.append(i)
           
    print (pair)
    print (impaire)
list =[1,2,3,4,5,6,7,8,9,10]
index(list)
