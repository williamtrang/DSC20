from card import Card
from hand import PlayerHand, DealerHand
from shuffle import Shuffle

class Deck:
    """
    Card deck of 52 cards.

    >>> deck = Deck()
    >>> deck.get_cards()[:5]
    [(2, clubs), (2, diamonds), (2, hearts), (2, spades), (3, clubs)]

    >>> deck.shuffle(modified_overhand=2, mongean=3)
    >>> deck.get_cards()[:5]
    [(A, clubs), (Q, clubs), (10, clubs), (7, diamonds), (5, diamonds)]

    >>> hand = PlayerHand()
    >>> deck.deal_hand(hand)
    >>> deck.get_cards()[0]
    (Q, clubs)
    """

    # Class Attribute(s)
    cards = []

    def __init__(self):
        """
        Creates a Deck instance containing cards sorted in ascending order.
        """
        suits = ['clubs', 'diamonds', 'hearts', 'spades']
        royals = ['J', 'Q', 'K', 'A']
        min_num = 2
        max_num = 10
        all_ranks = [i for i in range(min_num, max_num + 1)] + royals

        all_cards = [[Card(rank, suit) for suit in suits] for rank in all_ranks]
        [[self.cards.append(card) for card in lst] for lst in all_cards]

    def shuffle(self, **shuffle_and_count):
        """Shuffles the deck using a variety of different shuffles.

        Parameters:
            shuffle_and_count: keyword arguments containing the
            shuffle type and the number of times the shuffled
            should be called.
        """
        ...

    def deal_hand(self, hand):
        """
        Takes the first card from the deck and adds it to `hand`.
        """
        assert isinstance(hand, (PlayerHand, DealerHand))

    def get_cards(self):
        return self.cards
