import random


class Card:
    suits = {0: "hearts", 1: "tiles", 2: "clovers", 3: "pikes"}
    number = {
        1: "ace",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "10",
        11: "king",
        12: "lady",
        13: "Jack"
    }

    def __init__(self, number, suit):
        self.Number = number
        self.Suit = suit

    def print_info(self):
        print(Card.number[self.Number], Card.suits[self.Suit])

    def __eq__(self, other):
        if (self.Number == other.Number) and (self.Suit == other.Suit):
            return True
        return False


def card_make(user, other):
    all_card = []
    all_card.extend(user)
    all_card.extend(other)

    try:
        if len(all_card) < 52:
            number = random.randint(1, 13)
            suit = random.randint(0, 3)
            card = Card(number, suit)

            if all_card == []:
                user.append(card)

            else:
                while True:
                    find = False
                    for i_card in all_card:
                        if card == i_card:
                            find = True
                            break
                    if find:
                        number = random.randint(1, 13)
                        suit = random.randint(0, 3)
                        card = Card(number, suit)
                    else:
                        break

                user.append(card)
        else:
            raise BaseException
    except BaseException:
        print("End of card")


def print_cards(cards):
    for i_card in cards:
        i_card.print_info()


def sum_cards(cards):
    result = 0
    for i_card in cards:
        if i_card.Number == 1:
            if result < 21:
                result += 11
            else:
                result += 1
        elif i_card.Number > 10:
            result += 10
        else:
            result += i_card.Number
    return result


user_cards = []
computer_cards = []
for _ in range(2):
    card_make(user_cards, computer_cards)
    card_make(computer_cards, user_cards)

while True:
    print_cards(user_cards)
    action = input("\n1. take card\n2. stop\n")
    if action == "1":
        card_make(user_cards, computer_cards)
    else:
        break

user_result = sum_cards(user_cards)

if user_result == 21:
    print("user win")
else:
    computer_result = sum_cards(computer_cards)
    if (user_result < 21) and (user_result > computer_result):
        print("user win")
    else:
        print("computer win")

# TODO: У меня перебор, почему игра продолжается?
"""
2 hearts
9 clovers

1. take card
2. stop
1
2 hearts
9 clovers
7 pikes

1. take card
2. stop
1
2 hearts
9 clovers
7 pikes
5 tiles

1. take card
2. stop
"""