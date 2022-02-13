"""
DSC20 WI22 HW06
Name: William Trang
PID: A16679845
"""

# Question 1
def complexity_mc():
    """
    Write your answers to time complexity multiple-choice questions in this
    function. You don't need to add new doctests for this function.
    >>> answers = complexity_mc()
    >>> isinstance(answers, list)
    True
    >>> len(answers)
    10
    >>> all([isinstance(ans, int) and 1 <= ans <= 9 for ans in answers])
    True
    """
    # REPLACE ... WITH YOUR ANSWERS (1-9, duplicates allowed) #
    return 


#Question2
def find_the_word(lst, word):
    """
    Takes in input of a list and a string to look for,
    and returns the amount of times the string shows up
    in the list.

    Parameters:
        lst: Given list to search through.
        word: Word to search for in lst.
    Returns:
        Amount of times word shows up in lst.

    >>> find_the_word(["tickets"], "tickets")
    1
    >>> find_the_word(["selltickets", "tickets", "gold"], "tickets")
    1
    >>> find_the_word(["ticktok", "toktick"], "tickets")
    0
    >>> find_the_word([], "tickets")
    0
    >>> find_the_word(["ticketticket"], "tickets")
    0
    >>> find_the_word(["tickets", "who", "wants", "cheap", "tickets"],\
     "tickets")
    2
    >>> find_the_word(["tickets tickets", "ticketstickets"], "tickets")
    0

    # Add AT LEAST 3 doctests below, DO NOT delete this line
    >>> find_the_word(['foo', 'FOO', 'food', 'Foo', 'foo'], 'foo')
    2
    """
    if len(lst) <= 1:
        return int(word in lst)
    return find_the_word([lst[0]], word) + find_the_word(lst[1:], word)


#Question3.1
def corrupt_string(input, to_insert):
    """
    Takes in a base string input and another string to_insert.
    Corrupts the base string by making it so each character is
    followed by the string in to_insert and returns.

    Parameters:
        input: Base string that will be corrupted/modified.
        to_insert: String that is used to corrupt the base string.
    Returns:
        String input that has been corrupted by to_insert.

    >>> corrupt_string('tickets', '#')
    't#i#c#k#e#t#s#'
    >>> corrupt_string('', '@')
    ''
    >>> corrupt_string('buy now', '-')
    'b-u-y- -n-o-w-'

    # Add AT LEAST 3 doctests below, DO NOT delete this line
    >>> corrupt_string('foo', 'bar')
    'fbarobarobar'
    """
    if len(input) == 0:
        return input
    elif len(input) == 1:
        return input + to_insert
    return corrupt_string(input[0], to_insert) + corrupt_string(input[1:], to_insert)


# Question 3.2
def corrupt_list(lst, word, to_insert):
    """
    Takes in a list of strings, a string word to look for, and
    a string to_insert that will be used to corrupt instances
    of word in the list. Corrupts the strings in the list
    that are equal to word by adding to_insert after every
    character and returns the list.

    Parameters:
        lst: List of strings that will be corrupted.
        word: Word that will be corrupted in the list.
        to_insert: String that is used to corrupt the matching
        words in the list.
    Returns:
        List of strings with strings equal to word being corrupted.

    >>> corrupt_list(['tickets'], 'tickets','#')
    ['t#i#c#k#e#t#s#']
    >>> corrupt_list([], 'tickets','@')
    []
    >>> corrupt_list(['buy now', 'tickets'], 'tickets','-')
    ['buy now', 't-i-c-k-e-t-s-']
    >>> corrupt_list(['buy now', 'fake tickets'], 'tickets','-')
    ['buy now', 'fake tickets']
    >>> corrupt_list(['e-ticket', 'TiCkeTs'], 'tickets','-')
    ['e-ticket', 'TiCkeTs']

    # Add AT LEAST 3 doctests below, DO NOT delete this line
    >>> corrupt_list(['foo', 'food', 'Foo', 'foo'], 'foo', '1')
    ['f1o1o1', 'food', 'Foo', 'f1o1o1']

    >>> corrupt_list(['foo', 'food', 'Foo', 'foo', '', 'fooD'], 'foo', '1')
    ['f1o1o1', 'food', 'Foo', 'f1o1o1', '', 'fooD']

    >>> corrupt_list(['', 'Foo', ''], '', ',')
    ['', 'Foo', '']
    """
    if len(lst) <= 1:
        try:
            if lst[0] == word:
                return [corrupt_string(lst[0], to_insert)]
            return [lst[0]]
        except:
            return []
    return corrupt_list([lst[0]], word, to_insert) + corrupt_list(lst[1:], word, to_insert)

            
#Question4
def corrupt_with_vowels(input):
    """
    Takes in a base string input. Returns a
    string that has been corrupted by removing all
    the vowels (a, e, i, o, u) from it.

    Parameters:
        input: Base string that will be corrupted.
    Returns:
        String input with all vowels removed.

    >>> corrupt_with_vowels('buy and sell')
    'by nd sll'
    >>> corrupt_with_vowels('gold gold gold')
    'gld gld gld'
    >>> corrupt_with_vowels('AeI oU')
    ' '

    # Add AT LEAST 3 doctests below, DO NOT delete this line
    >>> corrupt_with_vowels('')
    ''
    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    if len(input) <= 1:
        if input.lower() in vowels:
            return ''
        return input
    return corrupt_with_vowels(input[0]) + corrupt_with_vowels(input[1:])


#Question 5
def where_to_go(point1, point2, separator):
    """
    Takes in two integers, point1 and point2, and a string separator.
    Returns all the integers between point1 and point2 with the
    string separator separating each integer.

    Parameters:
        point1: Starting point/integer.
        point2: Ending point/integer.
        separator: String to separate each integer with.
    Returns:
        String containing all integers between and including
        point1 and point2 separated by separator string.

    >>> where_to_go(17, 17, 'left')
    '17'
    >>> where_to_go(1, 8, ',')
    '1,2,3,4,5,6,7,8'
    >>> where_to_go(8, 1, '->')
    '8->7->6->5->4->3->2->1'

    # Add AT LEAST 3 doctests below, DO NOT delete this line
    >>> where_to_go(1, 5, '')
    '12345'

    >>> where_to_go(1, 5, 'nft')
    '1nft2nft3nft4nft5'
    """
    if point1 < point2:
        return str(point1) + separator + where_to_go(point1 + 1, point2, separator)
    elif point2 < point1:
        return str(point1) + separator + where_to_go(point1 - 1, point2, separator)
    elif point2 == point1:
        return str(point1)
