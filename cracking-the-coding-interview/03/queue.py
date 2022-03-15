class Queue:
    def __init__(self, elem):
        self.data = elem
        self.stack = None

    def add_stack(self, elem, stack):
        self.data

    def push(self, elem):
        if not elem:
            self.data = elem
        old_stack = Stack(self.data)
        old_stack.stack = self.stack
        self.data = elem
        self.stack = old_stack

    def pop(self):
        if not self.data:
            raise Exception
        ret = self.data
        if self.stack:
            self.data = self.stack.data
            self.stack = self.stack.stack
        else:
            self.data = None
        return ret

    def is_empty(self):
        return self.data == None

    def peek(self):
        return self.data

def test():
    stack = Stack(10)
    stack.push(2)
    print(stack.pop())
    print(stack.is_empty())
    print(stack.pop())
    stack.push(3)
    print(stack.is_empty())
    stack.push(4)
    print(stack.peek())
    stack.push(5)
    for _ in range(3):
        print(stack.pop())

test()
