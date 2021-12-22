import os
from unittest import TestCase
from public.script import get_average_grade

FILE = os.path.dirname(__file__) + "/test_grades.txt"


def delete():
    if os.path.exists(FILE):
        os.remove(FILE)


def write(lines):
    linesWithNewline = [l + "\n" for l in lines]
    with open(FILE, "x") as f:
        f.writelines(linesWithNewline)
    return "\\n".join(lines)


class PrivateTestSuite(TestCase):

    def setUp(self):
        import warnings
        warnings.simplefilter("ignore", ResourceWarning)
        delete()

    def tearDown(self):
        delete()

    def _assert(self, lines, expected, m=None):
        content = write(lines)
        actual = get_average_grade(FILE)
        if float != type(actual):
            m = "@@Returned value has incorrect type: expected float, was {}@@".format(type(actual).__name__)
            self.fail(m)
        if not m:
            m = "@@Calculation not correct for file:\n{}@@".format(content)
        self.assertAlmostEqual(expected, actual, delta=0.00001, msg=m)

    def test_no_file(self):
        actual = get_average_grade(FILE)
        m = "@@Calculation not correct for non-existing file.@@"
        self.assertEqual(None, actual, m)

    def test_empty_file(self):
        self._assert([], 0.0, "@@Calculation not correct for empty file.@@")

    def test_1(self):
        self._assert([
            "info1:3.25"], 3.25)

    def test_2(self):
        self._assert([
            "info1:4",
            "info2:5",], 4.5)

    def test_3(self):
        self._assert([
            "info1:4",
            "info2:5",
            "info3:5.25"], 4.75)

    def test_4(self):
        self._assert([
            "info1:4",
            "info2:5",
            "info3:5"], 4.6666666666666666666)


    def test_empty_line(self):
        self._assert([
            "info1:5",
            "",
            "info2:6",], 5.5)

    def test_comment(self):
        self._assert([
            "info1:4.75",
            "# empty",
            "info2:5.75",], 5.25)

    def test_with_spaces(self):
        self._assert([
            "informatik  1  :  3.75"], 3.75)

    def test_with_tabs(self):
        self._assert([
            "informatik\t1\t:\t4.00"], 4.00)
