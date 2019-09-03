class Node:

    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return f'{self.val}, Next: {self.next}'


class SingleLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __repr__(self):
        return f'Head: {self.head}\nTail: {self.tail}\nLength: {self.length}'

    def __len__(self):
        return self.length

    def append(self, val):
        newNode = Node(val)
        if not self.head:
            self.head = newNode
            self.tail = self.head
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1
        return self

    def pop(self):
        if not self.head:
            return None

        current = self.head
        new_tail = current
        while current.next:
            new_tail = current
            current = current.next

        self.tail = new_tail
        self.tail.next = None
        self.length -= 1

        if self.length is 0:
            self.head = None
            self.tail = None

        return self


linked_list = SingleLinkedList()
linked_list.append('Hello')
linked_list.append('World')
linked_list.append('!')
linked_list.pop()
print(linked_list)
