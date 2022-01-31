"""
DSC 20 Homework 04
Name: William Trang
PID: A16679845
"""
from math import log
# Question 1.1
def contract_list(filepath):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################
    >>> contract_list('files/contracts1.txt')
    ['Theo Hui, 19', 'Ben Ly, 20', 'Nathan Buenviaje, 23']
    >>> contract_list('files/contracts2.txt')
    ['Luke Pacetti, 17', 'Jonah Garcia, 16', 'Brandon Olander, 20', 'Ed Cloyd, 400']
    >>> contract_list('files/contracts3.txt')
    ['Stewie Lewis, 22', 'Sarah Culbertson, 19', 'Kim Lam, 21']

    # My doctests #

    """
    names = []
    with open(filepath, 'r') as f:
        for line in f:
            names.append(line.strip())
    return names

# Question 1.2
def registration(names, veterans):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> registration(['Theo, 19', 'Ben, 20', 'Nathan, 23'], \
['Ben, 20', 'Colby, 18'])
    ['Theo, 19']
    >>> registration(['Michelle, 17', 'Jonah, 16', \
'Brandon, 20', 'Ed, 40'], [])
    ['Michelle, 17', 'Jonah, 16', 'Brandon, 20']
    >>> registration([], ['Stewie, 22', 'Sarah, 19', 'Kim, 21'])
    []

    # Add at least 3 doctests below here #
    """
    assert isinstance(names, list)
    assert isinstance(veterans, list)
    assert all([isinstance(i, str) for i in names])
    assert all([isinstance(i, str) for i in veterans])
    max_age = 22
    return list(filter(lambda player: True if player not in veterans and int(player.split(', ')[1]) < max_age else False, names))

# Question 2
# Part 1 
def generate_labels_review(band_info):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################
    >>> generate_labels_review([('Ben Chen', 2016, 18, 'Flute'), \
('Theo Hui', 2021, 32, 'Mallet')])
    {'Ben Chen': 'ben18chen16flute', 'Theo Hui': 'theo32hui21mallet'}
    >>> generate_labels_review([])
    {}
    >>> generate_labels_review([('Linh Truong', 2077, 42, 'trombone'), \
('Gwen Am', 2006, 69, 'Trombone'), ('Brandon brandon', 1996, 0, 'Bass')])
    {'Gwen Am': 'gwen69am06trombone', 'Brandon brandon': 'bran0brandon96bass'}

    # Add at least 3 doctests below here #
    """
    # YOUR CODE GOES HERE #
    return

# Question 2
# Part 2
def generate_labels(band_info):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################
    >>> generate_labels([('Ben Chen', 2016, 18, 'Flute'), \
('Theo Hui', 2021, 32, 'Mallet')])
    {'Ben Chen': 'ben18chen16flute', 'Theo Hui': 'theo32hui21mallet'}
    >>> generate_labels([])
    {}
    >>> generate_labels([('Linh Truong', 2077, 42, 'trombone'), \
('Gwen Am', 2006, 69, 'Trombone'), ('Brandon brandon', 1996, 0, 'Bass')])
    {'Gwen Am': 'gwen69am06trombone', 'Brandon brandon': 'bran0brandon96bass'}

    # Add at least 3 doctests below here #
    """
    # YOUR CODE GOES HERE #
    return

# Question 3
def find_bands(bands, target_avg, target_range, min_shows):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################
    >>> DCI = {'Blue Devils': [98.2, 97.1, 99.1, 97.3, 98.2], \
        'Blue Coats': [98, 96.5, 97.2, 93, 92.1, 92, 97.4], \
        'Carolina Crown': [75.7, 82.8, 86.1, 98.2], \
        'The Cadets': [96.1, 93.4, 81, 78, 57.9, 86, 71.2, 35.5], \
        'Mandarins': [89.3, 88.1, 85.6, 83.8, 79.1, 88.4, 75.7], \
        'Little Rocks':[42], \
        'Logan Colts':[98.2, 84.4, 69.2, 42, 84]}

    >>> find_bands(DCI, (0, 10), 30, 2)
    []
    >>> find_bands(DCI, (90, 5), 5, 7)
    ['Mandarins']
    >>> find_bands(DCI, (70, 8), 10, 5)
    ['The Cadets', 'Logan Colts']
    >>> find_bands(DCI, (95, 3), 5, 4)
    ['Blue Devils', 'Blue Coats', 'The Cadets']
    """
    # YOUR CODE GOES HERE #
    return
