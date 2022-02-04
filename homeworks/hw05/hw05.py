"""
DSC20 WI22 HW05
Name: TODO
PID:  TODO
"""

# begin helper methods
def ceil(x):
    """
    Simulation to math.ceil
    No doctest needed
    """
    if int(x) != x:
        return int(x) + 1
    return int(x)

def log(x):
    """
    Simulation to math.log with base e
    No doctests needed
    """
    n = 1e10
    return n * ((x ** (1/n)) - 1)
# end helper methods

# Question1
def db_calc(dynamic, inst_mult):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################
    >>> snare_1 = db_calc('ff',  1.2)
    >>> snare_1(0)
    126.0
    >>> snare_1(10)
    80
    >>> snare_1(50)
    48
    >>> db_calc('loud', 1)(35)
    Traceback (most recent call last):
    ...
    AssertionError
    >>> db_calc('pp', 1.200001)(50)
    Traceback (most recent call last):
    ...
    AssertionError

    # Add AT LEAST 3 doctests below, DO NOT delete this line
    """
    # Your code starts here
    return


# Question2
def next_move(file_names, decision):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################
    >>> message_to_students = next_move("files/names.txt", "h")
    >>> mess = message_to_students("Never give up!")
    >>> print(mess)
    Dear I!
    Unfortunately, it is time to go home. Never give up!
    >>> message_to_students = next_move("files/names.txt", "s")
    >>> mess = message_to_students("San Diego, Earth.")
    >>> print(mess)
    Dear A, C, E, G, K!
    We are happy to announce that you can move to the next round.
    It will be held at San Diego, Earth.

    # Add AT LEAST 3 doctests below, DO NOT delete this line
    """
    # Your code starts here
    return

# Question3
def forge(filepath):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################
	>>> forge('files/vote1.txt')(0)
    >>> with open('files/vote1.txt', 'r') as outfile1:
    ...     print(outfile1.read().strip())
    Jerry,0
    Larry,0
    Colin,0
    Scott,0
    Jianming,0
    Huaning,1
    Amy,1
    Elvy,1
    >>> forge('files/vote2.txt')(0)
    >>> with open('files/vote2.txt', 'r') as outfile2:
    ...     print(outfile2.read().strip())
    Jerry,0
    Larry,0
    Colin,0
    Scott,1
    Jianming,0
    Huaning,1
    Amy,1
    Elvy,0
    >>> forge('files/vote3.txt')(1)
    >>> with open('files/vote3.txt', 'r') as outfile3:
    ...     print(outfile3.read().strip())
    Jerry,1
    Larry,1
    Colin,1
    Scott,0

    # Add AT LEAST 3 doctests below, DO NOT delete this line
    """
    # Your code starts here
    return

# Question4.1
def number_of_adults_1(lst, age = 18):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################
    >>> number_of_adults_1([1,2,3,4,5,6,7])
    3
    >>> number_of_adults_1([1,2,3,4,5,6,7], 5)
    2
    >>> number_of_adults_1([1,2,3,4,5,6,7], age = 2)
    1
    
    # Add AT LEAST 3 doctests below, DO NOT delete this line
    """
    # Your code starts here
    return

# Question4.2
def number_of_adults_2(*args):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################
    >>> number_of_adults_2(1,2,3,4,5,6,7)
    3
    >>> number_of_adults_2(10,20,13,4)
    1
    >>> number_of_adults_2(19, 20)
    0

    # Add AT LEAST 3 doctests below, DO NOT delete this line
    """
    # Your code starts here
    return

# Question4.3
def number_of_adults_3(*args, age = 18):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################
    >>> number_of_adults_3(1,2,3,4,5,6,7)
    3
    >>> number_of_adults_3(1,2,3,4,5,6,7, age = 5)
    2
    >>> number_of_adults_3(1,2,3,4,5,6,7, age = 2)
    1

    # Add AT LEAST 3 doctests below, DO NOT delete this line
    """
    # Your code starts here
    return

# Question5
def school_trip(age_limit, **kwargs):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################
    >>> school_trip(14, class1=[1,2,3], class2 =[4,5,6,7], class3=[15,16])
    {'class1': 1, 'class2': 2, 'class3': 0}
    >>> school_trip(14, class1=[21,3], class2 =[41,1,2,24,6], class3=[30,3,1,7,88])
    {'class1': 1, 'class2': 1, 'class3': 1}
    >>> school_trip(100, class1=[21,3], class2 =[41,1000,2,24,6], class3=[3,1,7,88])
    {'class1': 1, 'class2': 2, 'class3': 2}

    # Add AT LEAST 3 doctests below, DO NOT delete this line
    """
    # Your code starts here
    return

# Question6
def rearrange_args(*args, **kwargs):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################
    >>> rearrange_args(10, False, player1=[25, 30], player2=[5, 50])
    [('positional_0', 10), ('positional_1', False), \
('keyword_0_player1', [25, 30]), ('keyword_1_player2', [5, 50])]
    >>> rearrange_args('L', 'A', 'N', 'G', L='O', I='S')
    [('positional_0', 'L'), ('positional_1', 'A'), ('positional_2', 'N'), \
('positional_3', 'G'), ('keyword_0_L', 'O'), ('keyword_1_I', 'S')]
    >>> rearrange_args(no_positional=True)
    [('keyword_0_no_positional', True)]

    # Add AT LEAST 3 doctests below, DO NOT delete this line
    """
    # Your code starts here
    return
