__author__ = 'cclamb'

from crystal.stack import ListStack
from crystal.stack import TupleStack
from crystal.stack import StackType
from crystal.stack import create_stack

import unittest

class TestListStack(unittest.TestCase):

    def test_stack(self):
        self.assertIsNotNone(ListStack())


    def test_push(self):
        s = ListStack()
        s.push(1).push(2).push(3)
        self.assertFalse(s.empty())
        o = s.pop();
        self.assertEqual(o, 3)

    def test_pop(self):
        s = ListStack()
        s.push(1).push(2).push(3)
        self.assertFalse(s.empty())
        o = s.pop();
        self.assertEqual(o, 3)

    def test_empty(self):
        s = ListStack()
        s.push(1).push(2).push(3)
        self.assertFalse(s.empty())

class TestTupleStack(unittest.TestCase):

    def test_stack(self):
        pass

    def test_push(self):
        pass

    def test_pop(self):
        pass

    def test_empty(self):
        pass

class TestCreateStack(unittest.TestCase):

    def test_stack(self):
        l_stack = create_stack(StackType.List)
        self.assertTrue(type(l_stack) is ListStack)
        t_stack = create_stack(StackType.Tuple)
        self.assertTrue(type(t_stack) is TupleStack)
