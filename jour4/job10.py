def calculProduit():
    L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
    i=1 #création d'une variable
    for num in L:  # cela parcours les éléments et affiche la valeur
        if num>=25 and num<=90:
         i=i*num #ou i*=num 
    print(i)
calculProduit()
    