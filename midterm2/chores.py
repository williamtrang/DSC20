def chores(*complete, **named):
    """
    >>> chores('A', 'C', A=2, B=5, C = 4, D = 4)
    'Can finish'
    """
    hours = 0
    for keys, values, in named.items():
        if keys in complete:
            hours += values
    if hours <= 10:
        return 'Can finish'
    else:
        return 'Can\'t'