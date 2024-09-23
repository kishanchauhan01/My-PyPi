class DoublyLL:
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
            self._size += 1

        else:
            temp = self._Node(val, self._head)
            self._head._prev = temp
            self._head = temp
            self._size += 1

    def insertAtTail(self, val):
        if self.is_empty():
            self.insertAtHead(val)
            return

        else:
            temp = self._Node(val, None, self._tail)
            self._tail._next = temp
            self._tail = temp
            self._size += 1

    def insertAtPosition(self, val, pos):
        if self.is_empty():
            print("Linked list is empth")
            return

        elif pos == 1:
            self.insertAtHead(val)
            return

        else:
            count = 1
            temp = self._head
            while count < pos - 1:
                temp = temp._next
                count += 1

            if temp._next == None:
                self.insertAtTail(val)
                return
            else:
                temp._next = self._Node(val, temp._next, temp)
                temp._next._next._prev = temp._next
                self._size += 1

    def insertAfter(self, aval, val):
        if self.is_empty():
            print("List is empty")

        else:
            temp = self._head
            while temp._element != aval:
                temp = temp._next
                if temp == None:
                    break

            if temp == None:
                print("Value not found")

            elif temp._next == None:
                self.insertAtTail(val)

            else:
                temp._next = self._Node(val, temp._next, temp)
                temp._next._next._prev = temp._next
                self._size += 1

    def insertBefore(self, bval, val):
        if self.is_empty():
            print("List is empty")

        elif self._head._element == bval:
            self.insertAtHead(val)

        else:
            temp = self._head
            while temp._next._element != bval:
                temp = temp._next
                if temp._next == None:
                    break

            if temp._next == None:
                print("value not found")

            else:
                temp._next = self._Node(val, temp._next, temp)
                temp._next._next._prev = temp._next
                self._size += 1

    def deleteHead(self):
        if self.is_empty():
            print("List is empty")

        else:
            if len(self) == 1:
                self._tail = None
                self._head = None
                self._size -= 1
                print("Now list is empty")
            else:
                self._head = self._head._next
                self._head._prev = None
                self._size -= 1

    def deleteTail(self):
        if self.is_empty():
            print("List is empty")

        else:
            if len(self) == 1:
                self._tail = None
                self._head = None
                self._size -= 1
                print("Now list is empty")
                
            else:
                self._tail = self._tail._prev
                self._tail._next = None
                self._size -= 1

    def deleteAtPos(self, pos):
        if self.is_empty():
            print("List is empty")

        elif pos == 1:
            self.deleteHead()
            return

        else:
            count = 1
            temp = self._head
            while count < pos - 1:  # 1 2 3
                temp = temp._next
                count += 1

            if temp._next._next == None:
                self.deleteTail()
                return

            else:
                temp._next = temp._next._next
                temp._next._prev = temp
                self._size -= 1

        return

    def deleteBefore(self, val):
        if self.is_empty():
            print("List is empty")

        elif self._head._element == val:
            print("can't delete the element before the head ")

        else:
            temp = self._head
            while temp._next._element != val:
                temp = temp._next
                if temp._next == None:
                    break

            if temp._next == None:
                print("value not found")

            else:
                temp._prev._next = temp._next
                temp._next._prev = temp._prev
                self._size -= 1
        return

    def deleteAfter(self, val):
        if self.is_empty():
            print("List is empty")

        else:
            temp = self._head
            while temp._element != val:
                temp = temp._next
                if temp == None:
                    break

            if temp == None:
                print("value not found")

            elif temp == self._tail:
                print("Value is at last postion so can't delete it's after value")

            elif temp._next == self._tail:
                self.deleteTail()

            else:
                temp._next = temp._next._next
                temp._next._prev = temp
                self._size -= 1

        return

    def traverse(self):
        if self.is_empty():
            print("Linked List is empty")
            return
        else:
            temp = self._head
            while True:
                print(temp._element, "-> ", end="")
                if temp._next == None:
                    print("Null")
                    break

                temp = temp._next

    def reverseTraverse(self):
        if self.is_empty():
            print("Linked List is empty")
            return
        else:
            temp = self._tail
            while True:
                print(temp._element, "-> ", end="")
                if temp._prev == None:
                    print("NUll")
                    break
                temp = temp._prev

    def get_tail(self):
        return self._tail._element

    def get_head(self):
        return self._head._element
