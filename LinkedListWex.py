from ListenElement import ListenElement


class LinkedListWex:
    def __init__(self):
        self.start = ListenElement("Kopf")  # Erstellt ein Start-Element (Kopf der Liste)

    def hinzufuegen(self, wert):
        aktuelles = self.start
        while aktuelles.naechstes:  # Durchläuft die Liste bis zum letzten Element
            aktuelles = aktuelles.naechstes
        aktuelles.naechstes = ListenElement(wert)  # Fügt ein neues Element am Ende hinzu

    def einfuegen_nach(self, vorheriges, neu):
        aktuelles = self.start.naechstes  # Beginnt nach dem Kopf-Element
        while aktuelles and aktuelles.inhalt != vorheriges:  # Sucht das vorherige Element
            aktuelles = aktuelles.naechstes
        if aktuelles:  # Falls das Element gefunden wurde, füge das neue Element ein
            neues_element = ListenElement(neu)
            neues_element.naechstes = aktuelles.naechstes
            aktuelles.naechstes = neues_element

    def entfernen(self, wert):
        aktuelles = self.start
        while aktuelles.naechstes and aktuelles.naechstes.inhalt != wert:  # Sucht das zu löschende Element
            aktuelles = aktuelles.naechstes
        if aktuelles.naechstes:  # Falls das Element gefunden wurde, entferne es
            aktuelles.naechstes = aktuelles.naechstes.naechstes

    def suchen(self, wert):
        aktuelles = self.start
        while aktuelles:  # Durchläuft die Liste
            if aktuelles.inhalt == wert:
                return True  # Gibt True zurück, falls das Element gefunden wird
            aktuelles = aktuelles.naechstes
        return False  # Gibt False zurück, falls das Element nicht gefunden wird

    def liste_ausgeben(self):
        aktuelles = self.start.naechstes  # Überspringt das Kopf-Element
        while aktuelles:  # Gibt alle Elemente der Liste aus
            print(aktuelles.inhalt)
            aktuelles = aktuelles.naechstes

    def mittleres_element(self):
        aktuelles = self.start.naechstes
        laenge = 0
        while aktuelles:
            laenge += 1
            aktuelles = aktuelles.naechstes

        # Schritt 2: Finde das mittlere Element (0-basiert)
        mitte_index = laenge // 2
        aktuelles = self.start.naechstes
        for _ in range(mitte_index):
            aktuelles = aktuelles.naechstes

        return aktuelles.inhalt if aktuelles else None


def main():
    liste = LinkedListWex()
    liste.hinzufuegen("1")
    liste.hinzufuegen("2")
    liste.hinzufuegen("3")
    liste.hinzufuegen("4")
    liste.hinzufuegen("5")
    liste.einfuegen_nach("2", "neu")
    liste.entfernen("3")
    liste.liste_ausgeben()
    print("Ist '3' enthalten?", liste.suchen("3"))
    print("Ist '5' enthalten?", liste.suchen("5"))
    print("Mittleres Element:", liste.mittleres_element())


if __name__ == "__main__":
    main()
