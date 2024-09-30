class DoublyCircularLL:
    class _Node:
        slots__ = "_element", "_next", "_prev"

        def __init__(self, element, next=None, prev=None):
            self._element = element
            self._next = next
            self._prev = prev

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
            temp = self._Node(val)
            self._head = temp
            self._tail = temp
            temp._next = temp
            temp._prev = temp
            self._size += 1

        else:
            temp = self._Node(val, self._head, self._tail)
            self._head._prev = temp
            self._tail._next = temp
            self._head = temp
            self._size += 1

    def insertAtTail(self, val):
        if self.is_empty():
            self.insertAtHead(val)

        else:
            temp = self._Node(val, self._head, self._tail)
            self._tail._next = temp
            self._head._prev = temp
            self._tail = temp
            self._size += 1

    def traverse(self):
        if self.is_empty():
            print("Linked List is empty")

        else:
            temp = self._head
            while True:
                print(temp._element, "-> ", end="")
                if temp._next == self._head:
                    print("repeate")
                    break
                temp = temp._next

    def get_head(self):
        return self._head._element

    def get_tail(self):
        return self._tail._element
