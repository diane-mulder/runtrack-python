def multiples ():
    L=[1,24,48,2,16] #la liste est toujours entre crochets et les nombres nus sans""
    for i in L:
        if i % 3 ==0: # les multiples s'écrivent % X ==0
             print(i)
multiples()