def maxMin():
    L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
    max = L[0] # max : indique la valeur la plus grande de la liste
    min = L[0] # min : inqique la valeur la plus petite de la liste
    for i in L:
        if i<min:
            min=i
        elif i>max:
            max=i
    print(min,max)
maxMin()