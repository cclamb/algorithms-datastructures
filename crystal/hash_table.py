__author__ = 'cclamb'


from crystal.linked_list import LinkedList
from crystal.linked_list import ListType
from crystal.linked_list import create_list


class ChainedHashTable:


    class _Record:

        def __init__(self, k, v):
            self.key = k
            self.value = v


    Length = 256


    def __init_(self):
        self._store = []
        for i in range(ChainedHashTable.Length):
            self._store[i] = None

    def insert(self, k, v):
        key = self._generate_key(k)

        if self._is_slot_empty():
            self._insert_list(key)

        record = ChainedHashTable._Record(k, v)
        self._store[key].insert(record)

        return self

    def search(self):
        pass

    def delete(self):
        pass

    def _generate_key(self, k):
        if type(k) is not str:
            raise TypeError('the submitted key is not a string')
        return bytes(k, 'utf-8')[0]


    def _insert_list(self, key):
        self._store[key] = LinkedList()

    def _is_slot_empty(self, idx):
        return self._store(idx) is None
