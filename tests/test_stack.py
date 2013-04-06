__author__ = 'cclamb'

from crystal.stack import ListStack
from crystal.stack import TupleStack
from crystal.stack import StackType
from crystal.stack import create_stack

import unittest

class TestListStack(unittest.TestCase):

    def test_stack(self):
        pass

    def test_push(self):
        pass

    def test_pop(self):
        pass

    def test_empty(self):
        pass

class TestListStack(unittest.TestCase):

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
