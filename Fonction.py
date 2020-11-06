import pandas as pd
import random
from VideoPoker import gagne as gg

def premier_tirage(deck):
    tirage = []
    for i in range(5):
        card = random.choice(deck)
        tirage.append(card)
        deck.remove(card)
    return tirage, deck


def choix_carte(hand=list):
    jeu = []
    for i in hand:
        print(i)
        choix = input("voulez-vous garder cette carte ? [y/n] : ")
        if choix == "y":
            jeu.append(i)
    return jeu


def deuxieme_tirage(tirage, deck):
    nb_carte = len(tirage)
    nb_carte_a_avoir = 5 - nb_carte
    for i in range(nb_carte_a_avoir):
        card = random.choice(deck)
        tirage.append(card)
        deck.remove(card)
    return tirage


def machine():
    deck = ['2-h', '3-h', '4-h', '5-h', '6-h', '7-h', '8-h', '9-h', '10-h', 'J-h', 'Q-h', 'K-h', 'A-h', '2-d', '3-d',
            '4-d', '5-d', '6-d', '7-d', '8-d', '9-d', '10-d', 'J-d', 'Q-d', 'K-d', 'A-d', '2-c', '3-c', '4-c', '5-c',
            '6-c', '7-c', '8-c', '9-c', '10-c', 'J-c', 'Q-c', 'K-c', 'A-c', '2-s', '3-s', '4-s', '5-s', '6-s', '7-s',
            '8-s', '9-s', '10-s', 'J-s', 'Q-s', 'K-s', 'A-s']
    tirage, deck = premier_tirage(deck)
    print(tirage, "\n")
    jeu = choix_carte(tirage)
    tirage2 = deuxieme_tirage(jeu, deck)
    print(tirage2)
    return tirage2


# do a bankroll fox
def partie (mise,bankroll):
    print("\nta bankroll est de :",bankroll,"\nta mise est de :",mise,"\n")
    deck = ['2-h', '3-h', '4-h', '5-h', '6-h', '7-h', '8-h', '9-h', '10-h', 'J-h', 'Q-h', 'K-h', 'A-h', '2-d', '3-d',
            '4-d', '5-d', '6-d', '7-d', '8-d', '9-d', '10-d', 'J-d', 'Q-d', 'K-d', 'A-d', '2-c', '3-c', '4-c', '5-c',
            '6-c', '7-c', '8-c', '9-c', '10-c', 'J-c', 'Q-c', 'K-c', 'A-c', '2-s', '3-s', '4-s', '5-s', '6-s', '7-s',
            '8-s', '9-s', '10-s', 'J-s', 'Q-s', 'K-s', 'A-s']

    if bankroll >= mise:
        tirage, deck = premier_tirage(deck)
        print(tirage, "\n")
        jeu = choix_carte(tirage)
        tirage2 = deuxieme_tirage(jeu, deck)
        print("\nta nouvelle main :",tirage2)

        #on retire la mise puis on rajoute le gain
        bankroll = bankroll - mise + calcgain(tirage2, mise)
    return bankroll

def video_poker():

    quitter = False
    bankroll = 0

    print("#######################################")
    print("## Bienvenu sur Super-VideoPoker2000 ##")
    print("#######################################")

#saisi de bankroll
    while bankroll <= 0 :
        try :
         bankroll= int(input("veuillez inserer de l'argent, il correspondra a votre bankroll ( 0 < ): "))
        except ValueError:
            print("\n/!\ saisissez une valeur numérique  : ")
            continue


    while quitter == False and bankroll >0:
        dchoix = "o"
        mise = 0


#saisir la mise
        while  mise > bankroll or mise <= 0:
            try:
                mise = int(input("veuillez saisir votre mise ( 0 < mise < bankroll ) : "))
            except ValueError:
                continue

# lancement de la partie + prise du resultat ( gain ou perte )
        bkroll = partie(mise, bankroll)

        # mise a jour de la bankroll
        if bkroll <= 0:
            bankroll = 0
        else:
            bankroll = bkroll


# on regarde si ou veut quitter ou non
        print("votre bankroll est de : ",bankroll)
        while dchoix.lower() != "y" and dchoix.lower() != "n" and bankroll >0 :
            dchoix = input("\nvoulez-vous continuer [y/n] : ")
            if dchoix.isnumeric():
                print("entrer : ",dchoix," n'est pas équivalent a 'y' ou 'n'")
            if dchoix.lower() == "n":
                quitter=True


# message de fin
    if bankroll==0:
        print("\nOh non ! Tu as plus d'argent aurevoir o/")
    else:
        print("\nAurevoir et a très bientot pour de nouvelles supers parties !")





# insupportable
def calcgain(tirage,mise):

    paire, dpaire, brelan, carre, full , flush = gg.test_cfbd(tirage)
    q, qtf, qfr = gg.quinte(tirage)

    if paire:
        print("\nles deux font la Paire")
        return mise
    elif dpaire :
        print("\nd-d-d-Double Paire !")
        mise = mise *2
    elif brelan:
        print("\nchaud devant,attention c'est Brelan !")
        mise = mise *3
    elif carre:
        print("\nune belle racine Carré")
        mise = mise *25
    elif full:
        print("\ntu as Full comme un pro")
        mise = mise*9
    elif q:
        print("\nca es-Quinte le jeu ")
        mise = mise * 4
    elif qfr:
        print("\nQUINTE FLUSH ROYYAAALLLLLuuu!!!!!!\n\ntu as reussi a avoir une combinaison qui a  0,00015% de tomber\n des potes a moi vont venir voir si tu as pas triché ",)
        mise =mise*250
    elif qtf:
        print("\nah bah la ! Quinte Flush ")
        mise = mise * 50
    elif flush:
        print("\nflunch.. euhh.. Flush !")
        mise = mise *6


    else:
        print("\nperdu :'(  essaie encore si tu peux ")
        mise = mise - mise*2

    return  mise

