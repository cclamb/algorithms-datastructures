__author__ = 'cclamb'

import unittest

from crystal.queue import DynamicListQueue
from crystal.queue import QueueType
from crystal.queue import create_queue


class TestQueue(unittest.TestCase):

    def test_create(self):
        self.assertIsNotNone(DynamicListQueue())

    def test_enqueue(self):
        q = DynamicListQueue()
        q.enqueue(3).enqueue(2).enqueue(1)
        self.assertEqual(3, q.dequeue())
        self.assertEqual(2, q.dequeue())

    def test_dequeue(self):
        q = DynamicListQueue()
        q.enqueue('a').enqueue('b').enqueue('c')
        self.assertEqual('a', q.dequeue())
        self.assertEqual('b', q.dequeue())

    def test_clear(self):
        q = DynamicListQueue()
        self.assertTrue(q.empty())
        q.enqueue('a').enqueue('b').enqueue('c')
        self.assertFalse(q.empty())
