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

    def test_chr(self):
        letter = chr(97)
        self.assertEqual('a', letter)

    def test_classmethod(self):
        class One(object):
            @classmethod
            def self(cls):
                return cls

        self.assertEqual(One, One.self())

    # http://stackoverflow.com/questions/22443939/python-built-in-function-compile-what-is-it-used-for
    # http://python-lab.blogspot.com.by/2012/05/exec-pythona.html
    def test_compile_and_exec(self):
        codes = compile('x = 3\nprint("X is", x)', 'my_module', 'exec')
        exec(codes)
        self.assertEqual(3, x)

    def test_complex(self):
        a = complex("1+2j")
        self.assertEqual((1+2j), a)

    def test_delattr(self):
        class O(object): pass
        o = O()
        o.a = 5
        self.assertTrue('a' in o.__dict__)
        delattr(o, 'a') # del o.a
        self.assertFalse('a' in o.__dict__)

    def test_dict(self):
        raise NotImplementedError('dict class usage')

    def test_dir(self):
        import built_in_features

        class O(object):
            def m(self):
                pass
        o = O()
        o.a = 5
        local_scope_names = dir()
        self.assertEqual({'O', 'o', 'self', 'built_in_features'}, set(local_scope_names))
        self.assertEqual({'a', 'm'}, {'a', 'm'}.intersection(dir(o)))

    def test_divmod(self):
        quotient, remainder = divmod(6, 4)
        self.assertEqual((1, 2), (quotient, remainder))

    def test_enumerate(self):
        items = ['a', 'b']
        enumerated_items = enumerate(items, start=1)
        self.assertEqual([(1, 'a'), (2, 'b')], list(enumerated_items))

    def test_eval(self):
        x = 1
        y = eval("x + 2")
        self.assertEqual(3, y)

    def test_filter(self):
        result = filter(None, enumerate(['b', 'a'], start=1))
        self.assertEqual([(1, 'b'), (2, 'a')], list(result))

        result = filter(lambda x: x[1] != 'a', enumerate(['b', 'a'], start=1))
        self.assertEqual([(1, 'b')], list(result))



    def test_map(self):
        list1 = [1, 2]
        list2 = [3, 1]
        max_values = map(max, list1, list2)
        self.assertEqual([3, 2], list(max_values))

    def test_lambda(self):
        max_values = map(lambda x, y: max(x, y), [1, 2, 9, 0], [3, 1, 10, -1])
        self.assertEqual([3, 2, 10, 0], list(max_values))

    def test_zip(self):
        list1 = [1, 2, 3]
        list2 = ['a', 'b', 'c', 'd']
        zipped = zip(list1, list2)
        self.assertEqual([(1, 'a'), (2, 'b'), (3, 'c')], list(zipped))
