# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import copy
import unittest
import collections


class DictConstructionTest(unittest.TestCase):
    def test_keywords_construction(self):
        d = dict(user=dict(name="user name"))
        self.assertIn("user", d)
        self.assertIn("name", d["user"])

    def test_key_value_pairs_construction(self):
        d = dict([("login", ""), ("password", "")])
        self.assertIn("login", d)
        self.assertIn("password", d)

    def test_zipped_construction(self):
        keys = {"login", "password"}
        values = ["user1", "111"]
        d = dict(zip(keys, values))
        self.assertEqual(d.keys(), keys)

    def test_keys_construction(self):
        keys = {"login", "password"}
        d = dict.fromkeys(keys)
        self.assertEqual(d.keys(), keys)


class DictCopyTest(unittest.TestCase):
    def test_top_level_copy_dict(self):
        # Shallow copying, a and b will become two isolated objects,
        # but their contents still share the same reference

        d = {"user": {"name": "n1", "password": "123"}, "count": 1}
        d2 = d.copy()
        d2["count"] = 2
        d2["user"]["password"] = "321"
        self.assertNotEqual(d2["count"], d["count"])
        self.assertEqual(d["user"]["password"], d2["user"]["password"])

        d = {"user": {"name": "n1", "password": "123"}, "count": 1}
        d2 = copy.copy(d)
        d2["count"] = 2
        d2["user"]["password"] = "321"
        self.assertEqual(d["user"]["password"], d2["user"]["password"])

    def test_deep_copy_dict(self):
        # Deep copying, a and b structure
        # and content become completely isolated.

        d = {"user": {"name": "n1", "password": "123"}}
        d2 = copy.deepcopy(d)
        d2["user"]["password"] = "321"
        self.assertNotEqual(d["user"]["password"], d2["user"]["password"])


class DictTest(unittest.TestCase):
    def test_nesting(self):
        d = {"user": {"name": "user name", "password": "password"}}
        self.assertIn("user", d)
        self.assertIn("name", d["user"])

    def test_membership(self):
        d = {"login": "u1", "password": "123"}
        self.assertIn("login", d)
        self.assertIn("password", d)

    def test_get_keys(self):
        d = {"login": "u1", "password": "123"}
        self.assertEqual(set(d.keys()), {"login", "password"})

    def test_get_values(self):
        d = {"login": "u1", "password": "123"}
        self.assertEqual(set(d.values()), {"u1", "123"})

    def test_get_items(self):
        d = {"login": "u1", "password": "123"}
        self.assertEqual(set(d.items()), {("login", "u1"), ("password", "123")})

    def test_remove_all_items(self):
        d = {"login": "u1", "password": "123"}
        d.clear()
        self.assertEqual(d, dict())

        d = {"login": "u1", "password": "123"}
        d.pop("login")
        d.pop("password")
        self.assertEqual(d, dict())

        d = {"login": "u1", "password": "123"}
        del d["login"]
        del d["password"]
        self.assertEqual(d, dict())

    def test_merge_by_keys(self):
        d = {"login": "u1"}
        d2 = {"login": "u2", "password": "123"}
        d.update(d2)
        self.assertEqual(d, d2)


class DictFetchTest(unittest.TestCase):
    def test_fetch(self):
        d = {"login": "u1", "password": "123"}
        v = d.get("login")
        self.assertEqual(v, "u1")
        v = d.get("name")
        self.assertIsNone(v)

    def test_fetch_and_remove(self):
        d = {"login": "u1", "password": "123"}
        v = d.pop("login")
        self.assertEqual(v, "u1")
        self.assertEqual(d.keys(), {"password"})

    def test_fetch_item_and_remove(self):
        d = {"login": "u1", "password": "123"}
        key, value = d.popitem()
        self.assertEqual(
            0, len({k: v for k, v in d.items() if k == key and v == value}))
        self.assertEqual(1, len(d))

    def test_setdefault(self):
        d = {"login": "u1"}
        v = d.setdefault("password")
        self.assertEqual(d.keys(), {"login", "password"})
        self.assertEqual(v, None)

        v = d.setdefault("password", "123")
        self.assertEqual(d.keys(), {"login", "password"})
        self.assertEqual(v, None)


class OrderedDictTest(unittest.TestCase):
    pass
