def move(state, direction):
    # validate state (possible moves > 0 and invalid move not included)
    player_count = 0
    for i in state:
        if len(i) < 1:
            raise Warning('invalid dimension')
        if len(i) != len(state[0]):
            raise Warning('length of lines incosistent')
        for char in i:
            if char == 'o': player_count += 1
            elif not char == ' ' and not char == '#':
                raise Warning(f'invalid character: "{char}"')
    if player_count != 1:
        raise Warning(f'invalid amount of players: {player_count}')

    # get position
    def get_position(state):
        for lineidx, i in enumerate(state):
            if 'o' in i:
                cordy = lineidx
                cordx = i.find('o')
        return cordx, cordy

    cordx, cordy = get_position(state)

    # get possibilities
    def get_possibilities(state):
        poss_list = []
        if cordy > 0 and state[cordy - 1][cordx] == ' ':
            poss_list.append('up')
        if cordy + 1 < len(state) and state[cordy + 1][cordx] == ' ':
            poss_list.append('down')
        if cordx > 0 and state[cordy][cordx - 1] == ' ':
            poss_list.append('left')
        if cordx + 1 < len(state[0]) and state[cordy][cordx + 1] == ' ':
            poss_list.append('right')
        poss_list.sort()
        if poss_list == []:
            raise Warning('no possible moves')
        return poss_list
    poss_list = get_possibilities(state)

    # update state
    if not direction in poss_list:
        raise Warning('invalid move')
    state = list(state)
    state[cordy] = state[cordy].split('o')
    state[cordy] = ' '.join(state[cordy])
    if direction == 'up':
        state[cordy - 1] = state[cordy - 1][:cordx] + 'o' + state[cordy - 1][cordx + 1:]
    elif direction == 'down':
        state[cordy + 1] = state[cordy + 1][:cordx] + 'o' + state[cordy + 1][cordx + 1:]
    elif direction == 'left':
        state[cordy] = state[cordy][:cordx - 1] + 'o' + state[cordy][cordx:]
    elif direction == 'right':
        state[cordy] = state[cordy][:cordx + 1] + 'o' + state[cordy][cordx + 2:]

    # get possibilities for new state
    cordx, cordy = get_position(state)
    poss_list = get_possibilities(state)

    return tuple(state), tuple(poss_list)


s1 = (
    "#####   ",
    "###    #",
    "#   o ##",
    "   #####"
)
s2 = move(s1, "up")

print("= New State =")
print("\n".join(s2[0]))
print("\nPossible Moves: {}".format(s2[1]))