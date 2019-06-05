import re


def my_split(s):
    return filter(None, re.split(r'(\d+|[AJKQT])', s))


hands = {
    1: "high",
    2: "pair",
    3: "two pair",
    4: "three OAK",
    5: "straight",
    6: "flush",
    7: "full house",
    8: "4 OAK",
    9: "straight flush",
    10: "Royal Flush"
}

file = open("poker.txt", 'r')


def royal_flush(player_hand):
    if flush(player_hand) and straight(player_hand) and sorted(
            player_hand[0])[-1] == 14:
        return 1
    else:
        return 0


def straight_flush(player_hand):
    if flush(player_hand) and straight(player_hand):
        return 1
    else:
        return 0


def four_oak(player_hand):
    for value in player_hand[0]:
        if player_hand[0].count(value) == 4:
            return 1
    else:
        return 0


def full_house(player_hand):
    if three_oak(player_hand) and pair(player_hand):
        return 1
    else:
        return 0


def flush(player_hand):
    if player_hand[1].count(player_hand[1][0]) == 5:
        return 1
    else:
        return 0


def straight(player_hand):
    order_values = sorted(player_hand[0])
    low_card = order_values[0]
    high_card = order_values[1]

    for idx, value in enumerate(order_values[1:], 1):
        if value != low_card + idx:
            if high_card != 14:
                return 0

    if high_card != 14:
        return 1
    else:
        order_values.remove(14)
        order_values.insert(0, 1)
        low_card = order_values[0]
        for idx, value in enumerate(order_values[1:], 1):
            if value != low_card + idx:
                return 0
        else:
            return 1


def three_oak(player_hand):
    for values in player_hand[0][:3]:
        if player_hand[0].count(values) == 3:
            return 1
    else:
        return 0


def two_pairs(player_hand):
    count = 0
    for values in player_hand[0]:
        if player_hand[0].count(values) == 2:
            count += 1

    if count == 4:
        return 1
    else:
        return 0


def pair(player_hand):
    count = 0
    for values in player_hand[0]:
        if player_hand[0].count(values) == 2:
            count += 1

    if count == 2:
        return 1
    else:
        return 0


def hand(player_hand):
    if royal_flush(player_hand):
        return 10
    if straight_flush(player_hand):
        return 9
    if four_oak(player_hand):
        return 8
    if full_house(player_hand):
        return 7
    if flush(player_hand):
        return 6
    if straight(player_hand):
        return 5
    if three_oak(player_hand):
        return 4
    if two_pairs(player_hand):
        return 3
    if pair(player_hand):
        return 2

    return 1


def break_high(P1, P2):
    player1_values = sorted(P1[0], reverse=True)
    player2_values = sorted(P2[0], reverse=True)

    for p1_val, p2_val in zip(player1_values, player2_values):
        if p1_val > p2_val:
            return 1
        elif p2_val > p1_val:
            return 0


def break_pair(P1, P2):
    p1_high = 0
    p2_high = 0
    for value in P1[0]:
        if P1[0].count(value) == 2:
            p1_high = value
    for value in P2[0]:
        if P2[0].count(value) == 2:
            p2_high = value

    if p1_high > p2_high:
        return 1
    elif p2_high > p1_high:
        return 0
    else:
        return break_high(P1, P2)


def break_trips(P1, P2):
    p1_high = 0
    p2_high = 0
    for value in P1[0]:
        if P1[0].count(value) == 3:
            p1_high = value
    for value in P2[0]:
        if P2[0].count(value) == 3:
            p2_high = value

    if p1_high > p2_high:
        return 1
    elif p2_high > p1_high:
        return 0


def break_two_pair(P1, P2):
    p1_high = p1_low = 0
    p2_high = p2_low = 0
    for value in P1[0]:
        if P1[0].count(value) == 2:
            if p1_high != value:
                p1_high = value
            else:
                p1_low = value

    for value in P2[0]:
        if P2[0].count(value) == 2:
            if p2_high != value:
                p2_high = value
            else:
                p1_low = value

    if p1_high > p2_high:
        return 1
    elif p2_high > p1_high:
        return 0
    elif p1_low > p2_low:
        return 1
    elif p2_low > p1_low:
        return 0
    else:
        return break_high(P1, P2)


def break_straight(P1, P2):
    player1_order_values = sorted(P1[0])
    player2_order_values = sorted(P2[0])

    if player1_order_values[-1] > player2_order_values[-1]:
        return 1
    else:
        return 0


def break_flush(P1, P2):
    player1_order_values = sorted(P1[0])
    player2_order_values = sorted(P2[0])

    if player1_order_values[-1] > player2_order_values[-1]:
        return 1
    else:
        return 0


def tie_break(P1, P2, P1_hand):
    if P1_hand == 1:
        if break_high(P1, P2):
            return 1
        else:
            return 0

    if P1_hand == 2:
        if break_pair(P1, P2):
            return 1
        else:
            return 0

    if P1_hand == 3:
        if break_two_pair(P1, P2):
            return 1
        else:
            return 0

    if P1_hand == 4:
        if break_trips(P1, P2):
            return 1
        else:
            return 0

    if P1_hand == 5:
        if break_straight(P1, P2):
            return 1
        else:
            return 0

    if P1_hand == 6:
        if break_flush(P1, P2):
            return 1
        else:
            return 0


def who_wins(P1, P2):
    P1_hand = hand(P1)
    P2_hand = hand(P2)

    if P1_hand > P2_hand:
        return 1
    elif P2_hand > P1_hand:
        return 0
    else:
        return tie_break(P1, P2, P1_hand)


def to_num(card):
    if card == "T":
        return 10
    if card == "J":
        return 11
    if card == "Q":
        return 12
    if card == "K":
        return 13
    if card == "A":
        return 14
    return (int(card))


p1_score = 0
p2_score = 0
for line in file:
    cards = line.split()
    player1_initial_hand = cards[:5]
    player2_initial_hand = cards[5:]
    P1 = ([], [])
    P2 = ([], [])

    for p1_card, p2_card in zip(player1_initial_hand, player2_initial_hand):
        p1_split = list(my_split(p1_card))
        p2_split = list(my_split(p2_card))

        P1[0].append(to_num(p1_split[0]))
        P1[1].append(p1_split[1])
        P2[0].append(to_num(p2_split[0]))
        P2[1].append(p2_split[1])

    if who_wins(P1, P2):
        P1_hand = hand(P1)
        P2_hand = hand(P2)
        p1_score += 1
    else:
        P1_hand = hand(P1)
        P2_hand = hand(P2)
        p2_score += 1

print(p1_score, p2_score)
