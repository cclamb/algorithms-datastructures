__author__ = 'cclamb'

from collections import namedtuple

def create_list(type):
    if type == ListType.LinkedList:
        return LinkedList()
    else:
        raise NameError("unknown stack type requested")

class ListType:
    LinkedList  = range(1)

class LinkedList:

    _Record = namedtuple("_Record", "previous next key")

    def __init__(self):
        self._head = None

    def search(self, key):
        x = self._head
        while(x != None and x.key != key):
            x = x.next
        return x

    def insert(self, key):
        record = self._Record(self._head, None, key)
        if (self._head != None):
            self._head.next = record
        else:
            self._head = record
        return self

    def delete(self):
        pass