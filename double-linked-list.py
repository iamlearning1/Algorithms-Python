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

    def get_value(self, index):
        if (index < 0 or index >= self.length):
            return None

        if (index <= self.length / 2):
            node = self.head
            counter = 0
            while(counter < index):
                node = node.next
                counter += 1
        else:
            node = self.tail
            counter = self.length - 1
            while(counter > index):
                node = node.prev
                counter -= 1

        return node

    def set_value(self, index, value):
        node = self.get_value(index)
        if not node:
            return False

        node.val = value
        return True

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False

        if index is 0:
            return bool(self.unshift(value))

        if index is self.length:
            return bool(self.push(value))

        node = Node(value)
        current_node = self.get_value(index - 1)
        next_node = current_node.next

        node.prev = current_node
        node.next = next_node
        next_node.prev = node
        current_node.next = node

        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index > self.length:
            return False

        if index is 0:
            return self.shift()

        if index is self.length - 1:
            return self.pop()

        node = self.get_value(index)

        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None

        self.length -= 1
        return node

    def reverse(self):
        if self.length is 0:
            return None

        node = self.head
        new_head = None

        while node:
            temp = node.prev
            node.prev = node.next
            node.next = temp

            new_head = node
            node = node.prev

        return new_head.next.next


doubleLinkedList = DoubleLinkedList()

doubleLinkedList.push(1)
doubleLinkedList.push(2)
doubleLinkedList.push(3)
doubleLinkedList.push(4)
# print(doubleLinkedList.pop())
# print(doubleLinkedList.shift())
# doubleLinkedList.unshift(0)
# print(doubleLinkedList.get_value(-2))
# doubleLinkedList.set_value(2, 100)
# doubleLinkedList.insert(1, 100)
# print(doubleLinkedList.remove(2))

print(doubleLinkedList.reverse())
