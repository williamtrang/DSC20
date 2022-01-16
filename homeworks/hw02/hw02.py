"""
DSC 20 Homework 02
Name: TODO
PID: TODO
"""

# Question 1
def playlist_password(playlist_name, limit):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> playlist_password("World's Best Lasagne", 10)
    'eBsd7rwost'
    >>> playlist_password('Baked Casserole', 12)
    'oraCdaBkesse'
    >>> playlist_password('Hash browns', 11)
    'orb4s4awns'

    # Add at least 3 doctests below here #

    """
    # YOUR CODE GOES HERE #
    return

# Question 2
def cookable_recipes(ings, recipes):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> rec = {'Egg Fried Rice': ['egg', 'rice', 'msg'], \
'Spaghetti': ['noodle', 'tomato sauce'], 'Steamed Rice': ['rice']}
    >>> cookable_recipes(['egg', 'msg', 'rice'], rec)
    ['Egg Fried Rice', 'Steamed Rice']
    >>> cookable_recipes(['egg', 'rice', 'msg', 'noodle', 'tomato sauce'], rec)
    ['Egg Fried Rice', 'Spaghetti', 'Steamed Rice']
    >>> cookable_recipes(['egg'], rec)
    []

    # Add at least 3 doctests below here #

    """
    # YOUR CODE GOES HERE #
    return

# Question 3
# Part 1
def process_purchase(purchase):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> process_purchase([('rice', 'mitsuwa'), ('msg', '99ranch'), \
('eggs', 'costco')])
    {'mitsuwa': ['rice'], '99ranch': ['msg'], 'costco': ['eggs']}
    >>> process_purchase([('milk', 'ralphs'), ('carrot', 'ralphs'), \
('milk', 'ralphs'), ('carrot', 'costco')])
    {'ralphs': ['milk', 'carrot', 'milk'], 'costco': ['carrot']}

    # Add at least 3 doctests below here #

    """
    # YOUR CODE GOES HERE #
    return

# Part 2
def grocery_summary(grocery_purchases):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> p1 = [{'mitsuwa': ['rice'], '99ranch': ['msg']}, \
{'99ranch': ['sambal', 'banana leaf'], 'costco': ['eggs']}]
    >>> grocery_summary(p1)
    {'mitsuwa': ['rice'], '99ranch': ['msg', 'sambal', 'banana leaf'], \
'costco': ['eggs']}
    >>> p2 = [{'ralphs': ['milk', 'carrot', 'milk'], 'costco': ['carrot']}, \
{'ralphs': ['carrot', 'carrot', 'milk'], 'costco': ['carrot']}]
    >>> grocery_summary(p2)
    {'ralphs': ['milk', 'carrot'], 'costco': ['carrot']}

    # Add at least 3 doctests below here #

    """
    # YOUR CODE GOES HERE #
    return

# Question 4
def channel_stats(videos_stats):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> channel_stats ([[123, 231, 82, 430], [340, 158, 225, 647]])
    [('likes', 463), ('dislikes', 389), ('comments', 307), ('views', 1077)]
    >>> channel_stats([[865, 342, 205, 230]])
    [('likes', 865), ('dislikes', 342), ('comments', 205), ('views', 230)]
    >>> channel_stats([[954, 234, 235, 2035], [1040, 350, 394, 2500], \
[70, 43, 23, 230]])
    [('likes', 2064), ('dislikes', 627), ('comments', 652), ('views', 4765)]

    # Add at least 3 doctests below here #
    """
    # YOUR CODE GOES HERE #
    return

# Question 5
# Part 1
def parse_file(filepath):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> parse_file('files/viewer1.txt')
    {('marina', 1): [15, 10], ('elvy', 2): [8]}
    >>> parse_file('files/viewer2.txt')
    {('marina', 10): [65, 20], ('elvy', 4): [10, 60, 30], ('colin', 6): [90]}
    >>> parse_file('files/empty.txt')
    {}

    # Add at least 3 doctests below here #

    """
    # YOUR CODE GOES HERE #
    return

# Part 2
def long_views(filepath, threshold):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> long_views('files/viewer1.txt', 10)
    >>> with open('files/viewer1_modified.txt', 'r') as outfile1:
    ...     print(outfile1.read().strip())
    1,Yes
    2,No
    1,Yes

    >>> long_views('files/viewer2.txt', 40)
    >>> with open('files/viewer2_modified.txt', 'r') as outfile2:
    ...     print(outfile2.read().strip())
    10,Yes
    4,No
    4,Yes
    10,No
    6,Yes
    4,No

    # Add at least 3 doctests below here #

    """
    # YOUR CODE GOES HERE #
    return

# Part 3
def compare_subscribe(data, subscriber):
    """
    ##############################################################
    # TODO: Replace this block of comments with your own         #
    # method description and add at least 3 more doctests below. #
    ##############################################################

    >>> data = parse_file('files/viewer1.txt')
    >>> compare_subscribe(data, ['marina'])
    (12, 8)
    >>> compare_subscribe(data, ['marina', 'elvy'])
    (11, 0)
    >>> compare_subscribe(data, [])
    (0, 11)

    # Add at least 3 doctests below here #

    """
    # YOUR CODE GOES HERE #
    return
