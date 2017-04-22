# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import unittest
import collections

from nose_parameterized import parameterized


class TupleTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Run the setUpClass method")

    @classmethod
    def tearDownClass(cls):
        print("Run the tearDownClass method")

    def setUp(self):
        print("Run the setUp method")

    def tearDown(self):
        print("Run the tearDown method")

    def test_create(self):
        t = (1, )
        with self.subTest("first"):
            self.assertEqual(t[0], 1)

        t2 = tuple("str")
        with self.subTest("second"):
            self.assertEqual(t2, ("s", "t", "r"))

    def test_slice(self):
        t = tuple(range(10))
        self.assertEqual(t[3:6], (3, 4, 5))

    def test_concatenate(self):
        t1 = (1, 2)
        t2 = (4, 5)
        self.assertEqual(t1+t2, (1, 2, 4, 5))

    def test_repeat(self):
        t = (1, 2) * 2
        self.assertEqual(t, (1, 2, 1, 2))

    def test_create_namedtuple(self):
        c = collections.namedtuple("Car", ["width", "length"])
        car = c(width=50, length=150)
        self.assertEqual(car[0], getattr(car, "width"))
        self.assertEqual(car[1], getattr(car, "length"))

    def test_namedtuple_to_dict(self):
        c = collections.namedtuple("Car", ["width", "length"])
        car = c(width=50, length=150)
        d = car._asdict()
        self.assertEqual(
            d, collections.OrderedDict([("width", 50), ("length", 150)]))

    def test_count(self):
        t = (1, 2, 3, 3)
        self.assertEqual(t.count(3), 2)

    def test_index(self):
        t = (1, 2, 3, 2, 2, 3, 2, 2, 3)
        self.assertEqual(t.index(3, 3, 6), 5)

    def test_sort(self):
        t = tuple("google")
        self.assertEqual(sorted(t), ["e", "g", "g", "l", "o", "o"])
