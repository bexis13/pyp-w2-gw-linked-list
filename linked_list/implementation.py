from .interface import AbstractLinkedList
from .node import Node
from itertools import chain


class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """

    def __init__(self, elements=None):
        if elements is None:
            self.start = self.end = None
        else:
            it = iter(elements)
            try:
                self.start = self.end = Node(next(it))
            except StopIteration:
                self.start = self.end = None
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
        if not isinstance(index, int) or index < 0:
            raise IndexError('Expected nonnegative int, got {}'.format(index))
        if self.start is None:
            raise IndexError('Linked List is empty, no values to get')
        for i,v in enumerate(self):
            if i == index:
                return v
        else:
            raise IndexError('Linked list smaller than index')

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
        return sum(1 for v in self)
            
    __len__ = count

    def pop(self, index=None):
        if (index is not None) and ((not isinstance(index,int)) or index < 0):
            raise IndexError('expected nonnegative int or None for index, got {}'.format(index))
        elif self.start is None:
            raise IndexError('Linked list is empty, nothing to pop')
        elif self.start.tail is None and not index:
            res = self.start.head
            self.start = self.end = None
            return res
        elif index == 0:
            res = self.start.head
            self.start = self.start.tail
            return res
        elif index is None:
            for node in self.start:
                if node.tail.tail is None:
                    res = node.tail.head
                    node.tail = None
                    self.end = None
                    return res
        else:
            for i,node in enumerate(self.start):
                if i+1 == index:
                    try:
                        res = node.tail.head
                    except AttributeError:
                        raise IndexError('Linked list smaller than index')
                    if node.tail.tail is None:
                        self.end = node
                    node.tail = node.tail.tail
                    return res
            else:
                raise IndexError('Linked list smaller than index')