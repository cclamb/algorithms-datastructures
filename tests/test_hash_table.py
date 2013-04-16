__author__ = 'cclamb'

import unittest

from crystal.hash_table import ChainedHashTable


class TestChainedHashTable(unittest.TestCase):

    def test_create(self):
        self.assertIsNotNone(ChainedHashTable())

    def test_generate_key(self):
        h = ChainedHashTable()
        self.assertEquals(int(bytes('foo', 'utf-8')[0]), h._generate_key('foo'))
        self.assertRaises(TypeError, h._generate_key, 1)

    def test_insert_list(self):
        h = ChainedHashTable()
        h._insert_list(3)
        h._store[3].insert(4)
        x = h._store[3].search(4)
        self.assertTrue(x.key, 4)

    def test_is_slot_empty(self):
        pass