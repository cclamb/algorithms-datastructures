__author__ = 'cclamb'

from crystal.stack import Stack
import unittest

class InternalStack:
    def __init__(self):
        print("created")

    def print(self):
        print("from internalstack!")

class StackTest(unittest.TestCase):
    def test_creation(self):
        self.assertIsNotNone(InternalStack())

    def test_printer(self):
        stack = InternalStack()
        stack.print()

    def test_stack(self):
        self.assertIsNotNone(Stack())
