#     # retirer le minimum de la liste L
#     L.remove(minimum)

L = [8,3,10,6,1]
triés = [] # créer une liste vide pour stocker les éléments triés
while L>0:
    minimum = L[0] # trouver le minimum de la liste L
    for nombre in L:
        if nombre<minimum:
            minimum=nombre
            triés.append(minimum) # ajouter le minimum à la liste trié
            L.remove(minimum) # retirer le minimum de la liste L
        print(L)



