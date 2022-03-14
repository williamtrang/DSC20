def code(*args):
    """
    >>> code()
    []

    >>> code([1,2,3])
    [[1], [2], [3]]

    >>> code(['1', '2', '3'])
    [[1], [2], [3]]

    >>> code((1, 2, 3), ('1', '2', '3', '4'))
    [[2], [4], [6]]
    """
    output = []
    if len(args) == 0:
        return []
    elif len(args) == 1:
        for i in args:
            return [[int(j)] for j in i]
    elif len(args) == 2:
        for i in range(len(args[0])):
            output.append([int(args[0][i]) + int(args[1][i])])
    return output
