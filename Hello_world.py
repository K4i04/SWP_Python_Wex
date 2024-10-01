import random


def lottoziehen():
    meine_liste = []
    while len(meine_liste) < 6:
        zahl = random.randint(1, 45)
        if zahl not in meine_liste:
            meine_liste.append(zahl)
    return meine_liste


def zahlenZuordnen(lotto, ergebnis):
    for zahl in lotto:
        ergebnis[zahl] += 1
    return ergebnis


if __name__ == "__main__":
    ergebnis = {i: 0 for i in range(1, 46)}
    print(lottoziehen())
    for _ in range(1000):
        ergebnis = zahlenZuordnen(lottoziehen(), ergebnis)
    print(ergebnis)
