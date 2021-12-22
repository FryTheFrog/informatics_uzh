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
    from public.script import GameRunner
except:
    import_ex = sys.exc_info()[0].__name__

class PrivateSmokeTestSuite(TestCase):

    def test_example(self):
        if import_ex:
            m = "@@Failed to import the implementation of GameRunner due to an '{}'.@@".format(import_ex)
            self.fail(m)

        try:
            g = GameRunner()
            res = g.generate_hex_codes()
            self.assertEqual(len(res), g.rows * g.columns)
        except AssertionError:
            m = "@@Running the provided example has an incorrect result. Make sure that " +\
                "the public test suite passes, before you attempt any submissions.@@"
            self.fail(m)
        except:
            m = "@@Failed to run the provided example. Make sure that the public test" +\
                "suite passes, before you attempt any submissions.@@"
            self.fail(m)

        # To ensure that no points are given for submitting the task unchanged
        g = GameRunner()
        res = g.generate_hex_codes()
        m = "@@All hex codes are the same.@@"
        ref = [res[0]]
        res = list(set(res))
        self.assertNotEqual(res, ref, m)

