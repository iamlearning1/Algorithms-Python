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

    def shift(self):
        if not self.head:
            return None

        current = self.head
        self.head = self.head.next
        self.length -= 1

        if self.length is 0:
            self.tail = None

        return current

    def unshift(self, val):
        node = Node(val)
        if not self.head:
            self.head = node
            self.tail = None
        else:
            node.next = self.head
            self.head = node
            self.length += 1

        return self

    def get_value(self, index):
        if index < 0 or index >= self.length:
            return False

        current = self.head
        counter = 0
        while counter < index:
            current = current.next
            counter += 1

        return current

    def set_value(self, index, val):
        node = self.get_value(index)
        if not node:
            return False

        node.val = val
        return True

    def insert(self, index, val):
        if index < 0 or index >= self.length:
            return False

        if index is 0:
            return bool(self.unshift(val))

        if index is self.length:
            return bool(self.append(val))

        node = Node(val)
        current = self.get_value(index - 1)
        currents_next = current.next
        node.next = currents_next
        current.next = node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return False

        if index is 0:
            return bool(self.shift())

        if index is self.length:
            return bool(self.pop())

        node = self.get_value(index - 1)
        value_to_be_removed = node.next
        node.next = value_to_be_removed.next
        self.length -= 1
        return value_to_be_removed

    def reverse(self):
        node = self.head

        self.head, self.tail = self.tail, self.head

        next = None
        prev = None
        counter = 0
        while counter < self.length:
            next = node.next
            node.next = prev
            prev = node
            node = next
            counter += 1
        return self


linked_list = SingleLinkedList()
linked_list.append('Hello')
linked_list.append('World')
linked_list.append('!')
linked_list.append('!')
# linked_list.pop()
# linked_list.shift()
# linked_list.unshift('Hey')
# print(linked_list.get(5))
# linked_list.set_value(-1, 'How are you')
# linked_list.insert(3, 'Hi')
# linked_list.remove(3)
print(linked_list.reverse())
