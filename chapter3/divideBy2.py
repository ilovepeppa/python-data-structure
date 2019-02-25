from pythonds.stack import Stack


def divide_by2(dec_number, base):
    digits = '0123456789ABCDEF'

    stack = Stack()
    while dec_number != 0:
        rem = dec_number % base
        dec_number //= base
        stack.push(digits[rem])

    bin_string = ''
    while not stack.is_empty():
        bin_string += str(stack.pop())

    return bin_string


if __name__ == '__main__':
    print(divide_by2(25, 16))
