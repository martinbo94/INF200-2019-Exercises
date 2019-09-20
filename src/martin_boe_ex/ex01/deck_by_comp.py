SUITS = ('C', 'S', 'H', 'D')
VALUES = range(1, 14)


def deck_loop():
    deck = []
    for suit in SUITS:
        for val in VALUES:
            deck.append((suit, val))
    return deck


def deck_comp():
    """This function returns a deck of cards where 1 equals ace and
    13 equals king etc. C is clubs, S is spade, H is hearts and D is diamonds"""
    deck = [(suit, val) for suit in SUITS for val in VALUES]
    return deck


if __name__ == '__main__':
    if deck_loop() != deck_comp():
        print('ERROR!')
