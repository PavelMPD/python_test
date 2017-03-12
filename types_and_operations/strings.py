# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import time
import unittest
from nose_parameterized import parameterized


class StringTest(unittest.TestCase):
    def test_in_membership_expression(self):
        s = "some\x0Dtext"
        self.assertTrue("\r" in s)

        s = "some\x0Atext"
        self.assertTrue("\n" in s)

    def test_slice_expression(self):
        s = "some\ttext"
        slice_s = s[4:5]
        self.assertEqual(slice_s, "\t")

    def test_is_basestring(self):
        s = "some text"
        self.assertTrue(isinstance(s, str))

        l = list(s)
        self.assertFalse(isinstance(l, str))

    @parameterized.expand([
        ("\0000", 2),
        ("\1abc", 4),
        ("\12abc", 4),
    ])
    def test_octal_escape(self, value, count):
        self.assertTrue(len(value), count)

    @parameterized.expand([
        ("\xFF", 1),
        ("\x0A1", 2)
    ])
    def test_hex_escape(self, value, count):
        self.assertTrue(len(value), count)

    @parameterized.expand([
        ("\t", 1),
        ("\r\n", 2),
        ("\v", 1),
        ("\\", 1),
    ])
    def test_escape(self, value, count):
        # https://en.wikipedia.org/wiki/Escape_sequences_in_C
        self.assertTrue(len(value), count)

    def test_raw_string(self):
        value = r"\\"
        self.assertEqual(len(value), 2)

    def test_unicode_string(self):
        value = "текст"
        self.assertTrue(isinstance(value, str))

        # encode Unicode string by encoding to byte string
        encoded_string = value.encode(encoding='utf-8')
        self.assertTrue(encoded_string, bytes)

        # decode byte string in encoding to Unicode string
        decoded_string = encoded_string.decode(encoding='utf-8', errors='strict')
        self.assertTrue(isinstance(decoded_string, str))

    def test_concatenate(self):
        # http://stackoverflow.com/questions/12169839/which-is-the-preferred-way-to-concatenate-a-string-in-python

        s1 = "some text 1"
        s2 = "some text 2"

        start_time = time.time()
        sr = s1 + s2
        print("{} s".format(time.time() - start_time))
        self.assertEqual(sr, "some text 1some text 2")

        start_time = time.time()
        sr = list(s1)
        sr.append(s2)
        print("{} s".format(time.time() - start_time))
        self.assertEqual("".join(sr), "some text 1some text 2")

        start_time = time.time()
        sr = "".join([s1, s2])
        print("{} s".format(time.time() - start_time))
        self.assertEqual(sr, "some text 1some text 2")

    def test_repeat(self):
        result = "a" * 5
        self.assertEqual(result, "aaaaa")

    @parameterized.expand([
        ("string", 1, None, None, "t")
    ])
    def test_slice(self, s, i, j, k, expected_result):
        result = None
        if i and j is None and k is None:
            result = s[i]
        self.assertEqual(result, expected_result, (result, expected_result))
