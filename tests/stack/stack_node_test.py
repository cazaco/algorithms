import unittest

from source.data_structures.stack import StackNode


class TestStackNode(unittest.TestCase):
    def test_constructor(self):
        stack_node = StackNode(element=1)
        self.assertEqual(stack_node.element, 1)
        self.assertEqual(stack_node.next, None)

    def test_set_element(self):
        stack_node = StackNode(element="abc")
        stack_node.element = 456
        self.assertEqual(stack_node.element, 456)

    def test_set_next(self):
        stack_node_1 = StackNode(element="abc")
        stack_node_2 = StackNode(element=10.7)
        stack_node_1.next = stack_node_2
        self.assertEqual(stack_node_1.next.element, 10.7)


if __name__ == "__main__":
    unittest.main()
