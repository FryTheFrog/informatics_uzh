import sys
from unittest import TestCase
import inspect
import importlib

class PrivateTestSuite(TestCase):

    def setUp(self):
        def delete_modules():
            if "public.script" in sys.modules: del sys.modules["public.script"]
            if "public.tests" in sys.modules: del sys.modules["public.tests"]
            if "private.correct" in sys.modules: del sys.modules["private.correct"]
            if "private.buggy" in sys.modules: del sys.modules["private.buggy"]
            if "private" in sys.modules: del sys.modules["private"]
            if "public" in sys.modules: del sys.modules["public"]
            importlib.invalidate_caches()
        self.addCleanup(delete_modules)

    def test_fizzbuzz(self):
        from public import script
        script.n = 200115
        res = script.fizz_buzz()
        m = "@@fizz_buzz() doesn't return 'FizzBuzz' for every n divisible by both 3 and 5.@@"
        self.assertEqual(res, "FizzBuzz", m)

    def test_testfive(self):
        from private import correct
        import public.tests
        public.tests.script = correct
        source = inspect.getsource(public.tests.PublicTestSuite.test_five).splitlines()[-1]
        m = "@@test_five() does not seem to be implemented.@@"
        self.assertTrue("pass" not in source, m)
        try:
            public.tests.PublicTestSuite.test_five(self)
        except AssertionError:
            m = "@@test_five() shouldn't fail when run on the unmodified script.py@@"
            raise AssertionError(m)

    def test_testfifteen_buggy(self):
        from private import buggy
        import public.tests
        public.tests.script = buggy
        m = "@@test_fifteen() must fail when run on the unmodified script.py@@"
        try:
            with self.assertRaises(AssertionError):
                public.tests.PublicTestSuite.test_fifteen(self)
        except AssertionError:
            raise self.failureException(m)

    def test_testfifteen_good(self):
        from private import correct
        import public.tests
        public.tests.script = correct
        source = inspect.getsource(public.tests.PublicTestSuite.test_fifteen).splitlines()[-1]
        m = "@@test_fifteen() does not seem to be implemented.@@"
        self.assertTrue("pass" not in source, m)
        try:
            public.tests.PublicTestSuite.test_fifteen(self)
        except AssertionError:
            m = "@@test_fifteen() shouldn't fail when run on a bug-free script.py@@"
            raise AssertionError(m)

