from fundamental_stack import Stack

class SetOfStack:
    def __init__(self, capacity, elem=None):
        self.stack_set = [Stack(elem)]
        self.count = [1 if elem else 0]
        self.capacity = capacity

    def push(self, elem):
        if self.count[-1] == self.capacity:
            self.stack_set.append(Stack())
            self.count.append(0)
        self.stack_set[-1].push(elem)
        self.count[-1] += 1

    def pop(self):
        if self.count[-1] == 0 and len(self.count) > 1:
            self.stack_set.pop()
            self.count.pop()
        self.count[-1] -= 1
        return self.stack_set[-1].pop()

    def pop_at(self, index):
        if not self.stack_set[index].peek:
            raise Exception
        self.count[index] -= 1
        return self.stack_set[index].pop()

    def is_empty(self):
        return self.stack_set[-1].is_empty() and len(self.count) == 0

    def peek(self):
        if self.count[-1] == 0 and len(self.count) > 1:
            self.stack_set.pop()
        return self.stack_set[-1].peek()


def test():
    stack = SetOfStack(2)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.push(6)
    print(stack.pop_at(1))
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())

if __name__ == '__main__':
    test()

