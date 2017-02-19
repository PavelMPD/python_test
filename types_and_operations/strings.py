# -*- coding: utf-8 -*-
from __future__ import unicode_literals

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
