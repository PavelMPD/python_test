import unittest


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

    def test_octal_escape(self):
        s = "\000"
        self.assertTrue(len(s), 1)

    def test_hex_escape(self):
        s = "\xFF"
        self.assertTrue(len(s), 1)
