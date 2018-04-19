# -*- coding: utf-8 -*-
import unittest

x = 1


class ScopesTest(unittest.TestCase):
    def test_comprehension_variables(self):
        i = 5
        l = [i for i in [0, 1]]
        self.assertEqual(i, 5)

    def test_exception_variables(self):
        ex = 'error'

        try:
            raise ValueError()
        except ValueError as ex:
            assert ex != 'error'

        try:
            assert ex == 'error'
        except UnboundLocalError:
            pass

    @staticmethod
    def set_x():
        global x
        x = 3

    def test_global_variables(self):
        self.set_x()
        self.assertEqual(x, 3)

    def test_nonlocal_statement(self):
        x = 5
        def set_x(value):
            x = value
        set_x(7)
        self.assertEqual(x, 5)

        def set_x(value):
            nonlocal x
            x = value
        set_x(7)
        self.assertEqual(x, 7)
