class Node():
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

    def IsLeaf(self):
        return not self.left and not self.right