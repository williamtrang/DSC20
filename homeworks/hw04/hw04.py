"""
DSC 20 Homework 04
Name: William Trang
PID: A16679845
"""

# Question 1.1
def contract_list(filepath):
    """
    Reads a file with given filepath with names and age
    and returns a list of strings containing the
    information in the file with each string containing
    the person's name and age.

    Parameters:
        filepath: Path to file containing names and ages.
    Returns:
        List of compiled names and ages.


    >>> contract_list('files/contracts1.txt')
    ['Theo Hui, 19', 'Ben Ly, 20', 'Nathan Buenviaje, 23']
    >>> contract_list('files/contracts2.txt')
    ['Luke Pacetti, 17', 'Jonah Garcia, 16', 'Brandon Olander, 20', 'Ed Cloyd, 400']
    >>> contract_list('files/contracts3.txt')
    ['Stewie Lewis, 22', 'Sarah Culbertson, 19', 'Kim Lam, 21']

    # My doctests #
    >>> contract_list('files/contracts4.txt')
    ['William, 20', 'Marina, 18', 'Barack Obama, 124']

    >>> contract_list('files/contracts5.txt')
    ['a, 14']

    >>> contract_list('files/contracts6.txt')
    ["'william', 20", '!"#, 18', '14, 20']
    """
    names = []
    with open(filepath, 'r') as f:
        for line in f:
            names.append(line.strip())
    return names

# Question 1.2
def registration(names, veterans):
    """
    Takes in a list of strings with each string containing
    a name and age and a list of veteran players and
    returns the players who are not veterans and are under
    22 years old.

    Parameters:
        names: List containing names and ages of players.
        veterans: List of veteran players.
    Returns:
        List of players who fit the age requirement and
        are not veterans.

    >>> registration(['Theo, 19', 'Ben, 20', 'Nathan, 23'], \
['Ben, 20', 'Colby, 18'])
    ['Theo, 19']
    >>> registration(['Michelle, 17', 'Jonah, 16', \
'Brandon, 20', 'Ed, 40'], [])
    ['Michelle, 17', 'Jonah, 16', 'Brandon, 20']
    >>> registration([], ['Stewie, 22', 'Sarah, 19', 'Kim, 21'])
    []

    # Add at least 3 doctests below here #
    >>> contracts1 = contract_list('files/contracts1.txt')
    >>> registration(contracts1, [])
    ['Theo Hui, 19', 'Ben Ly, 20']

    >>> registration([14, 20], [])
    Traceback (most recent call last):
    ...
    AssertionError

    >>> registration(['William, abc', 'Sharon, 14'], [])
    Traceback (most recent call last):
    ...
    AssertionError

    >>> registration('abra', 'pokeon')
    Traceback (most recent call last):
    ...
    AssertionError

    >>> registration(['William, -14'], [])
    Traceback (most recent call last):
    ...
    AssertionError
    """
    assert isinstance(names, list)
    assert isinstance(veterans, list)
    assert all([isinstance(i, str) for i in names])
    assert all([isinstance(i, str) for i in veterans])
    assert all([i.split(', ')[1].isdigit() for i in names])
    assert all([int(i.split(', ')[1]) > 0 for i in names])

    max_age = 22
    age_index = 1

    return list(filter(lambda player: True if player not in veterans and \
        int(player.split(', ')[age_index]) < max_age else False, names))

