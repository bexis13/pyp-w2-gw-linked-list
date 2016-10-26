# -*- coding: utf-8 -*-
import unittest

from linked_list import Node


class NodeTestCase(unittest.TestCase):

    def test_node_str_representation_without_tail(self):
        self.assertEqual(str(Node(9)), "Node(9) > /")

    def test_node_str_representation_with_tail(self):
        n = Node(9)
        n.tail = Node('X')
        self.assertEqual(str(n), "Node(9) > Node(X)")

    def test_node_equal_value(self):
        self.assertEqual(Node(1), Node(1))
        self.assertEqual(Node('hello'), Node('hello'))
        self.assertEqual(Node(True), Node(True))
        self.assertEqual(Node([1, 2, 3]), Node([1, 2, 3]))

    def test_node_not_equal_value(self):
        self.assertNotEqual(Node(1), Node(2))
        self.assertNotEqual(Node('hello'), Node('bye'))
        self.assertNotEqual(Node(True), Node(False))
        self.assertNotEqual(Node([1, 2, 3]), Node([3, 2, 1]))

    def test_node_equal_value_different_tail_node(self):
        self.assertNotEqual(Node(1, tail=Node('tail1')),
                            Node(1, tail=Node('tail2')))
        self.assertNotEqual(Node('hello', tail=Node('tail1')),
                            Node('hello', tail=Node('tail2')))
        self.assertNotEqual(Node(True, tail=Node('tail1')),
                            Node(True, tail=Node('tail2')))
        self.assertNotEqual(Node([1, 2, 3], tail=Node('tail1')),
                            Node([1, 2, 3], tail=Node('tail2')))
