def lowest_dropped(grades):
    """
    >>> g = ((30, 70, 80), (70, 30), (10, 80, 30))
    >>> lowest_dropped(g)
    """
    return [list(i).remove(min(i)) for i in grades]