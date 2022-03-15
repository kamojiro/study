from collections import deque
from fundamental_stack import Stack

class QueueByStacks:
    def __init__(self):
        self.stacks = [Stack(), Stack()]
        self.pop_at = 1
    def push(self, elem):
        self.stacks[self.pop_at^1].push(elem)
    def pop(self):
        if self.stacks[0].is_empty() and self.stacks[1].is_empty():
            raise Exception
        if self.stacks[self.pop_at].is_empty():
            other = self.pop_at^1
            while not self.stacks[other].is_empty():
                self.stacks[self.pop_at].push(self.stacks[other].pop())

        return self.stacks[self.pop_at].pop()

def test():
    queue = deque()
    queue_stack = QueueByStacks()
    A = [1, -1, 2, 3, 4, -3, -4, -2]
    for a in A:
        if a < 0:
            assert queue.pop() == queue_stack.pop()
        else:
            queue.appendleft(a)
            queue_stack.push(a)


if __name__ == '__main__':
    test()

