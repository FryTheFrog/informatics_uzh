from unittest import TestCase
import sys
from unittest.case import expectedFailure
from public.script import move

NO_RESULT = None, None
UP, RIGHT, DOWN, LEFT = "up", "right", "down", "left"


class SampleMoveTests(TestCase):

    def execute(self, state, dir):
        actual = None
        try:
            actual = move(state, dir)
        except Exception as e:
            pass
        self.assertEqual(type(actual), tuple)
        self.assertEqual(len(actual), 2)
        self.assertEqual(type(actual[0]), tuple)
        self.assertEqual(type(actual[1]), tuple)
        return actual

    def compare(self, state, dir, next_state, next_moves):
        actual = self.execute(state, dir)
        expected = (next_state, next_moves)
        self.assertEqual(expected, actual)

    def assertFail(self, state, direction, type_expected_exception):
        try:
            move(state, direction)
        except Exception as actual_exception:
            actual_exception_type = type(actual_exception)
            self.assertEqual(type_expected_exception, actual_exception_type)

    def test_invalid_empty_field0(self):
        self.assertFail((), UP, Warning)

    def test_invalid_empty_field1(self):
        self.assertFail(("",), UP, Warning)

    def test_invalid_empty_field2(self):
        self.assertFail(("", ""), UP, Warning)

    def test_incorrect_dimensions(self):
        self.assertFail((" ", "o "), UP, Warning)
        
    def test_invalid_no_player(self):
        self.assertFail(("  ",), RIGHT, Warning)

    def test_invalid_multiple_players(self):
        self.assertFail(("o o ",), RIGHT, Warning)

    def test_invalid_invalid_symbols(self):
        self.assertFail(("!o ",), RIGHT, Warning)

    def test_invalid_no_move_possible1(self):
        self.assertFail(("o",), RIGHT, Warning)

    def test_invalid_no_move_possible2(self):
        self.assertFail((" # ",
                         "#o#",
                         " # "), RIGHT, Warning)

    def test_invalid_no_move_possible3_rock(self):
        self.assertFail(("#o ",), LEFT, Warning)

    def test_invalid_no_move_possible3_oob(self):
        self.assertFail(("o ",), UP, Warning)



    def test_all_directions_are_recognized(self):
        actual = self.execute(("   ",
                               " o ",
                               "   ",
                               "   "), DOWN)
        self.assertTrue(DOWN in actual[1])
        self.assertTrue(LEFT in actual[1])
        self.assertTrue(RIGHT in actual[1])
        self.assertTrue(UP in actual[1])

    def test1b_move_up(self):
        self.compare((" ",
                      "o"), UP, ("o",
                                 " "),
                     (DOWN,))

    def test1c_move_right(self):
        self.compare(("o ",), RIGHT, (" o",), (LEFT,))

    def test1d_move_down(self):
        self.compare(("o",
                      " "), DOWN, (" ",
                                   "o"),
                     (UP,))

    def test1e_move_left(self):
        self.compare((" o",), LEFT, ("o ",), (RIGHT,))

    def test1f_all_directions_are_sorted(self):
        self.compare(("   ",
                      " o ",
                      "   ",
                      "   "), DOWN, ("   ",
                                     "   ",
                                     " o ",
                                     "   "),
                     (DOWN, LEFT, RIGHT, UP))

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
        self.compare(state, RIGHT, expected, (LEFT, UP))
