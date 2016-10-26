from .interface import AbstractLinkedList
from .node import Node
from itertools import chain


class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """

    def __init__(self, elements=None):
        if elements is None:
            self.start = None
            self.end = None
        else:
            it = iter(elements)
            self.start = self.end = Node(next(it,None))
            for v in it:
                self.end.tail = Node(v)
                self.end = self.end.tail

    def __str__(self):
        if self.start is None:
            return '[]'
        else:
            return '[{}]'.format(', '.join(str(s) for s in self))

    def __iter__(self):
        if self.start is not None:
            for node in self.start:
                yield node.head

    def __getitem__(self, index):
        pass

    def __add__(self, other):
        return LinkedList(chain(self, other))

    def __iadd__(self, other):
        if self.start is None:
            self.start = other.start
            self.end = other.end
        else:
            self.end.tail = other.start
            self.end = other.end
        return self

    def __eq__(self, other):
        return isinstance(other,LinkedList) and self.start == other.start
    
    def __ne__(self, other):
        return not self == other

    def append(self, elem):
        if self.start is None:
            self.start = self.end = Node(elem)
        else:
            self.end.tail = Node(elem)
            self.end = self.end.tail
    
    def count(self):
        if self.start is None:
            return 0
        else:
            return sum(1 for node in self.start)
            
    __len__ = count

    def pop(self, index=None):
        pass