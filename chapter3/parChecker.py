from pythonds.stack import Stack


def par_checker_v1(symbol_string):
    s = Stack()
    balance = True
    for symbol in symbol_string:
        if symbol == '(':
            s.push(symbol)
        else:
            if s.is_empty():
                balance = False
                break
            s.pop()

    return balance and s.is_empty()


def match(open, close):
    opens = '([{'
    closers = ')]}'
    return opens.find(open) == closers.find(close)


def par_checker_v2(symbol_string):
    s = Stack()
    balance = True
    for symbol in symbol_string:
        if symbol in '([{':
            s.push(symbol)
        else:
            if s.is_empty():
                balance = False
                break
            top = s.pop()
            if not match(top, symbol):
                balance = False
                break

    return balance and s.is_empty()


if __name__ == '__main__':
    print(par_checker_v1('((()))'))
    print(par_checker_v1('(()'))

    print(par_checker_v2('{{[[()]]}}'))
    print(par_checker_v2('([})'))
