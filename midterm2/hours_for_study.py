def hours_for_study(*chores):
    """
    >>> hours_for_study(('A', 5))
    12

    >>> hours_for_study()
    17

    >>> hours_for_study(('A', 6), ('B', 4))
    7

    >>> hours_for_study(('B', 20))
    0
    """
    
    chore_hours = 0
    total_hours = 17
    for arg in chores:
        chore_hours += arg[1]
    total_hours -= chore_hours
    if total_hours <= 0:
        return 0
    return total_hours
