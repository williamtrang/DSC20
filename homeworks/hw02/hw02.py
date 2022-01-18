"""
DSC 20 Homework 02
Name: William Trang
PID: A16679845
"""

# Question 1
def playlist_password(playlist_name, limit):
    """
    # Takes in a string representing playlist name
    # and an integer character limit. Generates and
    # returns a string by defined rules that has a
    # length less than or equal to the character limit.

    >>> playlist_password("World's Best Lasagne", 10)
    'eBsd7rwost'
    >>> playlist_password('Baked Casserole', 12)
    'oraCdaBkesse'
    >>> playlist_password('Hash browns', 11)
    'orb4s4awns'

    # Add at least 3 doctests below here #
    >>> playlist_password('',  7)
    ''
    >>> playlist_password('HAP"P%Y N#EW Y"EA!!R!L!', 10)
    'EYwA4PPYNE'
    >>> playlist_password('hppy nw yr', 20)
    '4ppynwyr'
    >>> playlist_password('brEkf', 10)
    'Erbkf'
    >>> playlist_password('a', 20)
    'a'
    >>> playlist_password('aEiOuDWIK,,Lh', 20)
    'IwdOEaiuk74'
    """
    password = ''
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    lower_list = ['d', 'w', 'k']

    if len(playlist_name) == 0:
        return ''

    for i in playlist_name:
        if len(password) >= limit:
            return password

        if not i.isalnum():
            continue

        if i.lower() in vowel_list:
            password = (password + i)[::-1]
        elif i.lower() in lower_list:
            password += i.lower()
        elif i.upper() == 'L':
            password += '7'
        elif i.upper() == 'H':
            password += '4'
        else:
            password += i
    return password

# Question 2
def cookable_recipes(ings, recipes):
    """
    # Takes in a list of ingredients and a dictionary
    # of recipes. Returns the recipes that are able to be
    # made. A recipe can be made if all the components
    # are in the ingredients list.

    >>> rec = {'Egg Fried Rice': ['egg', 'rice', 'msg'], \
'Spaghetti': ['noodle', 'tomato sauce'], 'Steamed Rice': ['rice']}
    >>> cookable_recipes(['egg', 'msg', 'rice'], rec)
    ['Egg Fried Rice', 'Steamed Rice']
    >>> cookable_recipes(['egg', 'rice', 'msg', 'noodle', 'tomato sauce'], rec)
    ['Egg Fried Rice', 'Spaghetti', 'Steamed Rice']
    >>> cookable_recipes(['egg'], rec)
    []

    # Add at least 3 doctests below here #
    >>> cookable_recipes(['eggs', 'beef', 'flour'], {'Egg Noodle': \
['egg', 'flour'], 'Beef Noodle': ['eggs', 'beef', 'flour'], \
'Beef Wrap': ['flour', 'beef']})
    ['Beef Noodle', 'Beef Wrap']
    >>> cookable_recipes([], {})
    []
    >>> cookable_recipes(['egg', 'beefs', 'flour'], {'Egg Noodle': \
['egg', 'flour'], 'Beef Noodle': ['eggs', 'beef', 'flour'], \
'Beef Wrap': ['flour', 'beef']})
    ['Egg Noodle']
    """
    possible_recipes = []
    ings_counter = 0
    for keys, values in recipes.items():
        for j in ings:
            if j in values:
                ings_counter += 1
            if ings_counter == len(values):
                possible_recipes.append(keys)
                break
        ings_counter = 0
    return possible_recipes

# Question 3
# Part 1
def process_purchase(purchase):
    """
    # Takes in a list of tuples with two elements. Puts the
    # elements into dictionary by second element with
    # values being the first element and returns.

    >>> process_purchase([('rice', 'mitsuwa'), ('msg', '99ranch'), \
('eggs', 'costco')])
    {'mitsuwa': ['rice'], '99ranch': ['msg'], 'costco': ['eggs']}
    >>> process_purchase([('milk', 'ralphs'), ('carrot', 'ralphs'), \
('milk', 'ralphs'), ('carrot', 'costco')])
    {'ralphs': ['milk', 'carrot', 'milk'], 'costco': ['carrot']}

    # Add at least 3 doctests below here #
    >>> process_purchase([])
    {}
    >>> process_purchase([('rice', 'mitsuwa'), ('eggs', 'mitsuwa'), \
('rice', 'mitsuwa'), ('rice', 'costco')])
    {'mitsuwa': ['rice', 'eggs', 'rice'], 'costco': ['rice']}
    >>> process_purchase([('rice', 'costco'), ('eggs', 'mitsuwa')])
    {'costco': ['rice'], 'mitsuwa': ['eggs']}
    """
    if len(purchase) == 0:
        return {}

    purchase_dict = {}
    store_names = []
    items_purchased = []

    for i in range(0, len(purchase)):
        store_names.append(purchase[i][1])
        purchase_dict[store_names[i]] = []

    for i in range(0, len(purchase)):
        items_purchased.append(purchase[i][0])
        purchase_dict[store_names[i]].append(items_purchased[i])

    return purchase_dict

