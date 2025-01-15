class Feuerwehr:
    def __init__(self, name, ort):
        self.name = name
        self.ort = ort

    def __str__(self):
        return f"Feuerwehr {self.name} aus {self.ort}"

    @staticmethod  # 2
    def addSave(a, b):
        if (isinstance(a, int) and isinstance(b, int)):
            return a + b
        else:
            raise ValueError("Bitte 2 Zahlen eingeben!")

    def rekursiv(c):
        print(c)
        c = c + 1  # Diese Zeile hat keinen Effekt, weil das Ergebnis nicht gespeichert wird
        return Feuerwehr.rekursiv(c)  # Es wird wieder rekursiv mit dem gleichen Wert von c aufgerufen


class FeuerwehrAutos(Feuerwehr):
    def __init__(self, name, ort, auto_type, auto_nummer):
        super().__init__(name, ort)
        self.auto_type = auto_type
        self.auto_nummer = auto_nummer

    def __str__(self):
        return f"{super().__str__()} fährt ein {self.auto_type} mit der Nummer {self.auto_nummer}"


def main():
    # Erstellen eines Feuerwehr-Objekts
    feuerwehr1 = Feuerwehr("Schwaz", "Schwaz")
    print(feuerwehr1)  # Gibt: Feuerwehr Schwaz aus Schwaz

    # Erstellen eines FeuerwehrAutos-Objekts
    auto1 = FeuerwehrAutos("Jenbach", "Jenbach", "Löschfahrzeug", "LF-1234")
    # print(auto1)   Fehler gleich behebbar 1

    try:
        result = Feuerwehr.addSave(5, "3")  # Fehler: "3" ist kein int
        print(f"Das Ergebnis ist: {result}")
    except ValueError as e:
        print(f"Fehler: {e}")

    try:
        result = Feuerwehr.addSave(5, 7)  # Erfolgreich
        print(f"Das Ergebnis ist: {result}")
    except ValueError as e:
        print(f"Fehler: {e}")

    try:  # 3
        result = 10 / 0
    except ZeroDivisionError as e:
        print(f"Fehler: {e}")

    try:  # 4
        Feuerwehr.rekursiv(1)
    except RecursionError as e:
        print(f"Fehler : {e}")


if __name__ == "__main__":
    main()
