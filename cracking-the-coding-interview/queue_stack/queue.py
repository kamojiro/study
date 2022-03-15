# based on https://www.geeksforgeeks.org/queue-linked-list-implementation/

# Python3 program to demonstrate linked list
# based implementation of queue
 
# A linked list (LL) node
# to store a queue entry
class Node:
     
    def __init__(self, data):
        self.data = data
        self.next = None
 
# A class to represent a queue
 
# The queue, front stores the front node
# of LL and rear stores the last node of LL
class Queue:
     
    def __init__(self):
        self.front = self.rear = None
 
    def is_empty(self):
        return self.front == None
     
    # Method to add an item to the queue
    def enqueue(self, item):
        temp = Node(item)
         
        if self.rear == None:
            self.front = self.rear = temp
            return
        # Add the new node at the end of queue
        self.rear.next = temp
        # change rear pointer
        self.rear = temp
        # rear need not to know the preceeding node
    # Method to remove an item from queue
    def dequeue(self):
         
        if self.is_empty():
            return
        temp = self.front
        self.front = temp.next
        if(self.front == None):
            self.rear = None
        return temp.data

    def peek(self):
        if self.is_empty():
            return
        return self.front.data
 
# Driver Code
if __name__== '__main__':
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.dequeue()
    q.dequeue()
    q.enqueue(30)
    q.enqueue(40)
    q.enqueue(50)
    q.dequeue()  
    print("Queue Front " + str(q.front.data))
    print("Queue Rear " + str(q.rear.data))
    
