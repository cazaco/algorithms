from source.constants import T


class StackNode:
    def __init__(self, element: T):
        self._element = element
        self._next = None

    @property
    def element(self) -> T:
        """
        Get node element.
        :return: T
        """
        return self._element

    @element.setter
    def element(self, element: T):
        """
        Set node element.
        :param element:
        :return: None
        """
        self._element = element

    @property
    def next(self):
        """
        Get pointer to next node.
        :return: StackNode
        """
        return self._next

    @next.setter
    def next(self, next):
        """
        Set pointer to next node
        :param next:
        :return:
        """
        self._next = next


class Stack:
    def __init__(self):
        self._head = None

    @property
    def head(self) -> StackNode:
        """
        Get head's pointer
        :return:
        """
        return self._head

    @head.setter
    def head(self, head: StackNode) -> None:
        """
        Sets stack's head.
        :param head:
        :return:
        """
        self._head = head

    def top(self) -> T:
        """
        Returns head's element.
        :return: T
        """
        return self.head.element if self.head else None

    def push(self, element: T):
        """
        Push a new element in stack and becomes the new head.
        :param element:
        :return: Stack
        """
        node = StackNode(element=element)

        if self.head:
            node.next = self.head

        self.head = node

        return self

    def pop(self) -> T:
        """
        Pops head out of stack
        :return: T
        """
        if self.head:
            element = self.head.element
            self.head = self.head.next
            return element
        return None
