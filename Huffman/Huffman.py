from Utilies.Queue import Queue
from Utilies.Node import Node

class ValueSource():
    def __init__(self, simbol, probability):
        self.probability = probability
        self.simbol = simbol



class Huffman():
    def __init__(self, source):
        self.CheckSource(source)
        self.queueForResulting = Queue()
        self.initialQueue = Queue()
        
        for s in source:
            self.initialQueue.Enqueue(Node(ValueSource(s, source[s]), None, None)) 
                
        self.initialQueue.queue.sort(key=lambda x:x.value.probability)  
    
    def CheckSource(self, source):
        if not isinstance(source, dict):
            raise ValueError("The source must be a dictionary")

        if not(all(isinstance(p, (int, float)) and 0 <= p <= 1 for p in source.values()) and sum(source.values()) == 1):
               raise ValueError("The values of the dictionary must be integer or float and the sum must be equal to 1")
        
        if not(all(isinstance(p, str) and len(p) == 1 for p in source.keys())):
               raise ValueError("The values of the dictionary must be integer or float and the sum must be equal to 1")
        
    def FindMin(self):
        if self.queueForResulting.IsEmpty():
            return self.initialQueue.Dequeue()
        
        if self.initialQueue.IsEmpty():
            return self.queueForResulting.Dequeue()
        
        if self.initialQueue.Top().value.probability < self.queueForResulting.Top().value.probability:
            return self.initialQueue.Dequeue()
        
        return self.queueForResulting.Dequeue()
    
    
    def CreateTree(self):
        
        while not (self.initialQueue.IsEmpty() and self.queueForResulting.IsSizeOne()):
            firstNode = self.FindMin()
            secondNode = self.FindMin()
            
            nodeToAdd = Node(ValueSource("$", firstNode.value.probability+secondNode.value.probability), firstNode, secondNode)
        
            self.queueForResulting.Enqueue(nodeToAdd)
        
        return self.queueForResulting.Dequeue()
    
    def Encode(self, node, table, code):
        if not node.left  and not node.right:
            table[node.value.simbol] = code
        else:
            self.Encode(node.left, table, code+"0")
            self.Encode(node.right, table, code+"1")
     
    def Apply(self):
        
        root = self.CreateTree()
        table = {}
        
        self.Encode(root,table, "")
        
        return table

            



        