# Part 2
def grocery_summary(grocery_purchases):
    """
    # Takes in a list of dictionaries sorted as store as
    # keys and items bought as values. Congregates the
    # items bought between the dictionaries and returns
    # the combined dictionary.

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
    >>> grocery_summary([{}])
    {}
    >>> grocery_summary([{'vons': ['egg', 'egg', 'egg', 'eggs']}])
    {'vons': ['egg', 'eggs']}
    >>> grocery_summary([{'vons': ['egg', 'eggs', 'egg'], 'sams':\
        ['eggs', 'peach']}, {'vons': ['flour']}])
    {'vons': ['egg', 'eggs', 'flour'], 'sams': ['eggs', 'peach']}
    """
    if len(grocery_purchases) == 0:
        return {}

    combined_keys = []
    combined_dict = {}
    for i in range(0, len(grocery_purchases)):
        for keys in grocery_purchases[i].keys():
            combined_keys.append(keys)

    for i in range(0, len(combined_keys)):
        combined_dict[combined_keys[i]] = []

    for i in range(0, len(grocery_purchases)):
        for keys, values in grocery_purchases[i].items():
            for j in range(0, len(values)):
                if values[j] not in combined_dict[keys]:
                    combined_dict[keys].append(values[j])
    return combined_dict

# Question 4
def channel_stats(videos_stats):
    """
    # Takes in a list of lists with 4 elements each. Adds up
    # the values with the same index and returns all the
    # summed values.

    >>> channel_stats ([[123, 231, 82, 430], [340, 158, 225, 647]])
    [('likes', 463), ('dislikes', 389), ('comments', 307), ('views', 1077)]
    >>> channel_stats([[865, 342, 205, 230]])
    [('likes', 865), ('dislikes', 342), ('comments', 205), ('views', 230)]
    >>> channel_stats([[954, 234, 235, 2035], [1040, 350, 394, 2500], \
[70, 43, 23, 230]])
    [('likes', 2064), ('dislikes', 627), ('comments', 652), ('views', 4765)]

    # Add at least 3 doctests below here #
    >>> channel_stats([[0, 0, 0, 0], [0, 0, 0, 0]])
    [('likes', 0), ('dislikes', 0), ('comments', 0), ('views', 0)]
    >>> channel_stats([[12, 24, 36, 48], [2, 3, 4, 5], [11, 22, 33, 44]])
    [('likes', 25), ('dislikes', 49), ('comments', 73), ('views', 97)]
    >>> channel_stats([[1, 2, 3, 4], [4, 5, 6, 7]])
    [('likes', 5), ('dislikes', 7), ('comments', 9), ('views', 11)]
    """
    total_likes = 0
    total_dislikes = 0
    total_comments = 0
    total_views = 0

    likes_index = 0
    dislikes_index = 1
    comments_index = 2
    views_index = 3

    for i in range(0, len(videos_stats)):
        total_likes += videos_stats[i][likes_index]
        total_dislikes += videos_stats[i][dislikes_index]
        total_comments += videos_stats[i][comments_index]
        total_views += videos_stats[i][views_index]
    return [('likes', total_likes), ('dislikes', total_dislikes),
            ('comments', total_comments), ('views', total_views)]

# Question 5
# Part 1
def parse_file(filepath):
    """
    # Takes in a file pathway. Reads the designated file with specific
    # formatting for watch time stats and returns a dictionary
    # with the username, user ID, and their video watch times.

    >>> parse_file('files/viewer1.txt')
    {('marina', 1): [15, 10], ('elvy', 2): [8]}
    >>> parse_file('files/viewer2.txt')
    {('marina', 10): [65, 20], ('elvy', 4): [10, 60, 30], ('colin', 6): [90]}
    >>> parse_file('files/empty.txt')
    {}

    # Add at least 3 doctests below here #
    >>> parse_file('files/viewer3.txt')
    {('will', 7): [10, 9, 0]}
    >>> parse_file('files/viewer4.txt')
    {('will', 7): [0, 10, 21], ('zhien', 3): [4, 0]}
    >>> parse_file('files/viewer5.txt')
    {('will', 7): [1, 84], ('zhien', 3): [1], ('toby', 4): [1, 11]}
    """
    viewer_data = ''
    analytics = {}
    with open(filepath, 'r') as file:
        for line in file:
            viewer_data = line.split(',')

            username = viewer_data[0]
            user_id = int(viewer_data[1])
            view_start = int(viewer_data[2])
            view_end = int(viewer_data[3])

            if (username, user_id) not in analytics:
                analytics[(username, user_id)] = []
            analytics[(username, user_id)].append(view_end - view_start)
    return analytics

