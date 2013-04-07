__author__ = 'cclamb'

def create_stack(type):
    if type == StackType.Dynamic:
        return DynamicListStack()
    elif type == StackType.Adjustable:
        return None
    else:
        raise NameError("unknown stack type requested")

class StackType:
    Dynamic, Adjustable = range(2)

class DynamicListStack:
    def __init__(self):
        self._list = []

    def empty(self):
        return True if (len(self._list) == 0) else False

    def push(self, o):
        self._list.insert(0, o)
        return self

    def pop(self):
        return None if (len(self._list) == 0) else self._list.pop(0)