def itère ():
    for i in range(1,101):
        if i % 3 ==0 and i % 5 ==0: # les multiples s'écrivent % X ==0
             print("FizzBuzz")
        elif i % 3 ==0:
            print("Fizz")
        elif i % 5 ==0:
            print ("Buzz")
        else: #jamais mettre de condition après else
            print(i)
itère()#ne jamais oublier le rappel de la fonction


