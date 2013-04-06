__author__ = 'cclamb'

class StackType:
    DynamicList, AdjustableList = range(2)

def create_stack(type):
    if type == StackType.DynamicList:
        return DynamicListStack()
    elif type == StackType.AdjustableList:
        return None
    else:
        raise NameError("unknown stack type requested")

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