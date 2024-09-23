class SinglyCircularLL:
    class _Node:
        slots__ = "_element", "_next"

        def __init__(self, element, next=None):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def insertAtHead(self, val):
        if self.is_empty():
            self._head = self._Node(val)
            self._head._next = self._head
            self._tail = self._head
            self._size += 1

        else:
            newNode = self._Node(val, self._head)
            newNode._next = self._head
            self._tail._next = newNode
            self._head = newNode
            self._size += 1

    def insertAtTail(self, val):
        if self.is_empty():
            print("List is empty")

        else:
            self._tail._next = self._Node(val, self._head)

    def traversse(self):
        if self.is_empty():
            print("List is empty")

        elif len(self) == 1:
            print(self._head._element, " -> Null")

        else:
            temp = self._head
            while temp._next != self._head:
                print(temp._element, "-> ", end="")
                temp = temp._next

            if temp._next == self._head:
                print(temp._element, "-> Null")
