import random


def getDeck():
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['Herz', 'Karo', 'Pik', 'Kreuz']
    deck = [f'{value} {suit}' for value in values for suit in suits]
    return deck


def getHand(size=5):
    deck = getDeck()  # Erstelle ein Deck
    random.shuffle(deck)  # Mische das Deck
    hand = deck[:size]  # Ziehe die ersten `size` Karten
    return hand


def drilling(hand):
    value_count = {}
    for card in hand:
        value = card.split()[0]
        if value in value_count:
            value_count[value] += 1
        else:
            value_count[value] = 1

    for count in value_count.values():
        if count == 3:
            return True
    return False


def vierling(hand):
    value_count = {}
    for card in hand:
        value = card.split()[0]
        if value in value_count:
            value_count[value] += 1
        else:
            value_count[value] = 1

    for count in value_count.values():
        if count == 4:
            return True
    return False


def hasPair(hand):
    value_count = {}

    # Count occurrences of each value in the hand
    for card in hand:
        value = card.split()[0]  # Extract the value from the card
        if value in value_count:
            value_count[value] += 1
        else:
            value_count[value] = 1
    pairs = 0

    for count in value_count.values():
        if count == 2:
            pairs += 1

    return pairs


def strasse(hand):
    # Definition der Kartenwerte in der richtigen Reihenfolge
    value_order = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    # Extrahiere die Werte aus der Hand und sortiere sie
    values_in_hand = sorted([card.split()[0] for card in hand], key=lambda x: value_order.index(x))

    # Überprüfen auf eine Straße
    for i in range(len(values_in_hand) - 4):  # Gehe durch die Werte in der Hand
        # Überprüfen, ob die fünf aufeinanderfolgenden Werte sind
        if (value_order.index(values_in_hand[i + 1]) == value_order.index(values_in_hand[i]) + 1 and
                value_order.index(values_in_hand[i + 2]) == value_order.index(values_in_hand[i]) + 2 and
                value_order.index(values_in_hand[i + 3]) == value_order.index(values_in_hand[i]) + 3 and
                value_order.index(values_in_hand[i + 4]) == value_order.index(values_in_hand[i]) + 4):
            return True  # Eine Straße gefunden

    return False  # Keine Straße gefunden


def isFlush(hand):
    # Extrahiere die Farben aus der Hand
    suits = [card.split()[1] for card in hand]  # Die Farbe jeder Karte extrahieren

    # Überprüfen, ob alle Karten die gleiche Farbe haben
    return len(set(suits)) == 1  # Wenn nur eine Farbe in der Menge vorhanden ist, gibt es einen Flush


def isFullHouse(hand):
    value_count = {}

    # Zähle die Häufigkeit der Kartenwerte
    for card in hand:
        value = card.split()[0]  # Extrahiere den Wert (z.B. "3" von "3 Herz")
        if value in value_count:
            value_count[value] += 1
        else:
            value_count[value] = 1

    # Prüfen auf genau einen Drilling und genau ein Paar
    has_three_of_a_kind = False
    has_pair = False

    for count in value_count.values():
        if count == 3:
            has_three_of_a_kind = True
        elif count == 2:
            has_pair = True

    # Ein Full House hat genau einen Drilling und ein Paar
    return has_three_of_a_kind and has_pair


def isStraightFlush(hand):
    # Überprüfe, ob die Hand ein Flush ist
    if not isFlush(hand):
        return False  # Wenn kein Flush vorliegt, kann es auch kein Straight Flush sein

    # Definition der Kartenwerte in der richtigen Reihenfolge
    value_order = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    # Extrahiere die Werte aus der Hand
    values_in_hand = sorted([card.split()[0] for card in hand], key=lambda x: value_order.index(x))

    # Überprüfen, ob es eine Straße ist
    for i in range(len(values_in_hand) - 4):
        # Überprüfen, ob die fünf aufeinanderfolgenden Werte sind
        if (value_order.index(values_in_hand[i + 1]) == value_order.index(values_in_hand[i]) + 1 and
                value_order.index(values_in_hand[i + 2]) == value_order.index(values_in_hand[i]) + 2 and
                value_order.index(values_in_hand[i + 3]) == value_order.index(values_in_hand[i]) + 3 and
                value_order.index(values_in_hand[i + 4]) == value_order.index(values_in_hand[i]) + 4):
            return True  # Eine Straße in der gleichen Farbe (Straight Flush) gefunden

    return False  # Kein Straight Flush gefunden


def isRoyalFlush(hand):
    # Definition der Royal Flush Werte
    royal_values = {'10', 'J', 'Q', 'K', 'A'}

    # Überprüfe, ob die Hand ein Flush ist
    if not isFlush(hand):
        return False  # Wenn kein Flush vorliegt, kann es auch kein Royal Flush sein

    # Extrahiere die Werte aus der Hand
    values_in_hand = {card.split()[0] for card in hand}  # Verwende ein Set für die Werte

    # Überprüfe, ob alle Royal Flush Werte in der Hand sind
    return royal_values.issubset(values_in_hand)

    # Hauptprogramm


for i in range(10):
    hand = getHand()  # Ziehe eine Hand

    # Überprüfe die Pokerhände und gib nur einzigartige Hände aus
    if isRoyalFlush(hand):
        print("Ja, du hast einen Royal Flush.")
        print(hand)
    elif isStraightFlush(hand):
        print("Ja, du hast einen Straight Flush.")
        print(hand)
    elif isFullHouse(hand):
        print("Ja, du hast ein Full House.")
        print(hand)
    elif isFlush(hand):
        print("FLUSHHHH!!!")
        print(hand)
    elif strasse(hand):
        print("Du HAST EINE STRASSE!!!")
        print(hand)
    elif hasPair(hand) == 2:
        print("Ja, du hast zwei Paare in deiner Hand.")
        print(hand)
    elif hasPair(hand) == 1:
        print("Ja, du hast ein Paar in deiner Hand.")
        print(hand)
    elif vierling(hand):
        print("Ja, du hast ein 4a Paar in deiner Hand.")
        print(hand)
    elif drilling(hand):
        print("Ja, du hast ein 3a Paar in deiner Hand.")
        print(hand)
    else:
        print("Nein, du hast kein Paar in deiner Hand.")
