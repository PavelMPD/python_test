# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
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
        ("string", lambda s: s[1], "t"),
        ("string", lambda s: s[-1], "g"),
        ("string", lambda s: s[-2], "n"),
        ("string", lambda s: s[-1:], "g"),
        ("string", lambda s: s[-2:], "ng"),
        ("string", lambda s: s[0:2], "st"),
        ("string", lambda s: s[0:6:2], "srn"),
    ])
    def test_slice(self, s, l, expected_result):
        result = l(s)
        self.assertEqual(result, expected_result, (result, expected_result))

    @parameterized.expand([
        ("string", lambda s: s[::-1], "gnirts"),
        ("string", lambda s: "".join(reversed(s)), "gnirts"),
        ("string", lambda s: "".join(s[i] for i in range(len(s) - 1, -1, -1)), "gnirts"),
    ])
    def test_reverse(self, s, l, expected_result):
        result = l(s)
        self.assertEqual(result, expected_result, (result, expected_result))

    def test_length(self):
        s = "string"
        self.assertEqual(len(s), 6)

    @parameterized.expand([
        ("b", 1),
        ("в", 2),
    ])
    def test_byte_size(self, s, expected_size):
        size = len(s.encode("utf-8"))
        self.assertEqual(size, expected_size)


class StringFormattingTest(unittest.TestCase):
    @parameterized.expand([
        (
                "%s %r %c %c %d %i %o %x %f %%",
                ("str", "repr", 1, "a", 9.0, 5, 16, 15, 1.23),
                "str 'repr' \x01 a 9 5 20 f 1.230000 %"
        ),
        (
            "%(one)i %(two)s",
            {"one": 1, "two": "2"},
            "1 2"
        ),
        (
            "%d|%-5d|%5d|%+5d|%05d",
            (123, 123, 123, 123, 123),
            "123|123  |  123| +123|00123"
        ),
        (
            "%d|%-5d|%5d|%+5d|%05d",
            (1234567, 1234567, 1234567, 1234567, 1234567),
            "1234567|1234567|1234567|+1234567|1234567"
        ),
        (
            "%d|%-5d|%5d|%+5d|%05d",
            (-123, -123, -123, -123, -123),
            "-123|-123 | -123| -123|-0123"
        ),
        (
            "%d|%-5d|%5d|%+5d|%05d",
            (-1234567, -1234567, -1234567, -1234567, -1234567),
            "-1234567|-1234567|-1234567|-1234567|-1234567"
        ),
        (
            "%f|%5.2f|%0.0f|%0.1f|%1.1f",
            (123.123, 123.123, 123.123, 123.123, 123.123),
            "123.123000|123.12|123|123.1|123.1"
        ),
        ("%*.*f", (5, 1, 5.23), "  5.2"),
    ])
    def test_formatting_expression(self, expression, values, expected_result):
        result = expression % values
        self.assertEqual(result, expected_result)

    @parameterized.expand([
        ("{} {}", ("str", "repr"), dict(), "str repr"),
        ("{1} {0}", ("str", "repr"), dict(), "repr str"),
        ("{one} {two}", tuple(), {"one": 1, "two": 2}, "1 2"),
        ("{1[kind]} {0.platform}", (sys, {"kind": "laptop"}), dict(), "laptop linux"),
        ("{0:>3} {1:<3}", ("0", "1"), dict(), "  0 1  "),
        ("{0:f}, {1:.2f}, {2:06.2f}", (3.14159, 3.14159, 3.14159), dict(), "3.141590, 3.14, 003.14"),
        ("{0:X}, {1:o}, {2:b}", (255, 255, 255), dict(), "FF, 377, 11111111"),
        ("{number:.{precision}f}", tuple(), {"number": 3.1415, "precision": 3}, "3.142")
    ])
    def test_formatting_method(self, template, args, kwargs, expected_result):
        result = template.format(*args, **kwargs)
        self.assertEqual(result, expected_result)

    @parameterized.expand([
        (3.1415, ".2f", "3.14"),
        (3.1415, "^8.2f", "  3.14  "),
        (3333.1415, ",.2f", "3,333.14"),
    ])
    def test_format_function(self, value, format_spec, expected_result):
        self.assertEqual(format(value, format_spec), expected_result)


class StringMethodsTest(unittest.TestCase):
    @parameterized.expand([
        ("abc", "capitalize", None, None, "Abc"),
        ("abc", "casefold", None, None, "abc"),
        ("abc", "", None, None, ""),
        ("abc", "", None, None, ""),
        ("abc", "", None, None, ""),
        ("abc", "", None, None, ""),
        ("abc", "", None, None, ""),
        ("abc", "", None, None, ""),
        ("abc", "", None, None, ""),
        ("abc", "", None, None, ""),
        ("abc", "", None, None, ""),
        ("abc", "", None, None, ""),
        ("abc", "", None, None, ""),
    ])
    def test_method(self, value, method, args, kwargs, expected_result):
        if not method:
            return
        if args and kwargs:
            result = getattr(value, method)(*args, **kwargs)
        else:
            result = getattr(value, method)()
        self.assertEqual(result, expected_result)
