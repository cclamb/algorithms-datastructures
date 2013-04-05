__author__ = 'cclamb'


import unittest
from crystal import Stack


class StackTest(unittest.TestCase):
    def test_creation(self):
        self.assertIsNotNone(Stack())