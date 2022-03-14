def stats(file_name):
    """
    >>> stats('stats.txt')
    {'Monday': [70, 90], 'Wednesday': [46], 'Friday': [10, 44]}
    """
    line_split = ''
    dct = {}
    with open(file_name, 'r') as f:
        for line in f:
            line_split = line.split(',')
            if line_split[0] not in dct:
                dct[line_split[0]] = []
            dct[line_split[0]].append(int(line_split[2]))
    return dct