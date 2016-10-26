class Node(object):
    """
    Node class representing each of the linked nodes in the list.
    """
    def __iter__(self):
        here = self
        yield here
        while here.tail:
            here = here.tail
            yield here

    def __init__(self, head, tail=None):
        self.head = head
        self.tail = tail

    def __str__(self):
        if self.tail is None:
            return 'Node({s.head}) > /'.format(s=self)
        else:
            return 'Node({s.head}) > {s.tail}'.format(s=self)[:-2]

    def __eq__(self, other):
        return isinstance(other, Node) and self.head == other.head and self.tail == other.tail

    def __repr__(self):
        if self.tail is None:
            return 'Node({s.head})'.format(s=self)
        else:
            return 'Node({s.head!r}, {s.tail!r})'.format(s=self)