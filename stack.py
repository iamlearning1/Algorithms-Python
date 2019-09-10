class Node:

    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return f'{self.val}, Next: {self.next}'


class Stack:

    def __init__(self):
        self.start = None
        self.end = None
        self.size = 0

    def __repr__(self):
        return f'Start: {self.start}\nEnd: {self.end}\nSize: {self.size}'

    def push(self, val):
        node = Node(val)

        if self.size is 0:
            self.start = node
            self.end = self.start
        else:
            node.next = self.start
            self.start = node

        self.size += 1

        return self.size

    def pop(self):
        if self.size is 0:
            return None

        current = self.start
        self.start = self.start.next
        self.size -= 1

        if self.size is 0:
            self.start = None
            self.end = None

        return current.val


stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())

stack.push(1)
stack.push(2)
stack.push(3)

print(stack)
