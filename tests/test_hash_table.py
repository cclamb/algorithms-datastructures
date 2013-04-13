__author__ = 'cclamb'

import unittest

from crystal.hash_table import ChainedHashTable

class TestChainedHashTable(unittest.TestCase):

    def test_create(self):
        self.assertIsNotNone(ChainedHashTable())

    def test_generate_key(self):
        h = ChainedHashTable()
        self.assertEquals(bytes('foo', 'utf-8')[0], h._generate_key('foo'))
        self.assertRaises(TypeError, h._generate_key, 1)

    def test_insert_list(self):
        pass

    def test_is_slot_empty(self):
        pass