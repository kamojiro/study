from fundamental_stack import Stack

def sort_stack(stack):
    max_stack = Stack()
    now = 0
    while not stack.is_empty():
        now = max(now, stack.peek())
        max_stack.push((stack.pop(), now))
    while True:
        if max_stack.is_empty():
            break
        while not max_stack.is_empty():
            if max_stack.peek()[0] == max_stack.peek()[1]:
                temp = max_stack.pop()[0]
                break
            stack.push(max_stack.pop()[0])
        if stack.is_empty():
            stack.push(temp)
            continue
        now = max_stack.peek()[1] if max_stack.peek() else 0
        while not stack.is_empty():
            if stack.peek() >=  temp:
                break
            now = max(now, stack.peek())
            max_stack.push((stack.pop(), now))
            continue
        stack.push(temp)

def test():
    stack = Stack()
    stack.push(2)
    stack.push(4)
    stack.push(7)
    stack.push(1)
    stack.push(6)
    sort_stack(stack)
    while not stack.is_empty():
        print(stack.pop())

if __name__ == '__main__':
    test()
    
