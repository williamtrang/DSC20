def file_for_dragon(problems, preference):
    """
    >>> problems = [('p1', 'school'), ('p2', 'rec'), ('p3', 'rec')]
    >>> file_for_dragon(problems, 'rec')
    """
    kept = []
    for i in problems:
        if i[1] == preference:
            kept.append(i[0])
    with open('ProblemsToSolve.txt', 'w') as f:
        for i in kept:
            f.write(i + '\n')
