
"""
DSC 20 Homework 09
Name: William Trang
PID:  A16679845
"""


# Question 1

def maze(coord, map):
    """
    Given `coord` as a tuple and `map` as list of strings, 
    return 'treasure!' if treasure can be reached by following the signs
    return 'sad' otherwise
​
    There is no cycle
​
    >>> map = [
    ... "..............",
    ... ".RRRD..RRRRD..",
    ... "...DL..U...D..",
    ... "...D...U.D.D..",
    ... "...RRRRU.D.*..",
    ... ".............."]
    >>> maze((1,1), map)
    'treasure!'
    >>> maze((0,0), map)
    'sad'
    >>> maze((3,9), map)
    'sad'
    >>> maze((4,11), map)
    'treasure!'

    # Add more tests

    """
    treasure_loc = (0, 0)
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == '*':
                treasure_loc = (i, j)

    if len(map) == 1:
        for i in map[0]:
            if coord == treasure_loc:
                return 'treasure!'
            if i == 'R':
                coord = (coord[0] + 1, coord[1])
            elif i == 'L':
                coord = (coord[0] - 1, coord[1])
            elif i == 'U':
                coord = (coord[0], coord[1] - 1)
            elif i == 'D':
                coord = (coord[0], coord[1] + 1)
    return maze(coord, map[0]) + maze(coord, map[1:])
            

# Question 2
def binary_search(target, arr, left, right):
    """
    
    >>> arr = [2, 3, 4, 10, 40]
    >>> target = 3
    >>> binary_search(target, arr, 0, 5)
    [[2, 3, 4, 10, 40], [2, 3]]

    >>> arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30]
    >>> target = 20
    >>> binary_search(target, arr, 0, 12)
    [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30], [8, 9, 10, 20, 30], [20, 30], [20]]

    >>> arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30]
    >>> target = 20
    >>> binary_search(target, arr, 0, 10)
    [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [7, 8, 9, 10], [10], []]

    >>> arr = [2, 3, 4, 10, 40]
    >>> target = 30
    >>> binary_search(target, arr, 0, 5)
    [[2, 3, 4, 10, 40], [10, 40], [10], []]

    # Add more tests

    """

    mid = int((left + right) / 2)
    if target == arr[mid]:
        return arr[left:right]
    elif target > arr[mid]:
        return binary_search(target, arr, mid + 1, right)
    elif target < arr[mid]:
        return binary_search(target, arr, left, mid - 1)
    else:
        return [[]]



#3 No tests are needed. Fix the code. 

# Question 3.1
def fix_1(lst1, lst2):
    """
    Divide all of the elements in `lst1` by each element in `lst2`
    and return the values in a list.

    >>> fix_1([1, 2, 3], [0, 1])
    [1.0, 2.0, 3.0]
    >>> fix_1([], [])
    []
    >>> fix_1([10, 20, 30], [0, 10, 10, 0])
    [1.0, 2.0, 3.0, 1.0, 2.0, 3.0]
    """
    out = []
    for div in lst2:
        for num in lst1:
            try:
                out.append(num / div)  # add try-except block
            except ZeroDivisionError:
                pass
    return out


# Question 3.2
def fix_2(*filepaths):
    """
    Open all of the files in `filepaths` and PRINT a string for each file
    that indicates if this file can be opened or not.

    >>> fix_2('files/a.txt', 'files/b.txt', 'files/c.txt')
    files/a.txt opened
    files/b.txt not found
    files/c.txt not found

    >>> fix_2('docs.txt')
    docs.txt not found
    """
    for filepath in filepaths:
        try:
            cur_file = open(filepath, "r")
            print(filepath + ' opened')
            cur_file.close()
        except FileNotFoundError:
            print(filepath + ' not found')


# Question 3.3
def fix_3(lst):
    """
    For each element in `lst`, add it with its following element
    in the list. Returns all of the summed values in a list.

    >>> fix_3([1, '1', 2, None])
    <class 'TypeError'>
    <class 'TypeError'>
    <class 'TypeError'>
    <class 'IndexError'>
    []

    >>> fix_3([1, 2, 3, 4])
    <class 'IndexError'>
    [3, 5, 7]

    >>> fix_3([])
    []
    """
    sum_of_pairs = []
    for i, _ in enumerate(lst):
        try:
            sum_of_pairs.append(lst[i] + lst[i + 1])
        except TypeError as error:
            print(type(error))
        except IndexError as error:
            print(type(error))
    return sum_of_pairs





# Question 4
def check_inputs(input1, input2):
    """
    # TODO: Add method description and at least 3 new doctests #

    >>> check_inputs([1, 2.0, 3.0, 4], 4)
    'Input validated'

    >>> check_inputs([], 1)
    Traceback (most recent call last):
    ...
    TypeError: input2 not in input1

    >>> check_inputs(1, 1)
    Traceback (most recent call last):
    ...
    TypeError: input1 is not the correct type

    >>> check_inputs([1, 2, 'hi'], 4)
    Traceback (most recent call last):
    ...
    TypeError: The element at index 2 is not numeric

    >>> check_inputs([1.0, 2.0, 3.0], 'hello')
    Traceback (most recent call last):
    ...
    TypeError: input2 is not the correct type
    """
    
    # Your code is here


# Question 5
def load_file(filename):
    """
    # TODO: Add method description and at least 3 new doctests #

    >>> load_file(1)
    Traceback (most recent call last):
    ...
    TypeError: filename is not a string

    >>> load_file('files/ten_words.txt')
    10

    >>> load_file('files/empty.txt')
    Traceback (most recent call last):
    ...
    ValueError: File is empty

    >>> load_file('files/nonexistant.txt')
    Traceback (most recent call last):
    ...
    FileNotFoundError: files/nonexistant.txt does not exist
    """
    
    # Your code is here








