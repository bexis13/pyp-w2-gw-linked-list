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

    #coded this way under protest. :p Should really return chain all the way to end, and then be consistent re / at end or not...
    #but this is what the specs want. So harumph!
    def __str__(self):
        if self.tail is None:
            return 'Node({s.head}) > /'.format(s=self)
        else:
            return 'Node({s.head}) > Node({s.tail.head})'.format(s=self)

    def __eq__(self, other):
        return isinstance(other, Node) and self.head == other.head and self.tail == other.tail

    def __repr__(self):
        if self.tail is None:
            return 'Node({s.head})'.format(s=self)
        else:
            return 'Node({s.head!r}, {s.tail!r})'.format(s=self)
        