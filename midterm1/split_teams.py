def split_teams(people):
    return [people[i] for i in range(len(people)) if i % 2 == 0], [people[i] for i in range(len(people)) if i % 2 == 1]