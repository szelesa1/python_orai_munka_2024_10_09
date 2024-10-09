from random import *


def beolvas_egesz():
    szam = int(input("Kérem adjon meg egy egész számot! "))
    return szam


def beolvas2_tort():
    szam = float(input("Kérem adjon meg egy valós számot! "))
    return szam



def general_paros_egesz():
    szam1 = randint(-10, 10)
    # print("szám: " + str(szam1))
    while not(szam1 % 2 == 0):
        szam1 = randint(-10, 10)
    return szam1

    # ennek  az a fogalma, hogy függvény (lásd: egyAlapC():)