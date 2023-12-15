class Queue:
    """
    A basic class to represent a Queue. Abides by FIFO protocol.

    Attributes
    ----------
    queue : list
        Queue stored as a list object

    Methods
    -------
    isEmpty():
        Return True if queue is empty.
    enqueue(item):
        Add item to the queue
    dequeue():
        Returns next item in the queue
    size():
        Returns the size of the queue
    """
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return len(self.queue) == 0
    
    def enqueue(self, item):
        self.queue.insert(0, item)

    def dequeue(self):
        if self.isEmpty(): return None
        return self.queue.pop()
    
    def size(self):
        return len(self.queue)
    
if __name__ == '__main__':
    queue = Queue()
    queue.enqueue('Yellow')
    queue.enqueue('Red')
    queue.enqueue('Orange')
    queue.enqueue('Green')

    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())