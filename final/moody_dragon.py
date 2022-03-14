def moody_dragon(stats, categories):
    return list(map(lambda x: x[0], list(filter(lambda x: x[1] in categories['Positive'], stats))))