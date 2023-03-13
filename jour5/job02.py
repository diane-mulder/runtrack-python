def dessinRectangle (width,height):
    for i in range(width): # c'est la largeur
        if i ==0 or i == -1:
            print("-"*width)
        else:
           print("|" + "-" * (width-2) + "|")
dessinRectangle(10,3)