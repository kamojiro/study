class FixedMultiStack:
    def __init__(self, capacity):
        if capacity < 3:
            raise Exception
        self.n = capacity
        n = self.n
        self.stack = [None]*n
        self.begins = [0, n//3, n//3*2]
        self.ends = [n//3, n//3*2, n]
        self.now = [0, n//3, n//3*2]

    def push(self, index, elem):
        if self.now[index] == self.ends[index]:
            raise Exception
        self.stack[self.now[index]] = elem
        self.now[index] += 1

    def pop(self, index):
        if self.now[index] == self.begins[index]:
            raise Exception
        elem = self.stack[self.now[index]-1]
        self.stack[self.now[index]-1] = None
        self.now[index] -= 1
        return elem

    def peak(self, index):
        if self.now[index] == self.begins[index]:
            raise Exception
        return self.stack[self.now[index]-1]

    def is_empty(self, index):
        return self.now[index] == self.begins[index]

def test():
    multistack = FixedMultiStack(12)
    multistack.push(0, 1)
    multistack.push(0, 2)
    multistack.push(1, 3)
    multistack.push(1, 4)
    multistack.push(2, 5)
    multistack.push(2, 6)
    print(multistack.pop(0))
    print(multistack.pop(0))
    print(multistack.pop(1))
    print(multistack.pop(1))
    print(multistack.pop(2))
    print(multistack.pop(2))

test()
        
