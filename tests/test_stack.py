__author__ = 'cclamb'

from crystal.stack import DynamicListStack
from crystal.stack import StackType
from crystal.stack import create_stack

import unittest

class TestListStack(unittest.TestCase):

    def test_stack(self):
        self.assertIsNotNone(DynamicListStack())


    def test_push(self):
        s = DynamicListStack()
        s.push(1).push(2).push(3)
        self.assertFalse(s.empty())
        o = s.pop();
        self.assertEqual(o, 3)

    def test_pop(self):
        s = DynamicListStack()
        s.push(1).push(2).push(3)
        self.assertFalse(s.empty())
        o = s.pop();
        self.assertEqual(o, 3)

    def test_empty(self):
        s = DynamicListStack()
        s.push(1).push(2).push(3)
        self.assertFalse(s.empty())

    def test_blow_stack(self):
        s = DynamicListStack()
        self.assertIsNone(s.pop())

class TestCreateStack(unittest.TestCase):

    def test_stack(self):
        l_stack = create_stack(StackType.DynamicList)
        self.assertTrue(type(l_stack) is DynamicListStack)

    def test_stack_bad_type(self):
        self.assertRaises(NameError, create_stack, 10)
