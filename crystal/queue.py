__author__ = 'cclamb'


def create_queue(type):
    if type == ListType.Dynamic:
        return DynamicListQueue()
    else:
        raise NameError("unknown stack type requested")


class QueueType:
    Dynamic = range(1)


class DynamicListQueue:

    def __init__(self):
        self._list = []

    def enqueue(self, o):
        self._list.append(o)
        return self

    def dequeue(self):
        return None if (len(self._list) == 0) else self._list.pop(0)

    def empty(self):
        return True if (len(self._list) == 0) else False