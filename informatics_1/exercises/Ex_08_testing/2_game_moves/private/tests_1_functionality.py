#!/usr/bin/env python3
import sys
from unittest import TestCase

# catch potential exception from import
exception_import = None
try:
    from public.script import move
except Exception as e:
    exception_import = e

NO_RESULT = None, None
UP, RIGHT, DOWN , LEFT = "up", "right", "down", "left"

class PrivateTestSuite(TestCase):

    def _fail_on_import_problem(self):
        if exception_import:
            m = "@@Import of your implementation failed: {}@@".format(type(exception_import).__name__)
            self.fail(m)

    def _exec(self, state, dir):
        self._fail_on_import_problem()
        try:
            actual = move(state, dir)
        except Exception as exception_run:
            m = "@@Running your implementation on valid input failed unexpectedly ({}).@@".format(type(exception_run).__name__)
            self.fail(m)

        if type(actual) != tuple:
            self.fail("@@Your implementation has incorrect return type, tuple expected.@@")
        if len(actual) != 2:
            self.fail("@@Your returned tuple should always have a size of two.@@")
        if not (type(actual[0]) is tuple):
            self.fail("@@First element of your returned tuple should be a tuple of strings.@@")
        if not (type(actual[1]) is tuple):
            self.fail("@@Second element of your returned tuple should be a tuple of strings.@@")

        return actual

    def _assertFail(self, state, dir, expected_exception_type, m):
        self._fail_on_import_problem()

        try:
            move(state, dir)
        except Exception as actual_exception:
            actual_exception_type = type(actual_exception)
            if expected_exception_type != actual_exception_type:
                m = "@@Wrong exception when running your implementation with hidden test: {} (expected: {}, was: {})@@".format(m, expected_exception_type.__name__, actual_exception_type.__name__)
                self.fail(m)
        else:
            m = "@@Unexpectedly, a hidden test run did not fail with your implementation: {}@@".format(m)
            self.fail(m)

    def _assert(self, state, dir, next_state, next_moves, m):
        actual = self._exec(state, dir)
        expected = (next_state, next_moves)
        self.assertEqual(expected, actual, m)

    def test0_invalid_empty_field0(self):
        self._assertFail((), UP, Warning, "It does not reject an empty world")

    def test0_invalid_empty_field1(self):
        self._assertFail(("",), UP, Warning, "It does not reject a world with an empty row")

    def test0_invalid_empty_field2(self):
        self._assertFail(("", ""), UP, Warning, "It does not reject a world with empty rows")

    def test0_invalid_incorrect_dimensions(self):
        self._assertFail((" ", "o "), UP, Warning, "It does not reject worlds with inconsistent dimensions")

    def test0_invalid_no_player(self):
        self._assertFail(("  ",), RIGHT, Warning, "It does not reject worlds without player")

    def test0_invalid_multiple_players(self):
        self._assertFail(("o o ",), RIGHT, Warning, "It does not reject worlds with multiple players")

    def test0_invalid_invalid_symbols(self):
        self._assertFail(("!o ",), RIGHT, Warning, "It does not reject worlds with invalid symbols")

    def test0_invalid_no_move_possible1(self):
        self._assertFail(("o",), RIGHT, Warning, "It does not reject all worlds in which no move is possible")

    def test0_invalid_no_move_possible2(self):
        self._assertFail((" # ",
                          "#o#",
                          " # "), RIGHT, Warning, "It does not reject all worlds in which no move is possible")

    def test0_invalid_no_move_possible3_rock(self):
        self._assertFail(("#o ",), LEFT, Warning, "It does not reject all invalid moves")

    def test0_invalid_no_move_possible3_oob(self):
        self._assertFail(("o ",), UP, Warning, "It does not reject all invalid moves")

    def test1a_all_directions_are_recognized(self):
        actual = self._exec(("   ",
                             " o ",
                             "   ",
                             "   "), DOWN)
        self.assertTrue(DOWN in actual[1], "@@Your implementation does not detect all possible 'down' moves.@@")
        self.assertTrue(LEFT in actual[1], "@@Your implementation does not detect all possible 'left' moves.@@")
        self.assertTrue(RIGHT in actual[1], "@@Your implementation does not detect all possible 'right' moves.@@")
        self.assertTrue(UP in actual[1], "@@Your implementation does not detect all possible 'up' moves.@@")

    def test1b_move_up(self):
        self._assert((" ",
                      "o"), UP, ("o",
                                 " "),
                     (DOWN,), "@@Moving 'up' does not always work in your implementation.@@")

    def test1c_move_right(self):
        self._assert(("o ",), RIGHT, (" o",), (LEFT,), "@@Moving 'right'' does not always work in your implementation.@@")

    def test1d_move_down(self):
        self._assert(("o",
                      " "), DOWN, (" ",
                                   "o"),
                     (UP,), "@@Moving 'down'' does not always work in your implementation.@@")

    def test1e_move_left(self):
        self._assert((" o",), LEFT, ("o ",), (RIGHT,), "@@Moving 'left'' does not always work in your implementation.@@")

    def test1f_all_directions_are_sorted(self):
        self._assert(("   ",
                      " o ",
                      "   ",
                      "   "), DOWN, ("   ",
                                     "   ",
                                     " o ",
                                     "   "),
                     (DOWN, LEFT, RIGHT, UP), "@@The possible next moves do not seem to be ordered in your implementation.@@")

    def test2_provided_example(self):
        state = (
            "#####   ",
            "###    #",
            "#   o ##",
            "   #####"
        )
        expected = (
            "#####   ",
            "###    #",
            "#    o##",
            "   #####"
        )
        self._assert(state, RIGHT, expected, (LEFT, UP), "@@Example from template does not return correct result in your implementation.@@")

    #### utility functions ###

    def up(self, state=None): return self._move(state, "up")
    def right(self, state=None): return self._move(state, "right")
    def down(self, state=None): return self._move(state, "down")
    def left(self, state=None): return self._move(state, "left")

    def _move(self, state, dir):
        if state is None:
            state = ()
        else:
            state = tuple(state.split("\n"))
        return self._exec(state, dir)
