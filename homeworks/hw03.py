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

    >>> sort_by_index([3, 2, 0, 1], ['three', 'two', 'zero', 'one'])
    [('one', 3, 0), ('zero', 2, 1), ('three', 0, 2), ('two', 1, 3)]
    """
    assert isinstance(index, list)
    assert isinstance(array, list)
    assert len(set(index)) == len(array)
    assert all([isinstance(idx, int) for idx in index])
    assert all([i in range(len(index)) for i in index])
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
    >>> intersection('aaabbbccc', 'bbbcccaaa')
    ''

    >>> intersection('2345', '12358459374ffdhk~!#*')
    '5'
    
    >>> intersection('#RELATABLE!', '#relatable!')
    '#!'
    """
    assert isinstance(str1, str)
    assert isinstance(str2, str)
    return ''.join([str1[i] \
        for i in range(0, min([len(str1), len(str2)])) if str1[i] == str2[i]])


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

    >>> decode(' i DloSCve')
    'DSC I LOVE'
    """
    assert isinstance(to_decode, str)
    assert to_decode.lower() != to_decode
    assert to_decode.replace(' ', '').isalpha()
    return ''.join([a for a in to_decode if a.isupper()]) \
        + ''.join([a.upper() for a in to_decode if not a.isupper()])


# Question 4
def find_closest_stores(friends, stores):
    """
    Finds the closest store to each friend based
    on absolute distance from the store.

    Parameters:
        friends: Dictionary with friend names as keys
        and point location as values.
        stores: Dictionary with store names as keys
        and point locations as values.
    Returns:
        Dictionary with friends names as keys and the
        store closest to them as values.

    >>> friends1 = {'rob': 10, 'bob': 12}
    >>> stores1 = {'walmart': 11, 'costco': 12}
    >>> find_closest_stores(friends1, stores1)
    {'rob': 'walmart', 'bob': 'costco'}

    >>> friends2 = {'bob': 12}
    >>> stores2 = {'target': 12, 'costco': 12}
    >>> find_closest_stores(friends2, stores2)
    {'bob': 'costco'}

    # My doctests

    >>> friends3 = {'joe': 10, 'jack': 20}
    >>> stores3 = {'target': 5, 'walmart': 16}
    >>> find_closest_stores(friends3, stores3)
    {'joe': 'target', 'jack': 'walmart'}

    >>> friends4 = {'bob': 12}
    >>> stores4 = {'target': 12, 'costco': 12, 'apple': 12}
    >>> find_closest_stores(friends4, stores4)
    {'bob': 'apple'}

    >>> friends5 = {'joe': 0, 'jack': 2.5}
    >>> stores5 = {'target': 1.25, 'walmart': 1}
    >>> find_closest_stores(friends5, stores5)
    {'joe': 'walmart', 'jack': 'target'}
    """
    return {names: min([(abs(distance - locations), store) \
            for store, distance in stores.items()])[1] \
            for names, locations in friends.items()}


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

    # My doctests
    >>> average_housing({'LA': [782900, 1368800, 599000, 750000], \
                        2: [746600, 697100, 989900, 785000], \
                        'BNY': [675000, 239000, 789000, 1049000]})
    Traceback (most recent call last):
    ...
    AssertionError

    >>> average_housing(47)
    Traceback (most recent call last):
    ...
    AssertionError

    >>> average_housing({'LA': [1, 4, 5, -2], 'SD': [1, 3, -9999], \
        'JOE': [1, 2, 3]})
    'JOE'

    >>> average_housing({'JOE': 124})
    Traceback (most recent call last):
    ...
    AssertionError
    """
    assert isinstance(house_prices, dict)
    assert all([isinstance(keys, str) for keys in house_prices.keys()])
    assert all([isinstance(values, list) for values in house_prices.values()])
    null_value = -9999
    return min([(sum([i for i in values if i != null_value]) / \
                len([i for i in values if i != null_value]), keys) \
                for keys, values in house_prices.items()])[1]


# Question 6
def create_id(names, commands):
    """
    Transforms a list of ids based on given list of commands.

    Parameters:
        names: Starting list of names to transform.
        commands: List of tuples containing transformations to 
        perform on the names list.
    Returns: 
        List of names that has been transformed.

    >>> create_id(["TomNook", "Isabelle"], [('upper', 2)])
    ['TOmNoOk', 'ISaBeLlE']
    >>> create_id(["TomNook", "Isabelle"], [('last', 5), ('remove', 0)])
    ['belle']
    >>> create_id(["TomNook", "Isabelle"], [('first', 4), \
('insert', 2, 'Mabel'), ('length', 4)])
    ['TomN', 'Isab', 'Ma5bel']

    # My doctests
    >>> create_id(['HappyNewYear', 'Merry Christmas'], [('upper', 2), \
        ('last', 9), ('remove', 1), ('insert', 1, 'Halloween'), \
            ('first', 5), ('length', 1)])
    ['Py5NeW', 'Ha5llo']

    >>> create_id(['HappyNewYear', 'Merry Christmas'], [('remove', 1), \
        ('insert', 0, 'Halloween')])
    ['Halloween', 'HappyNewYear']

    >>> create_id(['Isabelle', 'TomNook'], [('last', 4), \
        ('insert', 1, 'Resetti'), ('upper', 4)])
    ['ellE', 'ResEtti', 'NooK']
    """
    string_half = 2
    commands_dict = {
        'upper': lambda string, count: ''.join([string[i].upper() \
                if (i+1) % count == 0 else string[i]
                for i in range(0, len(string))]),
        'first': lambda string, count: string[:count],
        'last': lambda string, count: string[(len(string) - count):],
        'insert': lambda lst, index, string: lst.insert(index, string),
        'remove': lambda lst, index: lst.pop(index),
        'length': lambda string, amount: string[:len(string) // string_half] \
                    + str(len(string)) + string[len(string) // string_half:] \
                    if len(string) > amount else string
    }

    for i in range(0, len(commands)):
        curr_command = commands[i][0]
        comm_value = commands[i][1]
        if curr_command not in ['insert', 'remove']:
            for j in range(0, len(names)):
                names[j] = commands_dict[curr_command](names[j], comm_value)
        elif curr_command == 'remove':
            commands_dict[curr_command](names, comm_value)
        elif curr_command == 'insert':
            add_string_index = 2
            add_string = commands[i][add_string_index]
            commands_dict[curr_command](names, comm_value, add_string)
    return names
