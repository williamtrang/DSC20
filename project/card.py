class Card:
    """
    Card class.

    # Doctests for str and repr
    >>> card_1 = Card("A", "spades")
    >>> print(card_1)
    ____
    |A  |
    | ♠ |
    |__A|
    >>> card_1
    (A, spades)
    >>> card_2 = Card("K", "spades")
    >>> print(card_2)
    ____
    |K  |
    | ♠ |
    |__K|
    >>> card_2
    (K, spades)
    >>> card_3 = Card("A", "diamonds")
    >>> print(card_3)
    ____
    |A  |
    | ♦ |
    |__A|
    >>> card_3
    (A, diamonds)

    # Doctests for comparisons
    >>> card_1 < card_2
    False
    >>> card_1 > card_2
    True
    >>> card_3 > card_1
    False

    # Doctests for set_visible()
    >>> card_3.set_visible(False)
    >>> print(card_3)
    ____
    |?  |
    | ? |
    |__?|
    >>> card_3
    (?, ?)
    >>> card_3.set_visible(True)
    >>> print(card_3)
    ____
    |A  |
    | ♦ |
    |__A|
    >>> card_3
    (A, diamonds)
    """

    # Class Attribute(s)

    def __init__(self, rank, suit, visible=True):
        """
        Creates a card instance and asserts that the rank and suit are valid.
        """
        assert isinstance(rank, (int, str))
        assert isinstance(suit, str)
        assert isinstance(visible, bool)
        
        suits = ['diamonds', 'clubs', 'hearts', 'spades']
        royals = ['J', 'Q', 'K', 'A']
        min_num = 2
        max_num = 10
        all_ranks = [i for i in range(min_num, max_num + 1)] + royals

        assert suit in suits
        assert rank in all_ranks

        self.rank = rank
        self.suit = suit
        self.visible = visible
        

    def __lt__(self, other_card):
        suit_vals = {'clubs': 1,
                    'diamonds': 2,
                    'hearts': 3,
                    'spades': 4}
        
        rank_vals = {2: 2,
                    3: 3,
                    4: 4,
                    5: 5,
                    6: 6,
                    7: 7,
                    8: 8,
                    9: 9,
                    10: 10,
                    'J': 11,
                    'Q': 12,
                    'K': 13,
                    'A': 14}

        if suit_vals[self.get_suit()] < suit_vals[other_card.get_suit()]:
            return True
        elif suit_vals[self.get_suit()] == suit_vals[other_card.get_suit()]:
            if rank_vals[self.get_rank()] < rank_vals[other_card.get_rank()]:
                return True
            return False
        return False

    def __str__(self):
        """
        Returns ASCII art of a card with the rank and suit. If the card is
        hidden, question marks are put in place of the actual rank and suit.

        Examples:
        ____
        |A  |
        | ♠ |
        |__A|
        ____
        |?  |
        | ? |
        |__?|             
        """
        ...

    def __repr__(self):
        """
        Returns (<rank>, <suit>). If the card is hidden, question marks are
        put in place of the actual rank and suit.           
        """        
        if self.visible:
            return (self.get_rank(), self.get_suit())
        return ('?', '?')

    def get_rank(self):
        return self.rank
    
    def get_suit(self):
        return self.suit

    def set_visible(self, visible):
        assert isinstance(visible, bool)
        self.visible = visible
    