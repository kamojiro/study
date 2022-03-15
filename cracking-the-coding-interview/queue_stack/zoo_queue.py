class LinkedList:
    def __init__(self, x=None, next=None):
        self.elem = x
        self.next = next

    def push(self, x):
        if self.elem == None:
            self.elem = x
        else:
            self.elem, self.next = x, LinkedList(self.elem, self.next)

    def pop(self):
        if self.elem == None:
            return None
        else:
            ret = self.elem
            if self.next == None:
                self.elem = None
            else:
                self.elem , self.next = self.next.elem, self.next.next
            return ret

    def kth_to_last(self, index):
        if self.elem == None:
            return None
        current = self.next
        count = 1
        while current:
            count += 1
            current = current.next
        if count < index:
            return None
        return self.convert_list()[count - index]
                
    def convert_list(self):
        if self.elem == None:
            return []
        elem = self.elem
        next = self.next
        ret = []
        ret.append(elem)
        while next:
            elem, next = next.elem, next.next
            ret.append(elem)
        return ret


class ZooQueue:
    
