class Node:

    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

    def __repr__(self):
        return f'{self.val}'
        # return f'{self.val}, Prev: {self.prev}, Next: {self.next}'


class DoubleLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __repr__(self):
        next_value = self.head
        prev_value = self.tail
        next = ''
        prev = ''

        while(next_value):
            next += f'Next: {next_value.next} '
            next_value = next_value.next

        while(prev_value):
            prev += f'Prev: {prev_value.prev} '
            prev_value = prev_value.prev

        return f'Head: {self.head}\n{next}\nPrev: {self.head.prev}\n--------\nTail: {self.tail}\n{prev}\nNext: {self.tail.next}\n--------\nLength: {self.length}'

    def __len__(self):
        return self.length

    def push(self, value):
        node = Node(value)

        if (self.length is 0):
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

        self.length += 1
        return self


doubleLinkedList = DoubleLinkedList()

doubleLinkedList.push(1)
doubleLinkedList.push(2)
doubleLinkedList.push(3)
doubleLinkedList.push(4)

print(doubleLinkedList)
