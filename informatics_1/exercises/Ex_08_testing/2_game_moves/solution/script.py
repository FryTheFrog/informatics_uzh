#!/usr/bin/env python3
# Sample Solution
def move(state, direction):

    if type(state) != tuple:
        raise UserWarning("@@A test provides a non-tuple as first argument. The resulting behavior is undefined.@@")

    if len(state) and not (type(state[0]) == str):
        raise UserWarning("@@A test uses a tuple with non-string elements as first argument. The resulting behavior is undefined.@@")

    assert_valid(state)

    # create list as mutable version of game state
    state = list(state)

    xy_from = find_player(state)
    possible_moves = get_possible_moves(state, xy_from)

    # Ensure that moves are possible and that the request move is among them
    if not possible_moves.keys() or direction not in possible_moves.keys():
        raise Warning()

    xy_to = possible_moves[direction]
    set_location(state, xy_from, " ")
    set_location(state, xy_to, "o")

    # identify possible moves in new game state
    possible_next_moves = get_possible_moves(state, xy_to)
    possible_next_moves = sorted(possible_next_moves.keys())

    # return an immutable version of the game state
    return (
        tuple(state),
        tuple(possible_next_moves)
    )


def assert_valid(state):
    # ensure valid characters
    for c in "".join(state):
        if c not in " o#":
            raise Warning()

    # ensure world is not empty
    if not state or not state[0]:
        raise Warning()

    # ensure that all rows have same length
    expected_len = len(state[0])
    for row in state:
        if len(row) != expected_len:
            raise Warning()

    # ensure exactly one player exists
    if state and state[0] and "".join(state).count("o") != 1:
        raise Warning()


def set_location(state, xy, c):
    x,y = xy
    state[y] = state[y][:x] + c + state[y][x+1:]


def get_possible_moves(state, xy):
    possible_moves = {}
    if is_in_game_and_free(up(xy), state):
        possible_moves["up"] = up(xy)
    if is_in_game_and_free(right(xy), state):
        possible_moves["right"] = right(xy)
    if is_in_game_and_free(down(xy), state):
        possible_moves["down"] = down(xy)
    if is_in_game_and_free(left(xy), state):
        possible_moves["left"] = left(xy)
    return possible_moves


def is_in_game_and_free(xy, state):
    x, y = xy

    y_min = 0
    y_max = len(state)- 1
    if y < y_min or y > y_max:
        return False

    x_min = 0
    x_max = len(state[y])-1
    if x < x_min or x > x_max:
        return False

    # please note that the first dimension contains the rows, i.e., is y
    return state[y][x] == " "


def find_player(state):
    for y, row in enumerate(state):
        for x, c in enumerate(row):
            if c == 'o':
                return x, y


def up(xy): return xy[0], xy[1]-1
def right(xy): return xy[0]+1, xy[1]
def down(xy): return xy[0], xy[1]+1
def left(xy): return xy[0]-1, xy[1]