# Part 2
def long_views(filepath, threshold):
    """
    # Takes in a file pathway and a threshold for watch time.
    # Read the file and determine whether the watch time
    # reached the threshold (watchtime = view_end - view_start).
    # Return the user ID and whether or not the watch time was met.

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
    >>> long_views('files/viewer3.txt', 10)
    >>> with open('files/viewer3_modified.txt', 'r') as outfile3:
    ...     print(outfile3.read().strip())
    7,Yes
    7,No
    7,No
    >>> long_views('files/empty.txt', 40)
    >>> with open('files/empty_modified.txt', 'r') as outfile4:
    ...     print(outfile4.read().strip())
    <BLANKLINE>
    >>> long_views('files/viewer4.txt', 0)
    >>> with open('files/viewer4_modified.txt', 'r') as outfile5:
    ...     print(outfile5.read().strip())
    7,Yes
    7,Yes
    3,Yes
    7,Yes
    3,Yes
    >>> long_views('files/viewer5.txt', 2)
    >>> with open('files/viewer5_modified.txt', 'r') as outfile6:
    ...     print(outfile6.read().strip())
    7,No
    3,No
    4,No
    4,Yes
    7,Yes
    """
    new_filepath = filepath.split('.')[0] + '_modified.txt'
    viewer_data = ''
    watched_enough = ''
    bool_to_yn = {'False': 'No', 'True': 'Yes'}
    with open(filepath, 'r') as file:
        for line in file:
            viewer_data = line.split(',')

            user_id = str(viewer_data[1])
            view_start = int(viewer_data[2])
            view_end = int(viewer_data[3])

            watched_enough += user_id + ',' + \
                bool_to_yn[str((view_end - view_start) >= threshold)] + '\n'
    with open(new_filepath, 'w') as new_file:
        new_file.write(watched_enough)

# Part 3
def compare_subscribe(data, subscriber):
    """
    # Takes in a dictionary with tuple keys containing
    # username and user ID and values denoting watch times
    # as well as a list of strings denoting subscribers.
    # A person is a subscriber if their username is
    # in the subscriber list. Return the average watch
    # time of subscribers and non-subscribers.

    >>> data = parse_file('files/viewer1.txt')
    >>> compare_subscribe(data, ['marina'])
    (12, 8)
    >>> compare_subscribe(data, ['marina', 'elvy'])
    (11, 0)
    >>> compare_subscribe(data, [])
    (0, 11)

    # Add at least 3 doctests below here #
    >>> data2 = parse_file('files/viewer2.txt')
    >>> compare_subscribe(data2, ['marina'])
    (42, 47)
    >>> compare_subscribe(data2, ['marina', 'colin'])
    (58, 33)
    >>> data3 = parse_file('files/viewer3.txt')
    >>> compare_subscribe(data3, [])
    (0, 6)
    """
    all_keys = []
    all_values = []
    subscriber_index = []

    sub_average = 0
    sub_viewcount = 0

    nonsub_average = 0
    nonsub_viewcount = 0

    for keys, values in data.items():
        all_keys.append(keys)
        all_values.append(values)

    for i in range(0, len(all_keys)):
        for j in range(0, len(subscriber)):
            if all_keys[i][0] == subscriber[j]:
                subscriber_index.append(i)

    for i in range(0, len(subscriber_index)):
        for j in range(0, len(all_values[subscriber_index[i]])):
            sub_average += int(all_values[subscriber_index[i]][j])
            sub_viewcount += 1

    for i in range(0, len(all_values)):
        if i not in subscriber_index:
            for j in range(0, len(all_values[i])):
                nonsub_average += int(all_values[i][j])
                nonsub_viewcount += 1
        else:
            continue

    if len(subscriber) != len(all_keys):
        nonsub_average = nonsub_average // nonsub_viewcount

    if len(subscriber) != 0:
        sub_average = sub_average // sub_viewcount
    return (sub_average, nonsub_average)
