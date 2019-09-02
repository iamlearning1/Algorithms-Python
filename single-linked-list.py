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

    def len(self):
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


linked_list = SingleLinkedList()
linked_list.append('Hello')
linked_list.append('World')
linked_list.append('!')
print(linked_list)
