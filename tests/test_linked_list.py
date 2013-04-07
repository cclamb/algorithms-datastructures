__author__ = 'cclamb'

import unittest

from crystal.linked_list import LinkedList
from crystal.linked_list import ListType
from crystal.linked_list import create_list

class TestLinkedList(unittest.TestCase):

    def test_create(self):
        self.assertIsNotNone(LinkedList())

    def test_insert(self):
        l = LinkedList()
        l.insert(1).insert(2).insert(3)

    def test_search(self):
        l = LinkedList()
        l.insert(1).insert(2).insert(3)
        r = l.search(2)
        self.assertEqual(2, r.key)
        r = l.search(1)
        self.assertEqual(1, r.key)
        r = l.search(3)
        self.assertEqual(3, r.key)

    def test_delete(self):
        l = LinkedList()
        l.insert(1).insert(2).insert(3)
        l.delete(2)
        self.assertEqual(None, l.search(2))
        self.assertEqual(1, l.search(1).key)
        self.assertEqual(3, l.search(3).key)

class TestCreateList(unittest.TestCase):

    def test_create_list(self):
        l_stack = create_list(ListType.LinkedList)
        self.assertTrue(type(l_stack) is LinkedList)

    def test_stack_bad_type(self):
        self.assertRaises(NameError, create_list, 10)
