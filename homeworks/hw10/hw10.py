
"""
DSC 20 Homework 10
Name: William Trang
PID:  A16679845
"""

from util import Stack, Queue

# Question 1
def parentheses_checker(expression):
    """
    Checks if given string expression has closing
    parentheses for every opening parentheses and vice
    versa. Return True if it only has pairs of parentheses
    that line up and False if not.

    Parameters:
        expression: Given string input to check for parentheses.
    Returns:
        True if all opening parentheses are matched by the same
        kind of closing parentheses and vice versa.

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
    >>> parentheses_checker("((((())))")
    False

    >>> parentheses_checker("[[[(((]]]")
    False

    >>> parentheses_checker("[][][]()(){}{}{)")
    False

    >>> parentheses_checker("(daimyo)")
    True
    """
    opening = ['(', '[', '{']
    closing = [')', ']', '}']
    classification = {'(': 'paren',
                    ')': 'paren',
                    '{': 'brace',
                    '}': 'brace',
                    '[': 'bracket',
                    ']': 'bracket'}

    opening_stack = Stack()

    for i in expression:
        if i in opening:
            opening_stack.push(i)
        if i in closing:
            if opening_stack.size() == 0:
                return False
            if classification[opening_stack.peek()] == classification[i]:
                opening_stack.pop()
            else:
                return False

    if opening_stack.size() != 0:
        return False
    return True


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
    >>> run_around(5., 1)
    Traceback (most recent call last):
    ...
    TypeError: Invalid input data type.

    >>> run_around(8, 3)
    3
    6
    1
    5
    2
    8
    4
    7

    >>> run_around(8, 4)
    4
    8
    5
    2
    1
    3
    7
    6

    >>> run_around(0, 2)
    Traceback (most recent call last):
    ...
    ValueError: m and n should be positive!
    """
    if (not isinstance(n, int)) or (not isinstance(m, int)):
        raise TypeError('Invalid input data type.')
    if (m <= 0) or (n <= 0):
        raise ValueError('m and n should be positive!')

    queue = Queue()
    for i in range(1, n + 1):
        queue.enqueue(i)

    while queue.size() > 0:
        for i in range(m):
            if i == m - 1:
                print(queue.dequeue())
            else:
                queue.enqueue(queue.dequeue())


# Question 3 (extra credit, you are on your own)

def choices_choices(candidate, pattern, possibility):
    """
    Append all possible words to possibility list
    >>> p = []
    >>> choices_choices(['t','p','h'], "_ower", p)
    >>> p
    ['tower', 'power', 'hower']

    >>> p = []
    >>> choices_choices(['w','c','d'], "_o_er", p)
    >>> p
    ['wocer', 'woder', 'cower', 'coder', 'dower', 'docer']

    >>> p = []
    >>> choices_choices(['w','c','d'], "coder", p)
    >>> p
    ['coder']

    # Add at least 3 doctests below #

    """
    # YOUR CODE GOES HERE #
