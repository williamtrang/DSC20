def registration(father, gender):
    """
    >>> f = registration('Donkey', 'F')
    >>> f("coco")
    'coco-Elizabeth Donkey'

    >>> f = registration('Donkey', 'm')
    >>> f('Will')
    'Will Donkey'
    """
    def inner(name):
        if gender.lower() == 'f':
            return name + '-Elizabeth ' + father
        return name + ' ' + father
    return inner