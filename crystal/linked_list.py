from pdb import _rstr

__author__ = 'cclamb'


def create_list(type):
    if type == ListType.LinkedList:
        return LinkedList()
    else:
        raise NameError("unknown stack type requested")


class ListType:
    LinkedList = range(1)


class _Record:

    def __init__(self, prev=None, next=None, key=None):
        self.prev = prev
        self.next = next
        self.key = key


class LinkedList:

    def __init__(self):
        self._head = None

    def search(self, key):
        x = self._head
        while x is not None and x.key != key:
            x = x.next
        return x

    def insert(self, key):
        record = _Record(self._head, None, key)
        x = self._head

        if x is None:
            self._head = record
            return self

        while x.next is not None:
            x = x.next

        x.next = record
        return self

    def delete(self, key):
        if self._head is None:
            return self
        x = self._head
        while x is not None and x.key != key:
            x = x.next
        prev_record = x.prev
        next_record = x.next
        prev_record.next = next_record
        return self