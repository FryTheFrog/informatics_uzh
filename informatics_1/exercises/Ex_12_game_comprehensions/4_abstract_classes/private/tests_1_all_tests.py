#!/usr/bin/env python3

from unittest import TestCase
from unittest.mock import mock_open, patch
from abc import ABC
import sys
import ast, types
import math
import re

# catch potential exception from import
import_ex = None
try:
    from public.game_logic import GameLogic
    from public.word_logic import WordLogic
    from public.number_logic import NumberLogic
except:
    import_ex = sys.exc_info()[0].__name__

filename = 'resource/words.txt'
with open(filename) as f:
    read_data = f.read()
    word_list = [word.rstrip().upper() for word in read_data.split('\n')]


class PrivateInformationHidingTestSuite(TestCase):

    def exists_gamelogic(self):
        m = "@@The GameLogic class does not seem to exist in script.py.@@"
        try: GameLogic
        except: self.fail(m)
    def exists_wordlogic(self):
        m = "@@The WordLogic class does not seem to exist in script.py.@@"
        try: WordLogic
        except: self.fail(m)
    def exists_numberlogic(self):
        m = "@@The NumberLogic class does not seem to exist in script.py.@@"
        try: NumberLogic
        except: self.fail(m)

    def instantiable_numberlogic(self):
        try:
            logic = NumberLogic(50, 10, 4)
        except IndexError:
            m = "@@An IndexError occured while trying to instantiate a NumberLogic object.@@"
            self.fail(m)
        except:
            m = "@@Cannot instantiate NumberLogic. Did you implement all abstract methods of its abstract super class?@@"
            self.fail(m)

    def test_1_abstract_class(self):
        if import_ex:
            if "'ABC' is not defined" in str(import_ex):
                m = "@@Did you forget to import ABC?@@".format(import_ex)
                self.fail(m)
            elif "'abstractmethod' is not defined" in str(import_ex):
                m = "@@Did you forget to import abstractmethod?@@".format(import_ex)
                self.fail(m)
            else:
                m = "@@Failed to import your implementation: '{}'.@@".format(import_ex)
                self.fail(m)

        self.exists_gamelogic()
        m = "@@The GameLogic class does not seem to be abstract. Make sure it inherits from ABC.@@"
        self.assertTrue(issubclass(GameLogic, ABC), m)

    def test_2_abstract_functions(self):
        self.exists_gamelogic()
        import inspect
        source = inspect.getsourcelines(GameLogic)[0]
        decorated_functions = []
        for i, j in enumerate(source):
            if j.strip().startswith("@"):
                _deco = source[i].strip()
                _impl = source[i+1].strip()
                if _impl.endswith("pass"):
                    _impl = _impl[:-4]
                    _pass = "pass"
                else:
                    _pass = source[i + 2].strip()
                decorated_functions.append((_deco, _impl, _pass))

        m = "@@Make sure that the GameLogic class declares exactly two abstract methods.@@"
        self.assertEqual(len(decorated_functions), 2, m)

        r = re.compile('def ([^(]*)\(.*')
        for deco, sig, impl in decorated_functions:
            res = r.match(sig)
            name = res.group(1)
            m = "@@Apparently, there exists an abstract method %s in GameLogic, where it should not exist.@@" % name
            self.assertTrue(name in ["_word_selection", "_generate_feedback"], m)
            m = "@@Apparently, a decorator %s was used in GameLogic, where it should not.@@" % deco
            self.assertEqual(deco, "@abstractmethod", m)
            m = "@@The function %s in GameLogic should be abstract and should not have any implementation (remember the 'pass' keyword).@@" % name
            self.assertEqual(impl, "pass", m)

    def test_2_inheritance_word_logic(self):
        self.exists_gamelogic(); self.exists_wordlogic()
        m = "@@WordLogic should inherit from GameLogic.@@"
        self.assertTrue(issubclass(WordLogic, GameLogic), m)

    def test_3_inheritance_number_logic(self):
        self.exists_gamelogic(); self.exists_numberlogic()
        m = "@@NumberLogic should inherit from GameLogic.@@"
        self.assertTrue(issubclass(NumberLogic, GameLogic), m)

    def test_4_inheritance_inits(self):
        self.exists_gamelogic(); self.exists_wordlogic()
        m = "@@WordLogic should not define its own __init__ function. The constructor should be inherited from GameLogic.@@"
        self.assertEqual(GameLogic.__init__, WordLogic.__init__, m)
        m = "@@NumberLogic should not define its own __init__ function. The constructor should be inherited from GameLogic.@@"
        self.assertEqual(GameLogic.__init__, NumberLogic.__init__, m)

    def test_5_word_selection(self):
        self.exists_numberlogic()
        self.instantiable_numberlogic()
        logic = NumberLogic(50, 10, 4)
        words = logic.words
        self.assertEqual(len(set(words)), len(words), "@@NumberLogic's word_selection return value contains duplicates.@@")

    def test_5b_word_selection(self):
        self.exists_numberlogic()
        self.instantiable_numberlogic()
        logic = NumberLogic(50, 10, 4)
        words = logic.words
        for w in words:
            self.assertEqual(len(w), logic.len_words, "@@NumberLogic's word_selection return value contains words with the wrong length.@@")

    def test_5c_word_selection(self):
        self.exists_numberlogic()
        self.instantiable_numberlogic()
        logic = NumberLogic(50, 10, 4)
        words = logic.words
        for w in words:
            self.assertTrue(w.isnumeric(), "@@NumberLogic's word_selection return value contains non-numbers.@@")

    def test_5d_number_logic_no_repetition_in_numbers(self):
        logic = NumberLogic(100, 10, 4)
        words = logic.words
        for w in words:
            for i in range(0, 10):
                count = w.count(str(i))
                if count > 1:
                    m = "@@NumberLogic._word_selection must avoid selecting the same number multiple times when " \
                        "selecting the words on initialization.@@"
                    self.fail(m)

    def test_5e_reject_guesses_with_repeating_numbers(self):
        try:
            sut = NumberLogic(100, 10, 4)
            sut.check("0000")
        except Warning:
            pass
        except:
            m = "@@Unexpected failure when callin NumberLogic.check with a guess that contains repeated numbers.@@"
            self.fail(m)
        else:
            m = "@@Implementation of NumberLogic.check should reject guesses that contain repeated numbers.@@"
            self.fail(m)

    @patch('builtins.open', new_callable=mock_open, read_data=read_data)
    def test_6_check(self, mock_open):
        self.exists_numberlogic()
        self.instantiable_numberlogic()
        password = '1234'
        num_words = 7
        logic = NumberLogic(num_words, 4, 7)
        logic.words = word_list
        logic.password = password

        def check_res(guess, n, correct):
            result, feedback = logic.check(guess)

            m = "@@NumberLogic's check function returns %s where it should be %s.@@" % (not correct, correct)
            self.assertEqual(result, correct, m)

            ratio = (n, logic.len_words)
            expected = [
                "%d/%d correct" % ratio,
                "Access denied!"
            ]
            m = "@@NumberLogic's check function's feedback says '%s' where it should be '%d/%d correct'.@@" % (feedback[0], *ratio)
            self.assertEqual(feedback, expected, m)

        check_res('5678', 0, False)
        check_res('1678', 1, False)
        check_res('1673', 2, False)
        check_res('1238', 3, False)
        check_res('4321', 4, False)
        check_res('1230', 3, False)

        result, feedback = logic.check(logic.password)
        self.assertTrue(result, "@@NumberLogic's check function returns False where it should be True.@@")
        m = "@@NumberLogic's check function's feedback says %s where it should be 'Access granted!'.@@" % feedback[0]
        self.assertEqual(feedback, ["Access granted!"], m)

        with self.assertRaises(Warning):
            result, feedback = logic.check('123')

    @patch('builtins.open', new_callable=mock_open, read_data=read_data)
    def test_6_more_weight(self, mock_open):
        self.test_6_check()

    @patch('builtins.open', new_callable=mock_open, read_data=read_data)
    def test_6_more_weight(self, mock_open):
        self.test_6_check()


class SolutionVisitor(ast.NodeVisitor):

    def __init__(self):
        self.hasAssignInGlobalScope = False

    def visit_If(self, node):
        try:
            if node.test.left.id == "__name__":
                return
        except:
            self.generic_visit(node)

    def visit_Assign(self, node):
        self.hasAssignInGlobalScope = True

    def visit_FunctionDef(self, node):
        return

    def visit_ClassDef(self, node):
        return
