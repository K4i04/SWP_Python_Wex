import random


# Erstellt ein komplettes Kartendeck mit allen Kombinationen aus Werten und Farben
def get_deck():
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['Herz', 'Karo', 'Pik', 'Kreuz']
    return [f"{value} {suit}" for value in values for suit in suits]  # Jede Karte wird als "Wert Farbe" gespeichert


# Zieht eine Hand von `size` Karten aus einem gemischten Deck
def get_hand(deck, size=5):
    random.shuffle(deck)  # Mische das Deck zufällig
    return deck[:size]  # Ziehe die obersten `size` Karten


# Berechnet den Prozentsatz einer Kombination
def calculate_percentage(total_hands, combination_count):
    return round((combination_count / total_hands) * 100, 2)  # Runden auf 2 Nachkommastellen


# Zählt die Häufigkeit jedes Kartenwerts in der Hand
def count_card_values(hand):
    value_count = {}
    for card in hand:
        value = card.split()[0]  # Extrahiere den Kartenwert (z.B. "3" aus "3 Herz")
        value_count[value] = value_count.get(value, 0) + 1  # Erhöhe den Zähler für diesen Wert
    return value_count


# Prüft, ob die Hand einen Drilling (3 gleiche Werte) enthält
def has_drilling(value_count):
    return 3 in value_count.values()  # Prüft, ob eine Zahl in den Häufigkeiten 3 ist


# Prüft, ob die Hand einen Vierling (4 gleiche Werte) enthält
def has_vierling(value_count):
    return 4 in value_count.values()  # Prüft, ob eine Zahl in den Häufigkeiten 4 ist


# Prüft, wie viele Paare (2 gleiche Werte) in der Hand vorhanden sind
def has_pair(value_count):
    return list(value_count.values()).count(2)  # Zählt, wie oft der Wert 2 in den Häufigkeiten vorkommt


# Prüft, ob die Hand eine Straße (5 aufeinanderfolgende Werte) enthält
def has_strasse(hand):
    value_order = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    values = sorted([card.split()[0] for card in hand], key=value_order.index)  # Sortiere die Werte
    indices = [value_order.index(value) for value in values]  # Hole die Indizes der Werte
    return all(
        indices[i] + 1 == indices[i + 1] for i in range(len(indices) - 1))  # Prüft, ob Indizes aufeinander folgen


# Prüft, ob die Hand einen Flush (alle Karten in einer Farbe) enthält
def has_flush(hand):
    suits = [card.split()[1] for card in hand]  # Extrahiere die Farben der Karten
    return len(set(suits)) == 1  # Prüft, ob alle Farben gleich sind (nur 1 Farbe im Set)


# Prüft, ob die Hand ein Full House (3 gleiche Werte + 2 gleiche Werte) enthält
def has_full_house(value_count):
    return 3 in value_count.values() and 2 in value_count.values()  # Es muss genau einen Drilling und ein Paar geben


# Prüft, ob die Hand ein Straight Flush (Straße + gleiche Farbe) enthält
def has_straight_flush(hand):
    return has_flush(hand) and has_strasse(hand)  # Kombination aus Flush und Straße


# Prüft, ob die Hand ein Royal Flush (Straight Flush von 10 bis A) enthält
def has_royal_flush(hand):
    royal_values = {'10', 'J', 'Q', 'K', 'A'}
    values = {card.split()[0] for card in hand}  # Speichere die Werte in einem Set
    return has_flush(hand) and royal_values.issubset(values)  # Prüft auf Flush und ob alle Royal-Werte enthalten sind


# Führt eine Simulation von `total_games` durch, um die Häufigkeit von Pokerkombinationen zu ermitteln
def simulate_games(total_games):
    deck = get_deck()  # Erstelle ein neues Deck
    results = {
        "royal_flush": 0,
        "straight_flush": 0,
        "full_house": 0,
        "flush": 0,
        "straight": 0,
        "pairs": 0,
        "four_of_a_kind": 0,
        "three_of_a_kind": 0,
    }

    for _ in range(total_games):  # Wiederhole die Simulation `total_games`-mal
        hand = get_hand(deck)  # Ziehe eine Hand
        value_count = count_card_values(hand)  # Zähle die Kartenwerte

        # Prüfe die Kombinationen und erhöhe die jeweiligen Zähler
        if has_royal_flush(hand):
            results["royal_flush"] += 1
        elif has_straight_flush(hand):
            results["straight_flush"] += 1
        elif has_full_house(value_count):
            results["full_house"] += 1
        elif has_flush(hand):
            results["flush"] += 1
        elif has_strasse(hand):
            results["straight"] += 1
        elif has_vierling(value_count):
            results["four_of_a_kind"] += 1
        elif has_drilling(value_count):
            results["three_of_a_kind"] += 1

        pairs = has_pair(value_count)  # Prüfe, wie viele Paare es gibt
        if pairs:
            results["pairs"] += pairs  # Erhöhe die Paaranzahl entsprechend

    return results  # Gib die gesammelten Ergebnisse zurück


# Hauptfunktion, um das Programm auszuführen
def main():
    zahl = 1234567.891
    print(f"{zahl:,.2f}")  # Ausgabe: 1,234,567.89

    total_games = int(input("Wie viele Spiele möchten Sie simulieren? "))  # Frage die Anzahl der Spiele ab
    results = simulate_games(total_games)  # Führe die Simulation durch

    # Gib die Ergebnisse mit Prozentwerten aus
    print(f"Royal Flush: {calculate_percentage(total_games, results['royal_flush'])}%")
    print(f"Straight Flush: {calculate_percentage(total_games, results ['straight_flush'])}%")
    print(f"Full House: {calculate_percentage(total_games, results['full_house'])}%")
    print(f"Flush: {calculate_percentage(total_games, results['flush'])}%")
    print(f"Straight: {calculate_percentage(total_games, results['straight'])}%")
    print(f"Pairs: {calculate_percentage(total_games, results['pairs'])}%")
    print(f"Four of a Kind: {calculate_percentage(total_games, results['four_of_a_kind'])}%")
    print(f"Three of a Kind: {calculate_percentage(total_games, results['three_of_a_kind'])}%")


# Tests für einzelne Funktionen
def test_calculate_percentage():
    assert calculate_percentage(100, 50) == 50.0
    assert calculate_percentage(1000, 250) == 25.0



if __name__ == "__main__":
    #main()  # Startet das Programm, wenn die Datei direkt ausgeführt wird
    test_calculate_percentage()
