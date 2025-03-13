def aeussere_funktion(x):
    """
    Diese Funktion gibt eine innere Funktion zurück,
    die x mit einem übergebenen y multipliziert.
    """
    def innere_funktion(y):
        # Zugriff auf x aus der äußeren Funktion
        return x * y
    return innere_funktion


def aussere_funktion2(x, y):
    """
    Diese Funktion gibt eine innere Funktion zurück,
    die (x + y) hoch z berechnet.
    """
    def innerfunktion(z):
        return (x + y) ** z
    return innerfunktion


def aussere_funktion3(x, y):
    """
    Diese Funktion gibt eine innere Funktion zurück,
    die (x + y) hoch z geteilt durch a berechnet.
    """
    def innerfunktion(z, a):
        return ((x + y) ** z) / a
    return innerfunktion

# Beispielaufrufe und Ausgabe
#aussere = aeussere_funktion(2)  # Rückgabe ist die innere Funktion
#resultat = aussere(5)           # 2 * 5 = 10
#print(resultat)


aussere2 = aussere_funktion2(1, 3)(3)
print(f"Ergebnis von aussere_funktion2(1,3)(3): {aussere2}")

aussere2 = aussere_funktion2(1, 3)
resultat = aussere2(3)
print(f"Ergebnis von aussere_funktion2(1,3) mit (3): {resultat}")

aussere3 = aussere_funktion3(1, 3)(3, 2)
print(f"Ergebnis von aussere_funktion3(1,3)(3,2): {aussere3}")

aussere3 = aussere_funktion3(1, 3)
resultat = aussere3(3, 2)
print(f"Ergebnis von aussere_funktion3(1,3) mit (3,2): {resultat}")

