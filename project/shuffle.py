class Shuffle:
    """
    Different kinds of shuffling techniques.
    
    >>> cards = [i for i in range(52)]
    >>> cards[25]
    25
    >>> mod_oh = Shuffle.modified_overhand(cards, 1)
    >>> mod_oh[0]
    25
    >>> mod_oh[25] 
    24
 
    >>> mongean_shuffle = Shuffle.mongean(mod_oh)
    >>> mongean_shuffle[0]
    51
    >>> mongean_shuffle[26]
    25

    #MY TESTS
    >>> cards2 = [i for i in range(1, 5)]
    >>> Shuffle.mongean(cards2)
    [4, 2, 1, 3]

    >>> cards3 = [i for i in range(1, 6)]
    >>> Shuffle.modified_overhand(cards3, 2)
    [1, 2, 3, 4, 5]

    >>> cards4 = [1, 3, 2, 4, 5]
    >>> Shuffle.modified_overhand(cards4, 2)
    [1, 3, 2, 4, 5]

    >>> cards5 = [3, 2, 1, 4]
    >>> Shuffle.modified_overhand(cards5, 2)
    [1, 2, 3, 4]

    >>> cards6 = [1, 2, 3, 4, 5]
    >>> Shuffle.mongean(cards6)
    [4, 2, 1, 3, 5]

    >>> cards7 = [5, 4, 7, 1, 2, 3, 6]
    >>> Shuffle.modified_overhand(cards7, 4)
    [2, 5, 4, 1, 7, 3, 6]
    """    
        
    def modified_overhand(cards, num):
        """
        Takes `num` cards from the middle of the deck and puts them at the
        top. 
        Then decrement `num` by 1 and continue the process till `num` = 0. 
        When num is odd, the "extra" card is taken from the bottom of the
        top half of the deck.
        """
        
        # Use Recursion.
        # Note that the top of the deck is the card at index 0.
        assert isinstance(cards, list)
        #assert all([isinstance(card, int) for card in cards])
        assert isinstance(num, int)

        if num == 0:
            return cards

        moved_cards = []
        counter = num
        mid = 0

        while counter != 0:
            if len(cards) % 2 == 0:
                mid = (len(cards) // 2) - 1
                moved_cards = [cards[mid]] + moved_cards
            else:
                mid = len(cards) // 2
                moved_cards = moved_cards + [cards[mid]]
            cards = cards[0:mid] + cards[mid + 1:]
            counter -= 1
        
        cards = moved_cards + cards
        return Shuffle.modified_overhand(cards, num - 1)
                    
    
    def mongean(cards):
        """
        Implements the mongean shuffle. 
        Check wikipedia for technique description. Doing it 12 times restores the deck.
        """
        
        # Remember that the "top" of the deck is the first item in the list.
        # Use Recursion. Can use helper functions.
        """
        if len(cards) <= 1:
            return cards
        if len(cards) % 2 == 0:
            return Shuffle.mongean([cards[len(cards) - 1]]) + Shuffle.mongean(cards[:len(cards) - 1])
        else:
            return Shuffle.mongean(cards[:len(cards) - 1]) + Shuffle.mongean([cards[len(cards) - 1]])
            """
            
        if not all([isinstance(item, list) for item in cards]):
            cards = [cards, []]
        if len(cards[1]) % 2 == 0:
            cards[1] = cards[1] + [cards[0][0]]
        elif len(cards[1]) % 2 == 1:
            cards[1] = [cards[0][0]] + cards[1]
        cards[0].pop(0)

        if len(cards[0]) == 0:
            return cards[1]
        return Shuffle.mongean(cards)
        
    