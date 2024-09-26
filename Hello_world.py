import random


def lottoziehung():
    return random.sample(range(1, 46), 6)


def lottoziehung_statistik(anzahl_ziehungen):
    statistik = {i: 0 for i in range(1, 46)}

    for _ in range(anzahl_ziehungen):
        gezogene_zahlen = lottoziehung()
        for zahl in gezogene_zahlen:
            statistik[zahl] += 1

    return statistik


if __name__ == "__main__":
    statistik = lottoziehung_statistik(1000)

    print(f"Statistik der Lottoziehungen ({1000} Ziehungen):")
    for zahl, anzahl in sorted(statistik.items()):
        print(f"Zahl {zahl}: {anzahl} Mal gezogen")
