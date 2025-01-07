from Utilities.Queue import Queue
from Utilities.Node import Node

class ValueSource():
    def __init__(self, simbol, probability):
        self.probability = probability
        self.simbol = simbol



class Huffman():
    def __init__(self, source):
        self.check_source(source)
        self.queue_for_resulting = Queue()
        self.initial_queue = Queue()
        
        for s in source:
            self.initial_queue.enqueue(Node(ValueSource(s, source[s]), None, None)) 
                
        self.initial_queue.queue.sort(key=lambda x:x.value.probability)  
    
    def check_source(self, source):
        if not isinstance(source, dict):
            raise ValueError("The source must be a dictionary")

        if not(all(isinstance(p, (int, float)) and 0 <= p <= 1 for p in source.values()) and sum(source.values()) == 1):
               raise ValueError("The values of the dictionary must be integer or float and the sum must be equal to 1")
        
        if not(all(isinstance(p, str) and len(p) == 1 for p in source.keys())):
               raise ValueError("The values of the dictionary must be integer or float and the sum must be equal to 1")
        
    def find_min(self):
        if self.queue_for_resulting.is_empty():
            return self.initial_queue.dequeue()
        
        if self.initial_queue.is_empty():
            return self.queue_for_resulting.dequeue()
        
        if self.initial_queue.top().value.probability < self.queue_for_resulting.top().value.probability:
            return self.initial_queue.dequeue()
        
        return self.queue_for_resulting.dequeue()
    
    
    def create_tree(self):
        
        while not (self.initial_queue.is_empty() and self.queue_for_resulting.is_size_one()):
            firstNode = self.find_min()
            secondNode = self.find_min()
            
            nodeToAdd = Node(ValueSource("$", firstNode.value.probability+secondNode.value.probability), firstNode, secondNode)
        
            self.queue_for_resulting.enqueue(nodeToAdd)
        
        return self.queue_for_resulting.dequeue()
    
    def encode(self, node, table, code):
        if not node.left  and not node.right:
            table[node.value.simbol] = code
        else:
            self.encode(node.left, table, code+"0")
            self.encode(node.right, table, code+"1")
            
    def is_leaf(self, node):
        return not node.left  and not node.right
    
    def choose_next_node(self, node, value):
        if(value == '0'):
            return node.left
        else:
            return node.right
    
    def decode(self, message, root):
        node_to_analize = root
        decoded_message = ""
        
        i = 0
        while(i < len(message)):
            if self.is_leaf(node_to_analize):
                decoded_message = decoded_message + node_to_analize.value.simbol
                node_to_analize = root
            else:
                node_to_analize = self.choose_next_node(node_to_analize, message[i])
                i+=1
            
        return decoded_message
            
            
    def apply_encode(self):
        
        root = self.create_tree()
        table = {}
        
        self.encode(root,table, "")
        
        return table
    
    def apply_decode(self, message):
        root = self.create_tree()
        return self.decode(message, root)
    

            



        