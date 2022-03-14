def possible_names(*names, last_name = 'Elizabeth'):
    """
    >>> possible_names('Cindy', 'Lucy', last_name = 'F')
    {'baby1': 'Cindy F', 'baby2': 'Lucy F'}

    >>> possible_names('Cindy', 'Lucy')
    {'baby1': 'Cindy Elizabeth', 'baby2': 'Lucy Elizabeth'}
    """
    name = enumerate(names)
    dct = {}
    for i in name:
        dct['baby' + str(i[0] + 1)] = i[1] + ' ' + last_name
    return dct