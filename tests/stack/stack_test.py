import unittest

from source.data_structures.stack import Stack


class TestStack(unittest.TestCase):
    def test_top(self):
        stack = Stack().push("abc")
        self.assertEqual(stack.top(), "abc")

    def test_pop(self):
        stack = Stack().push("abc").push(1).push(10.45)
        self.assertEqual(stack.pop(), 10.45)
        self.assertEqual(stack.pop(), 1)
        self.assertEqual(stack.pop(), "abc")

    def test_empty_stack_top(self):
        stack = Stack()
        self.assertEqual(stack.top(), None)

    def test_empty_stack_pop(self):
        stack = Stack()
        self.assertEqual(stack.pop(), None)


if __name__ == "__main__":
    unittest.main()