# Question 2
# Part 1
def generate_labels_review(band_info):
    """
    Takes in a list of tuples of four values containing name,
    starting year, dot number, and instrument. Generates a label
    based on these values and returns a dictionary with keys
    being a person's name and the values being the generated label.
    Dictionary is generated with dictionary comprehension.

    Parameters:
        band_info: List of tuples containing the player's information.
    Returns:
        Dictionary with player names as keys and generated labels as
        values.

    >>> generate_labels_review([('Ben Chen', 2016, 18, 'Flute'), \
('Theo Hui', 2021, 32, 'Mallet')])
    {'Ben Chen': 'ben18chen16flute', 'Theo Hui': 'theo32hui21mallet'}
    >>> generate_labels_review([])
    {}
    >>> generate_labels_review([('Linh Truong', 2077, 42, 'trombone'), \
('Gwen Am', 2006, 69, 'Trombone'), ('Brandon brandon', 1996, 0, 'Bass')])
    {'Gwen Am': 'gwen69am06trombone', 'Brandon brandon': 'bran0brandon96bass'}

    # Add at least 3 doctests below here #
    >>> generate_labels_review([('William Trang', 2020, 17, 'violin')])
    {'William Trang': 'will17trang20violin'}

    >>> generate_labels_review(2348)
    Traceback (most recent call last):
    ...
    AssertionError

    >>> generate_labels_review(['china', 'usa'])
    Traceback (most recent call last):
    ...
    AssertionError

    >>> generate_labels_review([('William', 2020, '1A', 'violin')])
    Traceback (most recent call last):
    ...
    AssertionError

    >>> generate_labels_review([('William Trang', 2020, 17, 'violin'), \
('Keith Kwong', 2032, 18, 'piano')])
    {'William Trang': 'will17trang20violin'}
    """
    assert isinstance(band_info, list)
    assert all([isinstance(i, tuple) for i in band_info])

    name_index = 0
    year_index = 1
    dot_index = 2
    instr_index = 3
    first_name = 0
    last_name = 1
    name_trunc = 4
    year_trunc = 2
    year_threshold = 2022
    info_len = 4

    assert all([len(i) == info_len for i in band_info])
    assert all([isinstance(i[name_index], str) for i in band_info])
    assert all([isinstance(i[year_index], int) for i in band_info])
    assert all([isinstance(i[dot_index], int) for i in band_info])
    assert all([isinstance(i[instr_index], str) for i in band_info])
    assert all([i[year_index] > 0 for i in band_info])

    return {i[name_index]: \
            (i[name_index].split(' ')[first_name][:name_trunc] + \
            str(i[dot_index]) + i[name_index].split(' ')[last_name] + \
            str(i[year_index])[int(len(str(i[year_index]))) - year_trunc:] + \
            i[instr_index]).lower() for i in band_info \
            if i[year_index] < year_threshold}

