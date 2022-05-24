import os
from unittest import TestCase
from public.script import process_data

INPUT_FILE = os.path.dirname(__file__) + "/my_test_data.txt"
OUTPUT_FILE = os.path.dirname(__file__) + "/my_test_data_processed.txt"


def delete():
    if os.path.exists(INPUT_FILE):
        os.remove(INPUT_FILE)
    if os.path.exists(OUTPUT_FILE):
        os.remove(OUTPUT_FILE)


def write(lines):
    linesWithNewline = [l + "\n" if l != lines[-1] else l for l in lines]
    with open(INPUT_FILE, "x") as f:
        f.writelines(linesWithNewline)
    return "\\n".join(lines)

class PrivateTestSuite(TestCase):

    def setUp(self):
        import warnings
        warnings.simplefilter("ignore", ResourceWarning)
        delete()

    def tearDown(self):
        delete()

    def _assert(self, lines, expected):
        content = write(lines)
        process_data(INPUT_FILE, OUTPUT_FILE)
        if os.path.exists(OUTPUT_FILE):
            with open(OUTPUT_FILE, "r") as f:
                actual = f.read()
        else:
            actual = None

        m = "@@Conversion was not correct for file:\n{}@@".format(content)
        self.assertEqual(expected, actual, m)


    def test_no_file(self):
        actual = process_data(INPUT_FILE, OUTPUT_FILE)
        m = "@@If file does not exist, False should be returned.@@"
        self.assertEqual(False, actual, m)

    def test_empty_file(self):
        lines = ""
        write(lines)
        process_data(INPUT_FILE, OUTPUT_FILE)
        if os.path.exists(OUTPUT_FILE):
            self.assertTrue(os.stat(OUTPUT_FILE).st_size == 0,
                        "@@An empty file should result in an empty file.@@")
        else:
            self.assertEqual("", None, "@@An empty file should result in an empty file.@@")

    def test_only_header(self):
        self._assert([
            "Name"], "Firstname,Lastname")

    def test_format1(self):
        self._assert([
            "Name",
            "Quirinus Quirrell"], "Firstname,Lastname\nQuirinus,Quirrell")

    def test_format2(self):
        self._assert([
            "Name",
            "Brickowski; Emmet"], "Firstname,Lastname\nEmmet,Brickowski")

    def test_empty_line(self):
        self._assert([
            "Name",
            "",
            "",
            "Brickowski; Emmet"], "Firstname,Lastname\n,\n,\nEmmet,Brickowski")

    def test_multiple_lines_format1(self):
        self._assert([
            "Name",
            "Guy Parmelin",
            "Alain Berset"], "Firstname,Lastname\n"
                             "Guy,Parmelin\n"
                             "Alain,Berset")

    def test_multiple_lines_format2(self):
        self._assert([
            "Name",
            "Amherd; Viola",
            "Sommaruga; Simonetta"], "Firstname,Lastname\n"
                                     "Viola,Amherd\n"
                                     "Simonetta,Sommaruga")

    def test_multiple_lines(self):
        self._assert([
            "Name",
            "Tim Li",
            "Al; Bea",
            "",
            "",
            "Bi; Flo"], "Firstname,Lastname\n"
                        "Tim,Li\n"
                        "Bea,Al\n"
                        ",\n"
                        ",\n"
                        "Flo,Bi")
