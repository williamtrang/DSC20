def best_days(dragon, me):
    """
    >>> d = {'Monday': (1, 6), 'Friday': (3, 5)}
    >>> m = {'Monday': (2, 4), 'Friday': (3, 6)}
    >>> best_days(d, m)
    ['Monday']

    >>> d = {'Monday': (1, 6), 'Friday': (3, 5)}
    >>> m = {'Monday': (0, 4), 'Friday': (3, 6)}
    >>> best_days(d, m)
    []

    >>> d = {'Monday': (1, 6), 'Friday': (3, 6), 'Thursday': (3, 67)}
    >>> m = {'Monday': (2, 4), 'Friday': (3, 6)}
    >>> best_days(d, m)
    ['Monday', 'Friday']
    """
    days = []
    for i in dragon.keys():
        try:
            if (dragon[i][0] <= me[i][0]) and (dragon[i][1] >= me[i][1]):
                days.append(i)
        except KeyError:
            pass
    return days