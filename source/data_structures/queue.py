from typing import TypeVar, Generic, Optional

T = TypeVar("T")


class QueueNode(Generic[T]):
    def __init__(self, data: T):
        self._data = data
        self._next = None

    @property
    def data(self):
        """

        :return:
        """
        return self._data

    @data.setter
    def data(self, data: T):
        """

        :param data:
        :return:
        """
        self._data = data

    @property
    def next(self):
        """

        :return:
        """
        return self._next

    @next.setter
    def next(self, next):
        """

        :param next:
        :return:
        """
        self._next = next


class Queue(Generic[T]):
    def __init__(self):
        self._head = None
        self._tail = None

    @property
    def head(self) -> QueueNode[T]:
        """

        :return:
        """
        return self._head

    @head.setter
    def head(self, head: QueueNode[T]) -> None:
        """

        :param head:
        :return:
        """
        self._head = head

    @property
    def tail(self) -> QueueNode[T]:
        """

        :return:
        """
        return self._tail

    @tail.setter
    def tail(self, tail: QueueNode[T]) -> None:
        """

        :param tail:
        :return:
        """
        self._tail = tail

    def enqueue(self, data: T) -> None:
        """

        :param data:
        :return:
        """
        node: QueueNode[T] = QueueNode(data=data)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def dequeue(self) -> Optional[T]:
        """

        :return:
        """
        if self.head:
            data = self.head.data
            self.head = self.head.next
            return data
        return None

    def is_empty(self) -> bool:
        """

        :return:
        """
        return self.head is None
