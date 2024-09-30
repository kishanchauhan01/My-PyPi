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
            self._tail = self._tail._next
            self._size += 1

    def insertAtPos(self, pos, val):
        if self.is_empty() or ((self._size == 1) and (pos > 1)):
            print("Either list is empty or postition is greter than 1")

        elif (self._size == 1) and (pos == 1):
            self.insertAtTail(val)

        else:
            if pos > self._size:
                print("Index out of range")
            elif pos == self._size:
                self.insertAtTail(val)

            else:
                count = 1
                thead = self._head
                while count < pos - 1:
                    count += 1
                    thead = thead._next

                temp = self._Node(val, thead._next)
                thead._next = temp
                self._size += 1

    def deleteHead(self):
        if self.is_empty():
            print("List is empty")

        elif len(self) == 1:
            self._head = None
            self._tail = None
            self._size -= 1

        else:
            self._head = self._head._next
            self._tail._next = self._head
            self._size -= 1

    def deleteTail(self):
        if self.is_empty():
            print("List is empty")

        else:
            temp = self._head
            while temp._next._next != self._head:
                temp = temp._next
            temp._next = self._head
            self._tail = temp
            self._size -= 1

    def deleteAtPos(self, pos):
        if self.is_empty():
            print("List is empty")

        elif pos > self._size:
            print("Index out of range")

        elif self._size == 1 and pos == 1:
            self.deleteHead()

        else:
            count = 1
            thead = self._head
            while count < pos - 1:
                count += 1
                thead = thead._next
            thead._next = thead._next._next
            if thead._next == self._head:
                self._tail = thead
            self._size -= 1

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

    def get_head(self):
        if self._head or self._tail == None:
            print("List is empty")
        else:
            print(self._head._element)

    def get_tail(self):
        if self._head or self._tail == None:
            print("List is empty")
        else:
            print(self._tail._element)

