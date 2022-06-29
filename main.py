DEBUG = True
CODE = 'some code 123@12345@12345>@@>@'


# Stack class

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return not self.items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            return None

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return '<' + str(self.items)[1:-1] + '>'


def is_true(popped):
    # number is true iff > 0
    # string is true iff != ' '*len(string)
    # boolean is true iff != False
    # list is true if all elements are true
    if popped is not None:
        popped_type = type(popped)
        if popped_type is int:
            if popped > 0:
                return 1
        if popped_type is str:
            if popped != ' ' * len(popped):
                return 1
        if popped_type is bool:
            if popped:
                return 1
        if popped_type is list:
            return all([is_true(item) for item in popped])


stack = Stack()
pointer = 0

while pointer < len(CODE):
    character = CODE[pointer]

    if DEBUG:
        print('Pointer:', pointer)
        print('Character:', character)
        print('Stack:', stack)
        print('\n')

    if character in '>':
        # SKIP NEXT COMMAND IF pop() IS TRUE
        if is_true(stack.pop()):
            pointer += 1

    if character in '@':
        # PUSH 0
        stack.push(0)

    if character in '1234567890':
        popped = stack.pop()
        popped_type = type(popped)
        if popped is not None:
            if popped_type is int:
                # if popped is num, push num*10+character
                stack.push(popped * 10 + int(character))
            if popped_type is str:
                # if popped is str, push popped*character
                # if char is '1', treat it as 10, if char is '0',
                #                                 push original string and string ''
                if character == '0': stack.push(popped)
                stack.push(popped * int(character if character != '1' else 10))
            if popped_type is bool:
                # if popped is bool, push bool that many times
                # if char is '0', push False, if char is '1', push True
                if character == '0':
                    stack.push(False)
                if character == '1':
                    stack.push(True)
                else:
                    for _ in range(int(character)):
                        stack.push(popped)
            if popped_type is list:
                # if popped is list, push popped*character
                # if char is '1', treat it as 10, if char is '0',
                #                                 push original list and list []
                if character == '0': stack.push(popped)
                stack.push(popped * int(character if character != '1' else 10))
        else:
            # if popped is None, push character
            stack.push(int(character))

    if character in '#':
        # PUSH ''
        stack.push('')

    if character in 'qwertyuiopasdfghjklzxcvbnm QWERTYUIOPASDFGHJKLZXCVBNM:;\'",.()!':
        popped = stack.pop()
        popped_type = type(popped)
        if popped is not None:
            if popped_type is int:
                # if popped is num, push popped and push ord(character)
                stack.push(popped)
                stack.push(ord(character))
            if popped_type is str:
                # if popped is str, push popped + character
                stack.push(popped + character)
            if popped_type is bool:
                # if popped is bool, push character if true, else push ''
                if popped:
                    stack.push(character)
                else:
                    stack.push('')
            if popped_type is list:
                pass  # Work in progress
        else:
            stack.push(character)

    pointer += 1

if DEBUG:
    print('Pointer:', pointer)
    print('Character:', 'NONE')
    print('Stack:', stack)
    print('\n')

