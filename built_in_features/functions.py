import unittest


class BuiltInFunctionsTests(unittest.TestCase):
    def test_all(self):
        l = [object(), None]
        result = all(l)
        self.assertFalse(result)

        l = [object(), object()]
        result = all(l)
        self.assertTrue(result)

    def test_any(self):
        l = [object(), None]
        result = any(l)
        self.assertTrue(result)

        l = [None, None]
        result = any(l)
        self.assertFalse(result)

    def test_ascii(self):
        raise NotImplementedError('ascii function usage')

    def test_bin(self):
        result = bin(4)
        self.assertEqual('0b100', result)

    def test_bool(self):
        l = [0, None, '']
        [self.assertFalse(bool(item)) for item in l]

        l = [1, object()]
        [self.assertTrue(bool(item)) for item in l]

    def test_bytearray(self):
        raise NotImplementedError('bytearray function usage')

    def test_bytes(self):
        raise NotImplementedError('bytes function usage')

    def test_callable(self):
        callable_list = [abs, bin, object]
        [self.assertTrue(callable(item)) for item in callable_list]

        not_callable_list = [object(), None, 1]
        [self.assertFalse(callable(item)) for item in not_callable_list]
