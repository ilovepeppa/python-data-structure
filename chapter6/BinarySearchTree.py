class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.left_child = left
        self.right_child = right
        self.parent = parent

    def has_left_child(self):
        return self.left_child

    def has_right_child(self):
        return self.right_child

    def is_left_child(self):
        return self.parent and self.parent.left_child == self

    def is_right_child(self):
        return self.parent and self.parent.right_child == self

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.left_child or self.right_child)

    def has_any_children(self):
        return self.left_child or self.right_child

    def has_both_children(self):
        return self.left_child and self.right_child

    def replace_node_data(self, key, val, left, right):
        self.key = key
        self.payload = val
        self.left_child = left
        self.right_child = right
        if self.has_left_child():
            self.left_child.parent = self
        if self.has_right_child():
            self.right_child.parent = self

    def find_successor(self):
        if self.has_right_child():
            return self.right_child.find_min()

    def find_min(self):
        current = self
        while current.has_left_child():
            current = current.left_child
        return current

    def splice_out(self):
        if self.is_leaf():
            if self.is_left_child():
                self.parent.left_child = None
            else:
                self.parent.right_child = None
        else:
            if self.is_left_child():
                if self.is_left_child():
                    self.parent.left_child = self.left_child
                else:
                    self.parent.right_child = self.left_child
                self.left_child.parent = self.parent
            else:
                if self.is_left_child():
                    self.parent.left_child = self.right_child
                else:
                    self.parent.right_child = self.right_child
                self.right_child.parent = self.parent

    def __iter__(self):
        if self:
            if self.has_left_child():
                for elem in self.left_child:
                    yield elem
            yield self.key
            if self.has_right_child():
                for elem in self.right_child:
                    yield elem


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size += 1

    def _put(self, key, val, current_node):
        if key < current_node.key:
            if current_node.has_left_child():
                self._put(key, val, current_node.left_child)
            else:
                current_node.left_child = TreeNode(key, val, parent=current_node)
        elif key > current_node.key:
            if current_node.has_right_child():
                self._put(key, val, current_node.right_child)
            else:
                current_node.right_child = TreeNode(key, val, parent=current_node)
        else:
            current_node.payload = val

    def get(self, key):
        node = self._get(key, self.root)
        return node.payload if node else None

    def _get(self, key, current_node):
        if not current_node:
            return None
        if key < current_node.key:
            return self._get(key, current_node.left_child)
        elif key > current_node.key:
            return self._get(key, current_node.right_child)
        else:
            return current_node

    def delete(self, key):
        if self.size == 0:
            raise KeyError('Error, key not in tree')
        elif self.size == 1:
            if key == self.root.key:
                self.root = None
                self.size -= 1
            else:
                raise KeyError('Error, key not in tree')
        else:
            node = self._get(key, self.root)
            if node:
                self._remove(node)
                self.size -= 1
            else:
                raise KeyError('Error, key not in tree')

    def _remove(self, node):
        if node.is_leaf():
            if node.is_left_child:
                node.parent.left_child = None
            else:
                node.parent.right_child = None
        elif node.has_both_children:
            succ = node.find_successor()
            succ.splice_out()
            node.key = succ.key
            node.payload = succ.payload
        else:
            if node.is_left_child():
                if node.has_left_child():
                    node.parent.left_child = node.left_child
                    node.left_child.parent = node.parent
                else:
                    node.parent.left_child = node.right_child
                    node.right_child.parent = node.parent
            elif node.is_right_child():
                if node.has_left_child():
                    node.parent.right_child = node.left_child
                    node.left_child.parent = node.parent
                else:
                    node.parent.right_child = node.right_child
                    node.right_child.parent = node.parent
            else:
                if node.has_left_child():
                    node.replace_node_data(node.left_child.key,
                                           node.left_child.payload,
                                           node.left_child.left_child,
                                           node.left_child.right_child)
                else:
                    node.replace_node_data(node.right_child.key,
                                           node.right_child.payload,
                                           node.right_child.left_child,
                                           node.right_child.right_child)

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        return self.get(key)


if __name__ == '__main__':
    tree = BinarySearchTree()
    tree[4] = 'd'
    tree[2] = 'b'
    tree[1] = 'a'
    tree[3] = 'c'
    tree[6] = 'f'
    tree[5] = 'e'
    tree[7] = 'g'

    for i in tree:
        print(i)
