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

    def search(self):
        self._head = None

    def insert(self, key):
        record = self._Record(self._head, None, key)
        if (self._head != None):
            self._head.next = record

    def delete(self):
        pass