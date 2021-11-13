from unittest import TestCase
from game import move

class MoveTestSuite(TestCase):

    # legal moves
    def test_move_right(self):
        state = (
            "#####   ",
            "###    #",
            "#   o ##",
            "   #####"
        )
        actual = move(state, "right")
        expected = (
            (
                "#####   ",
                "###    #",
                "#    o##",
                "   #####"
            ),
            ("left", "up")
        )
        self.assertEqual(expected, actual)

    def test_move_left(self):
        state = (
            "#####   ",
            "###    #",
            "#   o ##",
            "   #####"
        )
        actual = move(state, "left")
        expected = (
            (
                "#####   ",
                "###    #",
                "#  o  ##",
                "   #####"
            ),
            ("left", "right", "up")
        )
        self.assertEqual(expected, actual)

    def test_move_up(self):
        state = (
            "#####   ",
            "###    #",
            "#   o ##",
            "   #####"
        )
        actual = move(state, "up")
        expected = (
            (
                "#####   ",
                "### o  #",
                "#     ##",
                "   #####"
            ),
            ("down", "left", "right")
        )
        self.assertEqual(expected, actual)

    # invalid move
    def test_move_invalid(self):
        state = (
            "#####   ",
            "###    #",
            "#   o ##",
            "   #####"
        )
        with self.assertRaises(Warning):
            move(state, "down")

    def test_move_invalid2(self):
        state = (
            "#####   ",
            "###    #",
            "#     ##",
            " o #####"
        )
        with self.assertRaises(Warning):
            move(state, "down")

    # no possible moves
    def test_no_moves(self):
        state = (
            "#####   ",
            "####o###",
            "#   # ##",
            "   #####"
        )
        with self.assertRaises(Warning):
            move(state, "up")
    
    def test_no_moves2(self):
        state = (
            "#####   ",
            "###    #",
            "#     ##",
            "o# #####"
        )
        with self.assertRaises(Warning):
            move(state, "up")

    def test_no_moves3(self):
        state = (
            "o"
        )
        with self.assertRaises(Warning):
            move(state, "left")

    # invalid dimension
    def test_dimension(self):
        state = (
            "",
            "",
            "",
            ""
        )
        with self.assertRaises(Warning):
            move(state, "up")
            
    def test_dimension2(self):
        state = (
        )
        with self.assertRaises(Warning):
            move(state, "up")

    # inconsistent length of lines
    def test_length(self):
        state = (
            "##### ",
            "###    #",
            "#   o #",
            "    #####"
        )
        with self.assertRaises(Warning):
            move(state, "up")

    def test_length2(self):
        state = (
            "#####   ",
            "###    #",
            "#   o ##",
            "  #####"
        )
        with self.assertRaises(Warning):
            move(state, "up")

    # invalid char
    def test_char(self):
        state = (
            "#####   ",
            "###    #",
            "#   o ##",
            "   x####"
        )
        with self.assertRaises(Warning):
            move(state, "up")

    # invalid player count
    def test_playercount(self):
        state = (
            "##### o ",
            "###o   #",
            "#   o ##",
            "   #####"
        )
        with self.assertRaises(Warning):
            move(state, "up")

    def test_playercount2(self):
        state = (
            "#####   ",
            "###    #",
            "# oo  ##",
            "   #####"
        )
        with self.assertRaises(Warning):
            move(state, "up")

    def test_playercount3(self):
        state = (
            "#####   ",
            "###    #",
            "#     ##",
            "   #####"
        )
        with self.assertRaises(Warning):
            move(state, "up")

    def test_playercount4(self):
        state = (
            "  ",
            "  ",
            "  ",
            "  ",
            "oo"
        )
        with self.assertRaises(Warning):
            move(state, "up")