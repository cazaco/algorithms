import unittest

from source.data_structures.queue import QueueNode


class TestQueueNode(unittest.TestCase):
    def test_constructor(self):
        node: QueueNode[str] = QueueNode(data="ABC")
        self.assertEqual(node.data, "ABC")
        self.assertEqual(node.next, None)

    def test_set_data(self):
        node: QueueNode[str] = QueueNode(data="ABC")
        node.data = 123
        self.assertEqual(node.data, 123)

    def test_set_next(self):
        node_a: QueueNode[str] = QueueNode(data="ABC")
        node_b: QueueNode[str] = QueueNode(data="DEF")
        node_a.next = node_b
        self.assertEqual(node_a.next.data, "DEF")


if __name__ == "__main__":
    unittest.main()
