class Queue():
    def __init__(self):
        self.queue = []
 
    def is_size_one(self):
        return len(self.queue) == 1
 
    def is_empty(self):
        return self.queue == []
 
    def enqueue(self, x):
        self.queue.append(x)
 
    def dequeue(self):
        return self.queue.pop(0)
    
    def top(self):
        return self.queue[0]