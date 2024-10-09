import math

def harom():
    # 1. megoldás
    for i in range(0, 21, 1):
        print(i)

    # 2. megoldás
    for i in range(21):
        print(i)

    # 3. megoldás
    for i in range(0, 21):
        print(i)

    # 4.megoldás
    i = 0
    while i < 21:
        print(i)
        i += 1


def negy():
    for i in range(20, 57, 2):
        print(i)


def ot():
    for i in range(77, -77, -4):
        print(i)


def beolvas():
    szam = int(input("Kérem adjon meg egy egész számot! "))
    return szam


def hat():
    # 6.	Kérj be 2 számot, majd írasd ki a számokat a legkisebbtől a legnagyobbig! (a legnagyobbat is! Ha az első szám nagyobb, abban az esetben is a legkisebbtől a legnagyobbig írasd ki!)

    szam1 = beolvas()
    szam2 = beolvas()

    # melyik a nagyobb
    if szam2 < szam1:
        # csere
        atmenet = szam1
        szam1 = szam2
        szam2 = atmenet

    for i in range(szam1, szam2+1, 1):
        print(i, end=" ")


def het():
    # 7.	Kérj be 2 számot, majd írasd ki a számokat 0-tól a 2 szám szorzatáig!
    szam1 = beolvas()
    szam2 = beolvas()
    szorzat = szam1 * szam2

    if szorzat < 0:
        for i in range(0, szorzat-1, -1):
            print(i, end=" ")
    else:
        for i in range(0, szorzat+1, 1):
            print(i, end=" ")


def kilenc():
    pass


def nyolc():
    # 8.	Kérj be 2 számot, majd írasd ki a számokat 0-tól a 2 szám szorzatáig!
    szam1 = beolvas()
    szam2 = beolvas()
    szorzat = szam1 * szam2

    if szorzat < 0:
        i = 0
        while i < szorzat - 1:
            print(i, end=" ")
            i = i - 1
            # i-= 1
    else:
        i = 0
        while i < szorzat + 1:
            print(i, end=" ")
            i = i + 1


# 9.	Írasd ki az első 7 pozitív egész számot vesszővel elválasztva!
def kilenc():
    for szam in range(1, 8):
        # print(szam, end=", ")
        print(str(szam) + ",", end=" ")


# a.	úgy, hogy a végén ne legyen vessző!
def kilenc_a():
    # 1. megoldás
    for szam in range(0, 7, 1):
        # print(szam, end=", ")
        print(str(szam) + ",", end=" ")
    print(7)

    # 2. megoldás
    print(0, end=" ")
    for szam in range(1, 8, 1):
        # print(szam, end=", ")
        print("," + str(szam), end=" ")


def beolvas2():
    szam = float(input("Kérem adjon meg egy valós számot! "))
    return szam


# 11.	Írasd ki 2 bekért szám (x és y) alapján, hogy mennyi 3x+y2!
def tizenegy():
    x = beolvas2()
    y = beolvas2()
    eredmeny1 = 3 * x + y**2
    eredmeny2 = 3 * x + math.pow(y,2)
    eredmeny3 = 3 * x + pow(y,2)
    eredmeny4 = 3 * x + (y*y)
    print("3×"+str(x)+"+"+str(y)+"^2="+str(eredmeny1))


# 12.	Számold meg 2 bekért szám közötti páros számokat! (pl. hány db páros szám van 4 és 31 között?)
def tizenketto():
    x = beolvas2()
    y = beolvas2()
    db = 0
    for szam in range(math.ceil(x), round(y) + 1, 1):
        # print(szam, end=" ")
        if szam % 2 == 0:
            #  páros eset
            db += 1
    print("A páros számok száma: " + str(db) + ".")

