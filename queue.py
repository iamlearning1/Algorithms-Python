class Node:

    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return f'{self.val}, Next: {self.next}'


class Queue:

    def __init__(self):
        self.start = None
        self.end = None
        self.size = 0

    def __repr__(self):
        return f'Start: {self.start}\nEnd: {self.end}\nSize: {self.size}'

    def enqueue(self, val):
        node = Node(val)

        if self.size is 0:
            self.start = node
            self.end = self.start
        else:
            self.end.next = node
            self.end = node

        self.size += 1

        return self.size

    def dequeue(self):
        if self.size is 0:
            return None

        current = self.start
        self.start = self.start.next
        self.size -= 1

        if self.size is 0:
            self.start = None
            self.end = None

        return current.val


queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue)
