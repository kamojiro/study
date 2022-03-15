from queue import Queue

class ZooQueue:
    def __init__(self):
        self.queue = Queue()
        self.dog_queue = Queue()
        self.dog_removed_count = 0
        self.cat_queue = Queue()
        self.cat_removed_count = 0
    def enqueue(self, animal):
        self.queue.enqueue(animal)
        if animal[:3] == "dog":
            self.dog_queue.enqueue(animal)
        else:
            self.cat_queue.enqueue(animal)
    def dequeue_any(self):
        while self.cat_removed_count > 0:
            if self.queue.peek()[:3] == "cat":
                self.queue.dequeue()
                self.cat_removed_count -= 1
            else:
                break
        while self.dog_removed_count > 0:
            if self.queue.peek()[:3] == "dog":
                self.queue.dequeue()
                self.dog_removed_count -= 1
            else:
                break
        animal = self.queue.dequeue()
        if animal[:3] == "dog":
            self.dog_queue.dequeue()
        else:
            self.cat_queue.dequeue()
        return animal

    def dequeue_dog(self):
        while self.cat_removed_count > 0:
            if self.queue.peek()[:3] == "cat":
                self.queue.dequeue()
                self.cat_removed_count -= 1
            else:
                break
        while self.dog_removed_count > 0:
            if self.queue.peek()[:3] == "dog":
                self.queue.dequeue()
                self.dog_removed_count -= 1
            else:
                break
        self.dog_removed_count += 1
        return self.dog_queue.dequeue()

    def dequeue_cat(self):
        while self.cat_removed_count > 0:
            if self.queue.peek()[:3] == "cat":
                self.queue.dequeue()
                self.cat_removed_count -= 1
            else:
                break
        while self.dog_removed_count > 0:
            if self.queue.peek()[:3] == "dog":
                self.queue.dequeue()
                self.dog_removed_count -= 1
            else:
                break
        self.cat_removed_count += 1
        return self.cat_queue.dequeue()

def test():
    queue = ZooQueue()
    queue.enqueue("dog1")
    queue.enqueue("cat1")
    queue.enqueue("dog2")
    queue.enqueue("cat2")
    print(queue.dequeue_cat())
    print(queue.dequeue_dog())
    print(queue.dequeue_dog())
    print(queue.dequeue_any())
    print("-"*20)
    queue.enqueue("dog1")
    queue.enqueue("cat1")
    queue.enqueue("dog2")
    queue.enqueue("cat2")
    queue.enqueue("dog3")
    queue.enqueue("cat3")
    queue.enqueue("dog4")
    queue.enqueue("cat4")
    print(queue.dequeue_any())
    print(queue.dequeue_dog())
    print(queue.dequeue_dog())
    print(queue.dequeue_dog())
    print(queue.dequeue_any())
    print(queue.dequeue_any())
    print(queue.dequeue_any())
    print(queue.dequeue_any())
    
if __name__== '__main__':
    test()
