def create_nickname(team, word):
    gen_nickname = lambda string: string[::-1] + word
    return tuple(map(gen_nickname, team))