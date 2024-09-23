class Stack:
    def __init__(self, size):
        self._stack = []
        self._size = size
        for i in range(self._size):
            self._stack.append(0)
        self._empty = 1
        self._full = 0
        self._sp = 0

    def push(self, value):
        if self._sp == self._size:
            print("stack overflow")
            return

        else:
            self._stack[self._sp] = value
            self._sp = self._sp + 1

            if self._empty == 1:
                self._empty = 0

            if self._sp == self._size:
                self._full = 1

    def pop(self):
        if self._empty == 1:
            print("stack underflow")
            return

        else:
            self._sp = self._sp - 1
            x = self._stack[self._sp]
            self._stack[self._sp] = 0

            if self._full == 1:
                self._full = 0

            if self._sp == 0:
                self._empty == 1

            return x

    def isEmpty(self):
        if self._empty == 1:
            return True
        else:
            return False

    def peek(self):
        return self._stack[self._sp - 1]

    def printStack(self):
        print(self._stack)
        return


# python3 setup.py sdist bdist_wheel
