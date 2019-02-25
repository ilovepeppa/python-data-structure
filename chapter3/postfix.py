import operator
from pythonds.stack import Stack


def infix_to_postfix(infixexpr):
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1
    }

    postfixexpr = ''
    op_stack = Stack()

    for token in infixexpr:
        if token in 'ABCDEFGHIJKLMNOPQRSTUWXYZ' or token in '0123456789':
            postfixexpr += token
        elif token == '(':
            op_stack.push(token)
        elif token == ')':
            while not op_stack.is_empty():
                op = op_stack.pop()
                if op == '(':
                    break
                postfixexpr += op
        else:
            while not op_stack.is_empty():
                op = op_stack.peek()
                if prec[op] >= prec[token]:
                    postfixexpr += op_stack.pop()
                else:
                    break
            op_stack.push(token)

    while not op_stack.is_empty():
        postfixexpr += op_stack.pop()

    return postfixexpr


def postfix_eval(postfixexpr):
    operate = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }
    operand_stack = Stack()
    for token in postfixexpr:
        if token in '+-*/':
            b = int(operand_stack.pop())
            a = int(operand_stack.pop())
            operand_stack.push(operate[token](a, b))
        else:
            operand_stack.push(token)

    return operand_stack.pop()


print(infix_to_postfix('A*B+C*D'))
print(infix_to_postfix('(A+B)*C-(D-E)*(F+G)'))

print(postfix_eval('78+32+/'))
