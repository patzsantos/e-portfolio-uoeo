from enum import Enum

class Card(object):
    """Standard playing card"""

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank


suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7','8', '9', '10', 'Jack', 'Queen', 'King']


def __str__(self):
    return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])

    def __repr__(self):
        return 'Card <{}. {}>'.format(self.rank_names[self.rank], self.suit_names[self.suit])

    def __lt__(self, other):
        return self.rank < other.rank

    def __gt__(self, other):
        return self.rank > other.rank

    def __eq__(self, other):
        return self.rank == other.rank


class Deck(object):
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in range(4) for rank in range (1,14)]

    def __str__(self):
        return '\n'.join([str(card) for card in self.cards])

    def __repr__(self):
        return "Deck <{}>".format(self.cards)

    def __len__(self):
        return len(self.cards)

    def shuffle(self):
        shuffle(self.cards)
        return "deck shuffled"

    def sort(self):
        self.cards.sort()
        return "deck sorted"

    def deal_hands(self, num_of_hands, cards_per_hand):
        if (num_of_hands * cards_per_hand) > len(self): msg = '\n{}  hands with {} cards each is {} cards\\nTotal cards left in deck: {}'.format(num_of_hands. cards_per_hand, num_of_hands * cards_per_hand, len(self))
        raise ValueError(msg)

    def deal_hands(self, num_of_hands, cards_per_hand):
        if (num_of_hands * cards_per_hand) > len(self):
            msg = '\n{} hands with {} cards each is {} cards\
            \nTotal cards left in deck: {}'.format(num_of_hands, cards_per_hand, num_of_hands * cards_per_hand,
                                                      len(self))
            raise ValueError(msg)
        else:
            hands = []
            for h in range(num_of_hands):
                hand = Hand()
                for c in range(cards_per_hand):
                    hand.cards.append(self.cards.pop())
                hands.append(hand)
            return hands


class Hand(object):
    def __init__(self):
        self.cards = []

    def __repr__(self):
        return "Hand <{}>".format(self.cards)


"""Reference: 

epequeno. (2016) ThinkPy-Solutions/ch18/18.03.py. Available from:
https://github.com/epequeno/ThinkPy-Solutions/blob/master/ch18/18.03.py [Accessed 19 January 2024]."""
