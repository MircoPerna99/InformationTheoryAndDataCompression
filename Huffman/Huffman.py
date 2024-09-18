from Utilies.Queue import Queue
from Utilies.Node import Node

class Huffman():
    def __init__(self, source):
        self.queueForResulting = Queue()
        self.initialQueue = Queue()
        
        for s in source:
            self.initialQueue.Enqueue(Node({s : source[s]}, None, None))
            
    
    def Apply(self, source):
        return True



        