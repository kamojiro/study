from fundamental_stack import Stack

class MinStack:
    def __init__(self, elem=None):
        self.stack = Stack(elem)
        self.min_stack = Stack(elem)

    def push(self, elem):
        if self.stack.peek():
            self.min_stack.push(min(elem, self.min_stack.peek()))
        else:
            self.min_stack.push(elem)
        self.stack.push(elem)

    def pop(self):
        self.min_stack.pop()
        return self.stack.pop()

    def min(self):
        return self.min_stack.peek()

    def peek(self):
        return self.stack.peek()

def test():
    stack = MinStack()
    stack.push(10)
    stack.push(2)
    print(stack.min())
    print(stack.pop())
    stack.push(3)
    print(stack.min())
    stack.push(1)
    print(stack.min())
    stack.pop()
    print(stack.min())

if __name__ == '__main__':
    test()


