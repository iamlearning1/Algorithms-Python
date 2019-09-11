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

    def search(self, value):
        if not self.root:
            return False

        current = self.root
        found = False

        while not found and current:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                return True

        return False

    def BFS(self):
        queue = []
        data = []
        node = self.root

        queue.append(node)
        while len(queue) is not 0:
            node = queue.pop(0)
            data.append(node.value)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        return data

    def DFS_pre_order(self):
        queue = []

        def traverse(node):
            queue.append(node.value)

            if node.left:
                traverse(node.left)

            if node.right:
                traverse(node.right)

        traverse(self.root)
        return queue


bst = BST()

bst.insert(10)
bst.insert(5)
bst.insert(13)
bst.insert(2)
bst.insert(7)
bst.insert(11)
bst.insert(16)

# print(bst.search(10))

# print(bst.BFS())
print(bst.DFS_pre_order())

'''
                        10
                  5           13
              2       7   11      16
'''
