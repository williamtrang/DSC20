def calories(snacks):
    """
    >>> calories(0)
    0

    >>> calories(1)
    5

    >>> calories(2)
    55

    >>> calories(3)
    60

    >>> calories(4)
    110
    """
    unhealthy = 50
    healthy = 5
    if snacks % 2 == 0 and snacks != 0:
        return calories(snacks - 1) + unhealthy
    elif (snacks % 2 == 1) and snacks != 1:
        return calories(snacks - 1) + healthy
    elif snacks == 1:
        return healthy
    else:
        return 0
