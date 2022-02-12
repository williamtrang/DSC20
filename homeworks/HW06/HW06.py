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
    >>> all([isinstance(ans, int) and 1 <= ans <= 8 for ans in answers])
    True
    """
    # REPLACE ... WITH YOUR ANSWERS (1-9, duplicates allowed) #
    return 


#Question2
def find_the_word(lst, word):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

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

    """
    if len(lst) <= 1:
        return int(word in lst)
    return find_the_word([lst[0]], word) + find_the_word(lst[1:], word)


#Question3.1
def corrupt_string(input, to_insert):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> corrupt_string('tickets', '#')
    't#i#c#k#e#t#s#'
    >>> corrupt_string('', '@')
    ''
    >>> corrupt_string('buy now', '-')
    'b-u-y- -n-o-w-'

    # Add AT LEAST 3 doctests below, DO NOT delete this line
    """
    if len(input) == 0:
        return input
    elif len(input) == 1:
        return input + to_insert
    return corrupt_string(input[0], to_insert) + corrupt_string(input[1:], to_insert)


# Question 3.2
def corrupt_list(lst, word, to_insert):
    """

    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

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
    """
    if len(lst) <= 1:
        try:
            if lst[0] == word:
                return [corrupt_string(word, to_insert)]
        except:
            return []
    return [corrupt_list([lst[0]], word, to_insert) + corrupt_list([lst[1:], word, to_insert])]

            
#Question4
def corrupt_with_vowels(input):
    """

    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> corrupt_with_vowels('buy and sell')
    'by nd sll'
    >>> corrupt_with_vowels('gold gold gold')
    'gld gld gld'
    >>> corrupt_with_vowels('AeI oU')
    ' '

    # Add AT LEAST 3 doctests below, DO NOT delete this line
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
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> where_to_go(17, 17, 'left')
    '17'
    >>> where_to_go(1, 8, ',')
    '1,2,3,4,5,6,7,8'
    >>> where_to_go(8, 1, '->')
    '8->7->6->5->4->3->2->1'

    # Add AT LEAST 3 doctests below, DO NOT delete this line
    """
    return
