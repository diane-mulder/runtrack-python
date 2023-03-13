# random(): cette fonction renvoie un nombre aléatoire compris entre 0 et 1 (exclus).
# randint(a, b): cette fonction renvoie un entier aléatoire compris entre a et b (inclus).
# choice(seq): cette fonction renvoie un élément aléatoire dans la séquence donnée.
# shuffle(seq): cette fonction mélange la séquence donnée de manière aléatoire.
# sample(seq, k): cette fonction renvoie une liste de k éléments aléatoires de la séquence donnée.
# Pour utiliser ce module, il faut tout d’abord l’importer en utilisant l’instruction « import random ». Une fois importé, on peut appeler les fonctions de ce module en utilisant la syntaxe « random.fonction() ».
#import random
# import string

# password_length = 10
# characters = string.ascii_letters + string.digits + string.punctuation
# password = ''.join(random.choices(characters, k=password_length))
# print(password)


def creaPassword():# Demandez à l'utilisateur de choisir un mot de passe.
    password = input("Veuillez entrer votre mot de passe : ") 
    print("votre mot de passe est :", password)
    return(password)

def checkPassword(password):# définir le parametre dans la fonction
        # Vérifiez si le mot de passe choisi respecte les exigences de sécurité = des variables
    lettersMajuscule ="ABCDEFGHIJKLMNOPQRSTUVWXYZ" #lettres de l'alphabet majuscule
    lettersMinuscule ="abcdefghijklmnopqrstuvwxyz" #lettres minuscules
    digits = "0123456789" #liste de chiffres de 0 à 9
    special_chars ="!@#$%^&*"# indiquer les caractères spéciaux sans virgules!!
    pwd_lenght = 8 # longueur du mot de passe
    for lettre in (password):
        if len(password) < (pwd_lenght): # doit contenir 8 caractères
            print("votre mot de passe doit contenir 8 caractères")
        if lettre not in (digits):# doit contenir au moins 1 chiffre
            print("votre mot de passe doit contenir au moins 1 chiffre")
        elif lettre not in (lettersMajuscule):# lettre majuscule
            print("votre mot de passe doit contenir au moins 1 lettre majuscule")
        elif lettre not in (lettersMinuscule): # lettre minuscule
            print("votre mot de passe doit contenir au moins 1 lettre minuscule")
        elif lettre not in (special_chars):#doit contenir au moins 1 caractère spécial
            print("votre mot de passe doit contenir au moins un caractère spécial")
        else: # si le password répond à tous les critères ci-dessus
            print("votre mot de passe est valide")
new_password = creaPassword()
checkPassword(new_password)

  

     





