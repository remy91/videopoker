import random

def decompo(tirage):
 dic = {}
 keys = [1,2,3,4,5]
 valeur = []
 couleur = []
 for i,k in zip (tirage,keys):
     dic[k] = i.split('-')
 for key in dic.keys():
     valeur.append(dic[key][0])
     couleur.append(dic[key][1])
 return valeur,couleur


def convert(valeur):
    for e,i in zip(valeur,range(0,5)):
        try :
            valeur[i] = int(e)
        except :
            if e == "J":
                valeur[i] = 11
            elif e == "Q":
                valeur[i] = 12
            elif e == "K":
                valeur[i] = 13
            elif e == "A":
                valeur[i] = 14
            else:
                continue
    return valeur


def nunique(tirage):
    valeur,couleur =decompo(tirage)
    nb_valeur = []
    for x in set(valeur):
        nb_valeur.append(valeur.count(x))
    return (sorted(nb_valeur,reverse=True))[:2]


def test_cfbd(tirage):
    valeur,couleur = decompo(tirage)
    test_nunique =nunique(tirage)
    paire = False
    dpaire = False
    carre = False
    full = False
    brelan=False
    flush = False

    if test_nunique[0] == 2 and test_nunique[1] == 2:
       # print("double paires")
        dpaire = True
    elif couleur.count(couleur[0]) == 5:
       # print("flush")
        flush=True
    elif test_nunique[0] == 4:
       # print("carre")
        carre=True
    elif test_nunique[0] == 2 and not (test_nunique[0] == 2 and test_nunique[1] == 2) :
       # print("paire")
        paire=True
    elif test_nunique[0] == 3 and test_nunique[1] == 2:
       # print("full")
        full=True
    elif test_nunique[0] == 3:
       # print("brelan")
        brelan=True
    return paire,dpaire,brelan,carre,full,flush




def quinte(tirage):

    valeur, couleur = decompo(tirage)
    nval=convert(valeur)
    quinte = False
    quinteflush = False
    quinteflushroyal = False


    nval = [int(i) for i in nval]
    nval.sort()

    if sorted(nval) == sorted([10,11,12,13,14]) and couleur.count(couleur[0]) == 5:
       # print("Quinte flush royal")
        quinteflushroyal = True
        return quinte,quinteflush,quinteflushroyal

    elif int(nval[4]) - int(nval[0]) == 4 and couleur.count(couleur[0]) == 5:
        #print("Quinte flush ")
        quinteflush = True
        return quinte,quinteflush,quinteflushroyal

    elif int(nval[4]) - int(nval[0]) == 4:
        #print("quinte")
        quinte = True
        return quinte,quinteflush,quinteflushroyal

    return quinte,quinteflush,quinteflushroyal

