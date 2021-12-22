#!/usr/bin/env python3

from unittest import TestCase
from public.script import Fridge


class PrivateFunctionalTestSuite(TestCase):

    def myEq(self, expected, actual, m):
        if type(expected) != type(actual):
            m = "@@{}: wrong return type.@@".format(m)
            self.fail(m)
        if expected != actual:
            m = "@@{}: incorrect value.@@".format(m)
            self.fail(m)

    def test00_defaults_len(self):
        try:
            sut = Fridge()
        except:
            self.fail("@@Failed to init a fridge.@@")
        try:
            actual = len(sut)
        except:
            self.fail("@@Failed to get the length from an empty fridge.@@")
        self.myEq(0, actual, "Length calculation does not work for empty fridge")

    def test01_defaults_iter(self):
        try:
            sut = Fridge()
            actual = list(sut)
        except:
            self.fail("@@Failed to iterate an empty fridge.@@")
        self.assertEquals([], actual, "@@Iterating an empty fridge does not work.@@")

    def test02_item_store_and_take(self):
        sut = Fridge()
        expected = (123456, "x")
        try:
            sut.store(expected)
        except:
            self.fail("@@Failed while storing an item into a fridge.@@")
        try:
            actual = sut.take((123456, "x"))
        except:
            self.fail("@@Failed while taking an item out of a fridge.@@")
        self.myEq(expected, actual, "Storing and taking the same item does not work")

    def test03_len_does_work(self):
        try:
            sut = Fridge()
            sut.store((123456, "x"))
            actual = len(sut)
        except:
            self.fail("@@Failed to get the length from a fridge while storing and taking out items.@@")

        if actual == 0:
            self.fail("@@It seems that storing an item into a fridge does not affect __len__.@@")
        else:
            self.myEq(1, actual, "__len__ does not work after storing an item")

        try:
            sut.take((123456, "x"))
            actual = len(sut)
        except:
            self.fail("@@Failed to get the length from a fridge while storing and taking out items.@@")

        if actual == 1:
            self.fail("@@It seems that taking an item out of a fridge does not affect __len__.@@")
        else:
            self.myEq(0, actual, "__len__ does not work after taking an item out again")

    def test04_items_get_sorted(self):
        a = (111111, "a")
        b = (111112, "b")
        c = (111113, "c")
        try:
            sut = Fridge()
            sut.store(b)
            sut.store(a)
            sut.store(c)
        except:
            self.fail("@@Failed to store three different items with varying eat-by date.@@")
        try:
            actual = list(sut)
        except:
            self.fail("@@Failed to iterate over a fridge that contains three items with varying eat-by date.@@")

        if actual == [b, a, c]:
            self.fail("@@The Fridge iterates items in addition order, instead of sorting by eat-by date.@@")
        elif actual == [c, a, b]:
            self.fail("@@The Fridge iterates items in inverse addition order, instead of sorting by eat-by date.@@")
        elif actual == [c, b, a]:
            self.fail("@@The order of iteration is descending by eat-by date, instead of ascending.@@")
        else:
            expected = [a, b, c]
            self.myEq(expected, actual, "Iterating a fridge that contains three items with varying eat-by date does not work")

    def test05_error_on_non_existing_item(self):
        m = None
        with self.assertRaises(Warning, msg="@@Taking out a non-existing item does not raise a Warning.@@"):
            try:
                sut = Fridge()
                sut.take((123456, "x"))
            except Warning:
                raise
            except:
                m = "@@Taking out a non-existing item causes the wrong exception, Warning expected.@@"
        if m:
            self.fail(m)

    def test06_finds_right_item(self):
        a = (111111, "a")
        b = (111112, "a")
        c = (111113, "a")
        try:
            sut = Fridge()
            sut.store(b)
            sut.store(a)
            sut.store(c)
        except:
            self.fail("@@Failed to store the same items three times with varying eat-by date.@@")
        try:
            actual = sut.find("a")
        except:
            self.fail("@@Failed to find an item by name.@@")

        if actual == b:
            m = "@@The find function seems to return the first item that was added, " +\
                "not the one with the soonest eat-by date.@@"
            self.fail(m)
        elif actual == c:
            m = "@@The Fridge iterates items in inverse addition order, instead of sorting " +\
                "by ascending eat-by date.@@"
            self.fail(m)
        else:
            self.myEq(a, actual, "Finding an item by name does not work")

    def test07_find_does_not_change(self):
        try:
            sut = Fridge()
            sut.store((111111, "a"))
        except:
            self.fail("@@Failed to store an item in the fridge.@@")
        try:
            sut.find("a")
            actual = len(sut)
        except:
            self.fail("@@Failed to find an item by name.@@")

        if actual == 0:
            self.fail("@@'find' should only identify an item. However, the implementation seems to take it out.@@")

    def test08_find_does_not_have_to_match(self):
        try:
            sut = Fridge()
            actual = sut.find("a")
        except:
            self.fail("@@Failed to find an item in an empty fridge.@@")
        self.assertEquals(None, actual, "@@Finding a non-existing item in a fridge does not work.@@")

    def test09_take_before_works(self):
        a = (111111, "a")
        b = (111112, "b")
        try:
            sut = Fridge()
            sut.store(b)
            sut.store(a)
            actual = sut.take_before(111112)
        except:
            self.fail("@@Failed to store multiple items and take some out by date.@@")

        if len(actual) == 2 and a in actual and b in actual:
            m = "@@'take_before' should only take out items that will go bad before a provided date." +\
                "An item with the same eat-by date is still good on that day.@@"
            self.fail(m)
        elif actual == [b]:
            m = "@@'take_before' should take out items that will go bad before the date, instead, it " +\
                "currently returns all items that are still good on that day.@@"
            self.fail(m)
        else:
            self.myEq([a], actual, "Taking out items by date does not work")

    def test10_take_before_removes_items(self):
        try:
            sut = Fridge()
            sut.store((111111, "a"))
            sut.take_before(111112)
            actual = len(sut)
        except:
            self.fail("@@Failed to store multiple items and take some out by date.@@")
        self.assertEquals(0, actual, "@@Items taken out by date need to be removed from the fridge.@@")

    def test11_take_before_no_match(self):
        try:
            sut = Fridge()
            sut.store((111111, "a"))
            actual = sut.take_before(111110)
        except:
            self.fail("@@Failed to store multiple items and take some out by date.@@")
        self.assertEquals([], actual, "@@'take_before' should return an empty list, when no item matches.@@")
