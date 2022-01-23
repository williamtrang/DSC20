"""
DSC 20 Homework 03
Name: William Trang
PID: A16679845
"""

### Question 1
def sort_by_index_with_for_loop(index, array):
    """
    Sort the array with the given index and return a list of
    (<element>, <original index>, <new index>) tuples.

    Parameters:
        index: List of length n that contains interger 0 to n-1.
        array: List of length n.
    Returns:
        A list of length n containing
        (<element>, <original index>, <new index>) tuples or an empty list
        if n is 0.

    >>> sort_by_index_with_for_loop([ 0, 4, 2, 3, 1], ["zero", "four", "two", \
"three", "one"])
    [('zero', 0, 0), ('one', 4, 1), ('two', 2, 2), ('three', 3, 3), \
('four', 1, 4)]
    """
    sorted_list = []
    for i in range(0, len(array)):
        sorted_list.append((array[index[i]], index[i], i))
    return sorted_list


def sort_by_index(index, array):
    """
    Sort the array with the given index and return a list of
    (<element>, <original index>, <new index>) tuples. Throw an assertion
    error (thrown by failed asserts automatically) if the arguments passed
    are invalid.

    >>> sort_by_index([ 0, 4, 2, 3, 1], \
["zero", "four", "two", "three", "one"])
    [('zero', 0, 0), ('one', 4, 1), ('two', 2, 2), ('three', 3, 3), \
('four', 1, 4)]

    >>> sort_by_index([ 0.0, 4.0, 2.0, 3.0, 1.0], \
["zero", "four", "two", "three", "one"])
    Traceback (most recent call last):
    ...
    AssertionError

    >>> sort_by_index([ 0, 4, 2, 3, 0], \
["zero", "four", "two", "three", "one"])
    Traceback (most recent call last):
    ...
    AssertionError

    >>> sort_by_index([ 0, 4, 2, 3], ["zero", "four", "two", "three", "one"])
    Traceback (most recent call last):
    ...
    AssertionError

    # My doctests #
    >>> sort_by_index([1, 4, 3, 2], ['one', 'four', 'three', 'two'])
    Traceback (most recent call last):
    ...
    AssertionError

    >>> sort_by_index([],[])
    []
    """
    assert type(index) == list
    assert type(array) == list
    assert len(set(index)) == len(array)
    assert all([isinstance(idx, int) for idx in index])
    assert [i in range(len(index)) for i in index] == ([True] * len(index))
    return [(array[index[i]], index[i], i) for i in range(0, len(index))]


### Question 2
def intersection(str1, str2):
    """
    Finds the intersection of str1 and str2 where an intersection is
    determined by str1[i] == str[i].

    >>> intersection("bbbaabbb", "dddaaddd")
    'aa'
    >>> intersection("bbbaabbb", "dddaa")
    'aa'
    >>> intersection("bbbaabbb", "ddd")
    ''
    >>> intersection("bbbbbbbbb", "ababababa")
    'bbbb'
    >>> intersection("bbbaabbb", 1)
    Traceback (most recent call last):
    ...
    AssertionError

    # My doctests
    """
    assert type(str1) == str
    assert type(str2) == str
    return


### Question 3
def decode(to_decode):
    """
    Moves all the uppercase character to the beginning of the
    string and case the lowercase characters to uppercase.

    Parameters:
       to_decode: A string that is not all lowercase
    Returns:
       A decoded string.

    >>> decode(" neHAw yePParY")
    'HAPPY NEW YEAR'
    >>> decode(" Gof ERriALTvia")
    'GERALT OF RIVIA'
    >>> decode("ALL UPPERCASE")
    'ALLUPPERCASE '
    >>> decode("all lowercase")
    Traceback (most recent call last):
    ...
    AssertionError

    # My doctests
    >>> decode('324798578~!!')
    Traceback (most recent call last):
    ...
    AssertionError
    >>> decode('3A4a')
    Traceback (most recent call last):
    ...
    AssertionError
    """
    assert type(to_decode) == str
    assert to_decode.lower() != to_decode
    assert to_decode.replace(' ', '').isalpha()
    return ''.join([a for a in to_decode if a.isupper()])\
         + ''.join([a.upper() for a in to_decode if not(a.isupper())])


# Question 4
def find_closest_stores(friends, stores):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> friends1 = {'rob': 10, 'bob': 12}
    >>> stores1 = {'walmart': 11, 'costco': 12}
    >>> find_closest_stores(friends1, stores1)
    {'rob': 'walmart', 'bob': 'costco'}

    >>> friends2 = {'bob': 12}
    >>> stores2 = {'target': 12, 'costco': 12}
    >>> find_closest_stores(friends2, stores2)
    {'bob': 'costco'}
    """
    # YOR CODE GOES HERE #
    return


# Question 5
def average_housing(house_prices):
    """
    Calculate the lowest average price of houses in given areas while also
    ignoring the null value (-9999).

    Parameters:
        house_prices: A dictionary containing locations and their list
        of house prices.
    Returns:
        The house location with the lowest average price when ignoring null
        values.

    >>> average_housing({'LA': [782900, 1368800, -9999, -9999], \
                        'SD': [746600, 697100, 989900, 785000], \
                        'BNY': 675000})
    Traceback (most recent call last):
    ...
    AssertionError
    >>> average_housing({92122: [746600, 697100, 989900, 785000]})
    Traceback (most recent call last):
    ...
    AssertionError
    >>> average_housing({'LA': [782900, 1368800, 599000, 750000], \
                        'SD': [746600, 697100, 989900, 785000], \
                        'BNY': [675000, 239000, 789000, 1049000]})
    'BNY'
    >>> average_housing({'LA': [782900, 1368800, -9999, -9999], \
                        'SD': [746600, 697100, 989900, 785000], \
                        'BNY': [675000, -9999, 789000, 1049000]})
    'SD'
    >>> average_housing({'Acorn Blvd': [0, 1, 2], \
                        'Pine Ave': [4, 3, -9999], \
                        'Maple Lane': [3, -9999, 3, 3]})
    'Acorn Blvd'
    """
    assert type(house_prices) == dict
    return


# Question 6
def create_id(names, commands):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> create_id(["TomNook", "Isabelle"], [('upper', 2)])
    ['TOmNoOk', 'ISaBeLlE']
    >>> create_id(["TomNook", "Isabelle"], [('last', 5), ('remove', 0)])
    ['belle']
    >>> create_id(["TomNook", "Isabelle"], [('first', 4), \
('insert', 2, 'Mabel'), ('length', 4)])
    ['TomN', 'Isab', 'Ma5bel']
    """
    # YOUR CODE GOES HERE #
    return
