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
