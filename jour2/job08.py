def fruit_de_saison(type, saison):
    if type == "fruit" and saison == "hiver":
        print("orange, madarine, kiwi")
    elif type == "fruit" and saison == "été":
        print("poire, fraise, cassis")
    elif type == "legume" and saison == "hiver":
        print("carotte, topinambour, endive")
    elif type == "legume" and saison == "été":
        print("artichaut, aubergine, navet")
fruit_de_saison("fruit", "hiver")