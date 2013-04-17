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
        h._store[3].insert(0, 4)
        x = h._store[3][0]
        self.assertTrue(x, 4)

    def test_is_slot_empty(self):
        h = ChainedHashTable()
        self.assertTrue(h._is_slot_empty(3))
        h._insert_list(3)
        self.assertFalse(h._is_slot_empty(3))

    def test_search(self):
        h = ChainedHashTable()
        h.insert('foo', 1).insert('bar', 2)
        self.assertEqual(1, h.search('foo'))
        self.assertEqual(2, h.search('bar'))
        self.assertIsNone(h.search('blech'))

    def test_delete(self):
        h = ChainedHashTable()
        h.insert('foo', 1)
        self.assertEqual(1, h.search('foo'))
        h.delete('bar')
        h.delete('foo')
        self.assertIsNone(h.search('foo'))