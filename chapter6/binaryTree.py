class BinaryTree:
    def __init__(self, root):
        self.key = root
        self.left_child = None
        self.right_child = None

    def insert_left(self, node):
        if self.left_child is None:
            self.left_child = BinaryTree(node)
        else:
            t = BinaryTree(node)
            t.left_child = self.left_child
            self.left_child = t

    def insert_right(self, node):
        if self.right_child is None:
            self.right_child = BinaryTree(node)
        else:
            t = BinaryTree(node)
            t.right_child = self.right_child
            self.right_child = t

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def set_root_value(self, val):
        self.key = val

    def get_root_value(self):
        return self.key


if __name__ == '__main__':
    a = BinaryTree('a')
    a.insert_left('b')
    a.insert_right('c')

    print(a.get_root_value())
    print(a.get_left_child().get_root_value())
    print(a.get_right_child().get_root_value())
