class Node:

    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

    def __repr__(self):
        return f'Prev: {self.prev}, Node: {self.val}, Next: {self.next}'


class DoubleLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __repr__(self):
        return f'Head: {self.head}, Tail: {self.tail}, Length: {self.length}'

    def __len__(self):
        return self.length


doubleLinkedList = DoubleLinkedList()
print(doubleLinkedList)
