class SinglyLL:
    class _Node:
        __slots__ = "_element", "_next"

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

    def traverse(self):
        if self.is_empty():
            print("Linked List is empty")
            return None

        else:
            temp = self._head
            while True:
                print(temp._element, "-> ", end="")
                if temp._next == None:
                    print("NULL")
                    break

                temp = temp._next

    def insertAtHead(self, d):
        if self.is_empty():
            self._head = self._Node(d, None)
            self._tail = self._head
            self._size += 1

        elif len(self) == 1:
            temp = self._head
            self._head = self._Node(d, temp)
            self._tail = temp
            self._size += 1

        else:
            self._head = self._Node(d, self._head)
            self._size += 1

        return

    def insertAtTail(self, d):
        if self.is_empty():
            self._head = self._Node(d, None)
            self._tail = self._head
            self._size += 1

        else:
            self._tail._next = self._Node(d, None)
            self._tail = self._tail._next
            self._size += 1

        return

    def insertAtPos(self, d, pos):
        if self.is_empty():
            self.insertAtHead(d)
            return

        elif pos > len(self):
            print("Position out of range")
            return

        else:
            temp = self._head
            count = 1
            while count < pos - 1:
                temp = temp._next
                count += 1

            if temp._next == None:
                self.insertAtTail(d)
                return

            nodeToInsert = self._Node(d, None)
            nodeToInsert._next = temp._next
            temp._next = nodeToInsert

    def deleteHead(self):
        if self.is_empty():
            print("List is empty")
            return
        else:
            self._head = self._head._next
            self._size -= 1
            return

    def deleteTail(self):
        if self.is_empty():
            print("List is empty")
            return

        else:
            if self._head._next == None or self._head == None:
                self._head = self._head._next
                self._tail = self._head
                self._size -= 1
                return
            else:
                temp = self._head
                while temp._next._next != None:
                    temp = temp._next

                temp._next = None
                self._tail = temp
                self._size -= 1
                return

    def deleteAtPosition(self, pos):
        if self.is_empty():
            print("LL is empty")
            return

        if pos > len(self):
            print("Postion out of index")

        else:
            count = 1
            temp = self._head
            while count < pos - 1:
                temp = temp._next
                count += 1

            if temp._next == None:
                self.deleteTail()

            else:
                nextTonextNode = temp._next._next
                temp._next._next = None
                temp._next = nextTonextNode
            return

    def deleteBefore(self, val):
        if self.is_empty():
            print("LL is empty")

        temp = self._head
        while temp._next._element != val:
            temp = temp._next

        if temp._next == None:
            self.deleteTail()

    def insertAfter(self, val, d):
        if self.is_empty():
            print("LL is empty")
            return

        temp = self._head
        while temp._element != val:
            temp = temp._next
            if temp == None:
                break

        if temp == None:
            print("value is not found LL")
            return

        else:
            nextNode = temp._next
            temp._next = self._Node(d, nextNode)
        return

    def insertBefore(self, val, d):
        if self.is_empty():
            print("LL is empty")
            return

        temp = self._head
        if val == self.get_head():
            self.insertAtHead(d)

        else:
            while temp._next._element != val:
                temp = temp._next
                if temp._next == None:
                    break

            if temp._next == None:
                print("value is not found in LL")
                return

            else:
                nextNode = temp._next
                temp._next = self._Node(d, nextNode)
        return

    def mergeTwoLL(self, l1, l2):
        if l1.is_empty():
            self._head = l2._head
            self._tail = l2._tail
            self._size = l2._size
            return

        if l2.is_empty():
            self._head = l1._head
            self._tail = l1._tail
            self._size = l1._size
            return

        l1._tail._next = l2._head
        self._head = l1._head
        self._tail = l2._tail
        self._size = l1._size + l2._size

    def get_tail(self):
        # print(self._tail._element)
        return self._tail._element

    def get_head(self):
        # print(self._head._element)
        return self._head._element
