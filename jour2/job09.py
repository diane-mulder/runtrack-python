def triangle(a,b,c):
    if a+c>b and c+b>a and b+a>c:
        print ("c'est un triangle")
    if a**2==b**2+c**2 or b**2==a**2+c**2 or c**2==a**2+b**2:
        print ("c'est un triangle rectangle")
    elif a==b and b==c:
        print ("c'est un triangle equilatéral")
    if a**2==b**2+c**2 or b**2==a**2+c**2 or c**2==a**2+b**2 and (a==b and b==c):
        print("c'est un triangle rectangle et isocèle")
    else:
        print("c'est un triangle isocèle")
triangle(5,5,5)   
    

