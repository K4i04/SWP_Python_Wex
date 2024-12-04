class Feuerwehr:
    def __init__(self, name, ort):
        self.name = name
        self.ort = ort

    def __str__(self):
        return f"Feuerwehr {self.name} aus {self.ort}"


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
    print(auto1)  # Gibt: Feuerwehr Jenbach aus Jenbach fährt ein Löschfahrzeug mit der Nummer LF-1234


if __name__ == "__main__":
    main()
