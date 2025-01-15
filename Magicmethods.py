class Auto:
    def __init__(self, PS):
        self.PS = PS

    def __add__(self, other):
        if not isinstance(other, Auto):
            raise TypeError("Kann nur Autos addieren!")
        return Auto(self.PS + other.PS)

    def __sub__(self, other):
        if not isinstance(other, Auto):
            raise TypeError("Kann nur Autos subtrahieren!")
        return Auto(self.PS - other.PS)

    def __mul__(self, other):
        if not isinstance(other, Auto):
            raise TypeError("Kann nur Autos multiplizieren!")
        return Auto(self.PS * other.PS)

    def __eq__(self, other):
        if not isinstance(other, Auto):
            raise TypeError("Kann nur Autos vergleichen!")
        return self.PS == other.PS

    def __lt__(self, other):
        if not isinstance(other, Auto):
            raise TypeError("Kann nur Autos vergleichen!")
        return self.PS < other.PS

    def __gt__(self, other):
        if not isinstance(other, Auto):
            raise TypeError("Kann nur Autos vergleichen!")
        return self.PS > other.PS

    def __repr__(self):
        return f"{self.PS} PS"


def main():
    a1 = Auto(50)  # Auto mit 50 PS
    a2 = Auto(60)  # Auto mit 60 PS
    a3 = 1  # Keine gültige Zahl, um mit Auto zu rechnen

    try:
        # Test für Addition (Magic Method __add__)
        add = a1 + a2
        print(f"Addition: {add}")  # Erwartet: 110 PS

        # Test für Subtraktion (Magic Method __sub__)
        sub = a1 - a2
        print(f"Subtraktion: {sub}")  # Erwartet: -10 PS

        # Test für Multiplikation (Magic Method __mul__)
        mul = a1 * a2
        print(f"Multiplikation: {mul}")  # Erwartet: 3000 PS

        # Test für Gleichheit (Magic Method __eq__)
        if a1 == a2:
            print("Die Autos haben die gleiche PS-Zahl.")
        else:
            print("Die Autos haben unterschiedliche PS-Zahlen.")  # Erwartet: unterschiedliche PS-Zahlen

        # Test für kleiner als (Magic Method __lt__)
        if a1 < a2:
            print("Auto a1 hat weniger PS als Auto a2.")  # Erwartet: weniger PS
        else:
            print("Auto a1 hat nicht weniger PS als Auto a2.")

        # Test für größer als (Magic Method __gt__)
        if a1 > a2:
            print("Auto a1 hat mehr PS als Auto a2.")
        else:
            print("Auto a1 hat nicht mehr PS als Auto a2.")  # Erwartet: weniger PS als a2

        # Falsche Operationen: Versuchen mit einem anderen Datentyp (a3 ist keine Auto-Instanz)
        sub_invalid = a1 - a3  # Erwartet: TypeError
        print(sub_invalid)
    except TypeError as e:
        print(f"Fehler: {e}")  # Gibt an, dass nur Autos verglichen oder berechnet werden können


if __name__ == "__main__":
    main()
