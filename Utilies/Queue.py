class Queue():
    def __init__(self):
        self.queue = []
 
    def IsSizeOne(self):
        return len(self.queue) == 1
 
    def IsEmpty(self):
        return self.queue == []
 
    def Enqueue(self, x):
        self.queue.append(x)
 
    def Dequeue(self):
        return self.queue.pop(0)
    
    def Top(self):
        return self.queue[0]