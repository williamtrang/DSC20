
"""
DSC 20 Homework 10
Name: William Trang
PID:  A16679845
"""

from util import Stack, Queue

# Question 1
def parentheses_checker(expression):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> parentheses_checker("(((]})")
    False
    >>> parentheses_checker("(")
    False
    >>> parentheses_checker("(){}[]]")
    False
    >>> parentheses_checker("(   x   )")
    True
    >>> parentheses_checker("a()b{}c[]d")
    True
    >>> parentheses_checker("")
    True

    # Add at least 3 doctests below #
    
    """
    # YOUR CODE GOES HERE #
    


# Question 2
def run_around(n, m):
    """
    n is the number of players in the circle
    m is the number of the player removed from a game
    functions prints the number of removed player, in order
    >>> run_around(6,3)
    3
    6
    4
    2
    5
    1
    >>> run_around(-1,-2)
    Traceback (most recent call last):
    ...
    ValueError: m and n should be positive!
    >>> run_around('5','1')
    Traceback (most recent call last):
    ...
    TypeError: Invalid input data type.

    # Add at least 3 doctests below #
    
    """
    # YOUR CODE GOES HERE #

   
# Question 3 (extra credit, you are on your own)

def choices_choices(candidate, pattern, possibility):
    """
    Append all possible words to possibility list
​
    >>> p = []
    >>> choices_choices(['t','p','h'], "_ower", p)
    >>> p
    ['tower', 'power', 'hower']
​
    >>> p = []
    >>> choices_choices(['w','c','d'], "_o_er", p)
    >>> p
    ['wocer', 'woder', 'cower', 'coder', 'dower', 'docer']
​
    >>> p = []
    >>> choices_choices(['w','c','d'], "coder", p)
    >>> p
    ['coder']

    # Add at least 3 doctests below #
    
    """
    # YOUR CODE GOES HERE #



