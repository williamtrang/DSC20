"""
DSC 20 Lab 05
Name: William Trang
PID: A16679845
"""

# pre-defined functions
def identity(x):
    return x

def square(x):
    return x**2

def cube(x):
    return x**3


# Q1
def vector_op(lst, func):
    """
    IMPORTANT: You should ONLY use one-line list comprehension.

    Make a function that applies given function to the given list.

    >>> lst = [1,2,3]
    >>> vector_op(lst, square)
    [1, 4, 9]
    >>> lst = [1,2,3,5]
    >>> vector_op(lst, lambda x: -x)
    [-1, -2, -3, -5]
    >>> vector_op(lst, identity)
    [1, 2, 3, 5]
    >>> lst = [10,20,30]
    >>> vector_op(lst, cube)
    [1000, 8000, 27000]
    """
    return [func(i) for i in lst]


# Q2
def matrix_op(lsts, func):
    """
    IMPORTANT: You should ONLY use one-line list comprehension.

    Make a function that applies given function to the given nested-list.

    >>> lsts = [[1,2], [3,4]]
    >>> matrix_op(lsts, square)
    [[1, 4], [9, 16]]
    >>> lsts = [[10, 20], [30, 40]]
    >>> matrix_op(lsts, lambda x: x / 10)
    [[1.0, 2.0], [3.0, 4.0]]
    >>> lsts = [[5,15], [25,35]]
    >>> matrix_op(lsts, identity)
    [[5, 15], [25, 35]]

    """
    return [[func(i) for i in lst] for lst in lsts]


# Q3
def hop_hop(lst, func):
    """
    IMPORTANT: You should ONLY use one-line list comprehension.

    Make a function that applies given function to the given list twice.

    >>> lst = [1,2,3]
    >>> hop_hop(lst, square)
    [1, 16, 81]
    >>> lst = [5,6,7,8]
    >>> hop_hop(lst, lambda x:x+1)
    [7, 8, 9, 10]
    >>> lst = [10,20,30]
    >>> hop_hop(lst, cube)
    [1000000000, 512000000000, 19683000000000]
    """
    return [func(func(i)) for i in lst]


# Q4
def hop_many(lst, func, iterations):
    """
    Make a function that applied given function to the given list for
    given number of iterations.

    >>> lst = [1,2,3]
    >>> hop_many(lst, square, 2)
    [1, 16, 81]
    >>> hop_many(lst, square, 3)
    [1, 256, 6561]
    >>> hop_many(lst, identity, 100)
    [1, 2, 3]
    >>> hop_many(lst, lambda x: x - 1, 4)
    [-3, -2, -1]
    """
    final = []
    for i in lst:
        for _ in range(iterations):
            i = func(i)
        final.append(i)
    return final


# Q5
def can_replace(func, n):
    """
    Write a higher-order function that takes in a function func
    and a value n. It return a function such that it takes in
    another function func2 and it will return True if func could
    be replaced by func2 at value n; False otherwise.

    >>> can_replace(lambda x: x, 1)(lambda x: x**2)
    True
    >>> can_replace(square, -1)(cube)
    False
    >>> can_replace(identity, -1)(identity)
    True
    """
    def inner(func2):
        return func2(n) == func(n)
    return inner


# Q6.1
def strange_sequence(num1, num2):
    """
    Write a function that takes two integers num1, num2 and
    returns an inner function that takes in an integer limit
    which will return a list of all integers from 1 to limit
    (both ends are included) but overrides those number with
    given rules.

    >>> inner = strange_sequence(1, 3)
    >>> inner(3)
    [5, 6, -1]
    >>> inner = strange_sequence(10, 15)
    >>> inner(3)
    ['nothing special', 'nothing special', 'nothing special']
    >>> inner = strange_sequence(10, 15)
    >>> inner(1)
    ['nothing special']
    """
    def gems(limit):
        gem_lst = []
        element = 0
        for number in range(1, limit + 1):
            element = number
            if (number % num1 == 0) and (number % num2 == 0) and (number == num1 + num2):
                element = 'gem found'
            elif (number % num1 == 0) and (number % num2 == 0):
                element = number - num1 - num2
            elif (number % num1 == 0):
                element = number + num1 + num2
            else:
                element = 'nothing special'
            gem_lst.append(element)
        return gem_lst
    return gems


# Q6.2
def param_for_gem():
    """
    Identify the parameters that will generate such "gem found".
    Once you find these three numbers (number, num1 and num2),
    return them in a list.

    >>> output = param_for_gem()
    >>> len(output) == 3
    True
    >>> all([isinstance(num, int) for num in output])
    True
    """
    return [2, 1, 1]
