#!/usr/bin/env python3

import builtins, sys
from unittest import TestCase

# replace input implementation
class YouCannotUseInputInACCESSException(Exception): pass
def crashing_input(prompt):
    raise YouCannotUseInputInACCESSException()
builtins.input_orig = builtins.input
builtins.input = crashing_input

# catch potential exception from import
import_ex = None
try:
    from public.game_logic import GameLogic
    from public.word_logic import WordLogic
    from public.number_logic import NumberLogic
except:
    import_ex = sys.exc_info()[0].__name__

class PrivateSmokeTestSuite(TestCase):

    def _run_example(self):
        w = WordLogic(10, 7, 5)
        self.assertEqual(10, w.num_words)
        self.assertEqual(7, w.len_words)
        self.assertEqual(5, w.num_attempts)
        self.assertEqual(len(w.words), w.num_words)
        self.assertEqual(w.password in w.words, True)

    def test_example(self):
        if import_ex:
            m = "@@Failed to import at least one of the files due to a '{}'.@@".format(import_ex)
            self.fail(m)

        # run example
        try:
            self._run_example()
        except AssertionError:
            m = "@@Running the provided example has an incorrect result. Make sure that " +\
                "the public test suite pass, before you attempt any submissions.@@"
            self.fail(m)
        except:
            m = "@@Failed to run the provided example. Make sure that the public test " +\
                "suite passes, before you attempt any submissions.@@"
            self.fail(m)

        # check if example can be run repeatedly
        try:
            self._run_example()
            self._run_example()
        except:
            m = "@@Failed to run the public test suite a second time. This might be caused by shared " +\
                "class variables that introduce unexpected side effects. We highly encourage you to " +\
                "add your own tests to the public test suite before you attempt any submissions.@@"
            self.fail(m)

