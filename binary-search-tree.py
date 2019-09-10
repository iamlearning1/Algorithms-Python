class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f'{self.value}, \nLeft: {self.left}, \nRight: {self.right}'


class BST:

    def __init__(self):
        self.root = None

    def __repr__(self):
        return f'{self.root}'

    def insert(self, value):
        node = Node(value)

        if self.root is None:
            self.root = node
            return self

        current = self.root

        while True:
            if current.value is value:
                return None

            if value < current.value:
                if current.left is None:
                    current.left = node
                    return self
                current = current.left

            elif value > current.value:
                if current.right is None:
                    current.right = node
                    return self
                current = current.right


bst = BST()

bst.insert(10)
bst.insert(5)
bst.insert(13)
bst.insert(2)
bst.insert(7)
bst.insert(11)
bst.insert(16)

print(bst)
