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


def calculate_percentage(total_hands, combination_count):
    return (combination_count / total_hands) * 100

total_games = 100000
royal_flush_count = 0
straight_flush_count = 0
full_house_count = 0
flush_count = 0
straight_count = 0
pair_count = 0
four_of_a_kind_count = 0
three_of_a_kind_count = 0

for _ in range(total_games):
    hand = getHand()  # Ziehe eine Hand

    # Zähle die verschiedenen Kombinationen
    if isRoyalFlush(hand):
        royal_flush_count += 1
    elif isStraightFlush(hand):
        straight_flush_count += 1
    elif isFullHouse(hand):
        full_house_count += 1
    elif isFlush(hand):
        flush_count += 1
    elif strasse(hand):
        straight_count += 1
    elif hasPair(hand) == 2:
        pair_count += 2
    elif hasPair(hand) == 1:
        pair_count += 1
    elif vierling(hand):
        four_of_a_kind_count += 1
    elif drilling(hand):
        three_of_a_kind_count += 1


print(f"Royal Flush: {calculate_percentage(total_games, royal_flush_count):.4f}%")
print(f"Straight Flush: {calculate_percentage(total_games, straight_flush_count):.4f}%")
print(f"Full House: {calculate_percentage(total_games, full_house_count):.4f}%")
print(f"Flush: {calculate_percentage(total_games, flush_count):.4f}%")
print(f"Straight: {calculate_percentage(total_games, straight_count):.4f}%")
print(f"Pairs: {calculate_percentage(total_games, pair_count):.4f}%")
print(f"Four of a Kind: {calculate_percentage(total_games, four_of_a_kind_count):.4f}%")
print(f"Three of a Kind: {calculate_percentage(total_games, three_of_a_kind_count):.4f}%")

