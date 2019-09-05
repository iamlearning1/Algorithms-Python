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
        if (self.length > 0):
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
        else:
            return f'Head: {self.head} Tail: {self.tail} Length: {self.length}'

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

    def pop(self):
        if (self.length is 0):
            return None

        node = self.tail

        if (self.length is 1):
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        node.prev = None
        self.length -= 1
        return node

    def shift(self):
        if (self.length is 0):
            return None

        node = self.head

        if (self.length is 1):
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            node.next = None

        self.length -= 1
        return node

    def unshift(self, value):
        node = Node(value)

        if (self.length is 0):
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node

        self.length += 1
        return self


doubleLinkedList = DoubleLinkedList()

doubleLinkedList.push(1)
doubleLinkedList.push(2)
doubleLinkedList.push(3)
# print(doubleLinkedList.pop())
# print(doubleLinkedList.shift())
doubleLinkedList.unshift(0)

print(doubleLinkedList)
