__author__ = 'cclamb'

class StackType:
    List, Tuple = range(2)

def create_stack(type):
    if type == StackType.List:
        return ListStack()
    elif type == StackType.Tuple:
        return TupleStack()
    else:
        raise NameError("unknown stack type requested")

class TupleStack:
    def __init__(self):
        self._list = []

    def empty(self):
        pass

    def push(self):
        pass

    def pop(self):
        pass

class ListStack:
    def __init__(self):
        self._list = []

    def empty(self):
        return True if (len(self._list) == 0) else False

    def push(self, o):
        self._list.insert(0, o)
        return self

    def pop(self):
        return self._list.pop(0)