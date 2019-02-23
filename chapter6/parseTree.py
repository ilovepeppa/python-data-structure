import operator
from stack import Stack
from binaryTree import BinaryTree


def build_parse_tree(fpexp):
    stack = Stack()
    node = BinaryTree(None)
    stack.push(node)
    current = node
    for s in fpexp.split(' '):
        if s == '(':
            current.insert_left(None)
            stack.push(current)
            current = current.get_left_child()
        elif s == ')':
            current = stack.pop()
        elif s in '+-*/':
            current.set_root_value(s)
            current.insert_right(None)
            stack.push(current)
            current = current.get_right_child()
        else:
            current.set_root_value(int(s))
            current = stack.pop()

    return node


def evaluate(tree):
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }

    val = tree.get_root_value()
    left_child = tree.get_left_child()
    right_child = tree.get_right_child()

    if left_child and right_child:
        return operations[val](evaluate(left_child), evaluate(right_child))
    else:
        return val


def pre_order(tree):
    if tree:
        print(tree.get_root_value())
        pre_order(tree.get_left_child())
        pre_order(tree.get_right_child())


def post_order(tree):
    if tree:
        post_order(tree.get_left_child())
        post_order(tree.get_right_child())
        print(tree.get_root_value())


def in_order(tree):
    if tree:
        in_order(tree.get_left_child())
        print(tree.get_root_value())
        in_order(tree.get_right_child())


def print_exp(tree):
    s = ''
    if tree:
        s += '(' + print_exp(tree.get_left_child())
        s += str(tree.get_root_value())
        s += print_exp(tree.get_right_child()) + ')'

    return s


if __name__ == '__main__':
    tree = build_parse_tree("( ( 10 + 5 ) * 3 )")
    # print(evaluate(tree))
    # in_order(tree)
    # in_order(tree)
    # post_order(tree)
    print(print_exp(tree))
