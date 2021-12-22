#!/usr/bin/env python3

from unittest import TestCase
import sys
import ast, types

import_ex = None
try:
    import public.script as implementation
except Exception as e:
    import_ex = e

class PrivateInformationHidingTestSuite(TestCase):

    def check_return(self, fun, t=ast.ListComp):
        import ast
        label = str(ast.ListComp)
        if t is ast.ListComp: label = "List Comprehension"
        if t is ast.DictComp: label = "Dict Comprehension"
        try:
            import inspect
            source = inspect.getsource(fun)
            tree = ast.parse(source)
            f_node = list(ast.iter_child_nodes(tree))[0]
            f_content = list(ast.iter_child_nodes(f_node))
            content_node = f_content[1]
            m = "@@The method definition of %s must start with a return statement.@@" % fun.__name__
            self.assertTrue(type(content_node) == ast.Return, m)
            return_value = list(ast.iter_child_nodes(content_node))[0]
            m = "@@The return value of %s must be a %s.@@" % (fun.__name__, label)
            self.assertTrue(type(return_value) == t, m)
        except AssertionError as e:
            raise e
        except:
            m = "@@There is something wrong with %s@@" % fun.__name__
            self.fail(m)

    def test01_words_containing_string(self):
        try:
            m = "@@words_containing_string does not return the right number of elements for a given string.@@"
            self.assertTrue(len(implementation.words_containing_string("good")) == 2, m)
            self.assertTrue(len(implementation.words_containing_string("and")) == 109, m)
            self.assertTrue(len(implementation.words_containing_string("bad")) == 3, m)
            self.check_return(implementation.words_containing_string)
        except AssertionError as e:
            raise e
        except:
            m = "@@words_containing_string should return a list of strings.@@"
            self.fail(m)

    def test02_words_starting_with_character(self):
        try:
            m = "@@words_starting_with_character does not return the right number of elements for a given character.@@"
            self.assertTrue(len(implementation.words_starting_with_character("a")) == 639, m)
            self.assertTrue(len(implementation.words_starting_with_character("q")) == 39, m)
            self.assertTrue(len(implementation.words_starting_with_character("j")) == 102, m)
            self.assertTrue(len(implementation.words_starting_with_character("p")) == 717, m)
            self.assertTrue(len(implementation.words_starting_with_character("z")) == 14, m)
            self.check_return(implementation.words_starting_with_character)
        except AssertionError as e:
            raise e
        except:
            m = "@@words_starting_with_character should return a list of strings.@@"
            self.fail(m)

    def test03_alphabet(self):
        m = "@@alphabet() must return 26 lower-case letters a through z as a single string.@@"
        try:
            ref = "abcdefghijklmnopqrstuvwxyz"
            r = implementation.alphabet()

            al_list = [chr(i) for i in range(ord("a"), ord("z")+1)]
            if r == al_list:
                m = "@@Calling alphabet() generates a list with the correct elements, but it should return a string.@@"
                self.fail(m)
            if type(r) != str:
                m = "@@Calling alphabet() should return a string.@@"
                self.fail(m)
            if r != ref:
                m = "@@Calling alphabet() does not return the correct string.@@"
                self.fail(m)
            import inspect
            source = inspect.getsource(implementation)
            m = "@@There are more elegant ways to get the alphabet in python other than just hard-coding it in place!@@"
            self.assertTrue(ref not in source, m)
        except AssertionError as e:
            raise e
        except:
            self.fail(m)

    def test04_dictionary(self):
        dm = "@@The return value of dictionary() should be a dict where each key is a letter of the alphabet and each corresponding value is a list containing all the words starting with that letter.@@"
        try:
            d = implementation.dictionary()
            m = "@@The return value of dictionary() must be a dict.@@"
            self.assertTrue(type(d) is dict, m)
            m = "@@The return value of dictionary() has the wrong number of keys.@@"
            self.assertTrue(len(d.keys()) == 26, m)
            self.assertTrue(len(d["a"]) == 639, dm)
            self.assertTrue(len(d["q"]) == 39, dm)
            self.assertTrue(len(d["j"]) == 102, dm)
            self.assertTrue(len(d["p"]) == 717, dm)
            self.assertTrue(len(d["z"]) == 14, dm)
            self.check_return(implementation.dictionary, t=ast.DictComp)
        except AssertionError as e:
            raise e
        except:
            self.fail(dm)

    def test05_censored_words(self):
        dm = "@@The return value of censored_words(s) should be a list of all original words, except that those containing s, for which all their characters should be replaced by 'x'. For example, 'abba' becomes 'xxxx'.@@"
        try:
            res = implementation.censored_words("and")
            m = "@@The return value of censored_words does not seem to contain the correct number of elements (should be the same as the word list). Remember that you do not want to filter the original list, but instead you transform every element: some stay the same, some are changed to a string of x's. This kind of 'if' situation belongs on the left side of the comprehension.@@"
            self.assertTrue(len(res) == 8845, m)
            m = "@@Calling censored_words() does not seem to return the correct number of censored elements.@@"
            d = [w for w in res if set(w) == set("x")]
            self.assertTrue(len(d) == 109, m)
            if res[17] != "xxxx" or res[1257] != "xxxxx" or res[2526] != "xxxxxx":  # andy, brand, andrea
                m = "@@The censoring does not consider the length of the word. Assuming the parameter is 'bad', " \
                    "the resulting list should replace 'badly' with 'xxxxx'.@@"
                self.fail(m)
            self.check_return(implementation.censored_words)
        except AssertionError as e:
            raise e
        except:
            self.fail(dm)


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

