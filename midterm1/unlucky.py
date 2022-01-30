def unlucky(team, unlucky_list):
    return list(filter(lambda nickname: False if nickname in unlucky_list else True, team))