# Question 2
# Part 2
def generate_labels(band_info):
    """
    Takes in a list of tuples of four values containing name,
    starting year, dot number, and instrument. Generates a label
    based on these values and returns a dictionary with keys
    being a person's name and the values being the generated label.
    Dictionary is generated by zipping together tuples generated
    by map(), filter(), and lambda functions.

    Parameters:
        band_info: List of tuples containing the player's information.
    Returns:
        Dictionary with player names as keys and generated labels as
        values.

    >>> generate_labels([('Ben Chen', 2016, 18, 'Flute'), \
('Theo Hui', 2021, 32, 'Mallet')])
    {'Ben Chen': 'ben18chen16flute', 'Theo Hui': 'theo32hui21mallet'}
    >>> generate_labels([])
    {}
    >>> generate_labels([('Linh Truong', 2077, 42, 'trombone'), \
('Gwen Am', 2006, 69, 'Trombone'), ('Brandon brandon', 1996, 0, 'Bass')])
    {'Gwen Am': 'gwen69am06trombone', 'Brandon brandon': 'bran0brandon96bass'}

    # Add at least 3 doctests below here #
    >>> generate_labels([('William Trang', 2020, 17, 'violin')])
    {'William Trang': 'will17trang20violin'}

    >>> generate_labels(2348)
    Traceback (most recent call last):
    ...
    AssertionError

    >>> generate_labels(['china', 'usa'])
    Traceback (most recent call last):
    ...
    AssertionError

    >>> generate_labels([('William', 2020, '1A', 'violin')])
    Traceback (most recent call last):
    ...
    AssertionError

    >>> generate_labels([('William Trang', 2020, 17, 'violin'), \
('Keith Kwong', 2032, 18, 'piano')])
    {'William Trang': 'will17trang20violin'}

    >>> generate_labels([('William Trang', 18, 20)])
    Traceback (most recent call last):
    ...
    AssertionError

    >>> generate_labels(['William Trang', '20', 17, 'violin'])
    Traceback (most recent call last):
    ...
    AssertionError

    >>> generate_labels([('William Trang', -4, 17, 'violin')])
    Traceback (most recent call last):
    ...
    AssertionError
    """
    assert isinstance(band_info, list)
    assert all([isinstance(i, tuple) for i in band_info])

    name_index = 0
    year_index = 1
    dot_index = 2
    instr_index = 3
    first_name = 0
    last_name = 1
    name_trunc = 4
    year_trunc = 2
    year_threshold = 2022
    info_len = 4

    assert all([len(i) == info_len for i in band_info])
    assert all([isinstance(i[name_index], str) for i in band_info])
    assert all([isinstance(i[year_index], int) for i in band_info])
    assert all([isinstance(i[dot_index], int) for i in band_info])
    assert all([isinstance(i[instr_index], str) for i in band_info])
    assert all([i[year_index] > 0 for i in band_info])

    trunc_name = lambda name: name[:name_trunc]
    trunc_year = lambda year: str(year)[int(len(str(year))) - year_trunc:]

    gen_label = lambda info: \
        (trunc_name(info[name_index].split(' ')[first_name]) + \
        str(info[dot_index]) + info[name_index].split(' ')[last_name] + \
            trunc_year(info[year_index]) + info[instr_index]).lower()

    filtered_info = list(filter(lambda info: info[year_index] \
        < year_threshold, band_info))

    return dict(zip(tuple(map(lambda info: info[name_index], filtered_info)), \
        tuple(map(gen_label, filtered_info))))

# Question 3
def find_bands(bands, target_avg, target_range, min_shows):
    """
    Searches dictionary of bands with band name as keys and
    competition scores as values for bands that are within the
    range of the target average and have performed the minimum
    number of shows. Returns a list of bands that meet the search
    criteria.

    Parameters:
        bands: Dictionary with band name as keys and scores as values.
        target_avg: Tuple containing the average to look for and the
        amount of scores to look at.
        target_range: Range to look away from the target average.
        min_shows: Minimum number of shows to be eligible.
    Returns:
        List of bands that meet the search criteria.

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

    # My doctests
    >>> find_bands(DCI, (42, 10), 1, 1)
    ['Little Rocks']

    >>> find_bands(DCI, (87, 10), 5, 5)
    ['Mandarins']

    >>> DCI2 = {'UCSD': [100, 99, 100, 100, 100, 100], \
        'UCLA': [50, 49, 100, 100, 100], \
        'UCD': [90, 90, 87, 45, 79]}
    >>> find_bands(DCI2, (95, 3), 5, 4)
    ['UCSD']
    >>> find_bands(DCI2, (75, 5), 10, 4)
    ['UCLA', 'UCD']
    """
    search_range = [target_avg[0] - target_range, target_avg[0] + target_range]
    lower_bound = search_range[0]
    upper_bound = search_range[1]
    noted_scores = target_avg[1]
    score_index = 1

    in_range = lambda avg: (avg >= lower_bound and avg <= upper_bound)
    score_avg = lambda scores, kept_scores: sum(scores) / len(scores) \
        if len(scores) <= kept_scores \
        else sum(scores[0:kept_scores]) / kept_scores

    return list(map(lambda name: name[0], \
            list(filter(lambda band: \
            in_range(score_avg(band[score_index], noted_scores)), \
            filter(lambda band: True if len(band[score_index]) >= min_shows \
            else False, list(bands.items()))))))
