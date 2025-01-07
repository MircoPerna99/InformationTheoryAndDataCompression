class NodeLZ78():
    def __init__(self, value, char):
        self.value = value
        self.char = char
        self.children = []

    def is_leaf(self):
        return not self.children
    
    def define_next_node_from_char(self, char):
        for node in self.children:
            if node.char == char:
                return node

        return None
    
    
    def add_node(self, new_node):
        self.children.append(new_node)
        
        
class LZ78Coder():
    def __init__(self):
        self.tree = NodeLZ78(0, '')
        self.table = {0:None}
        
    def encode(self, message):
        see_tree = self.tree
        i = 0
        next_value = 1
        string_encode = ""
        output = []
        while (i < len(message)):
            next_node = see_tree.define_next_node_from_char(message[i])
            if(not next_node):
                see_tree.add_node(NodeLZ78(next_value,message[i]))
                string_encode = string_encode + message[i]
                self.table[next_value]= string_encode
                next_value += 1
                output.append({see_tree.value:message[i]})
                see_tree = self.tree
                string_encode = ""
            else:
                see_tree = next_node
                string_encode = string_encode + message[i]
            
            i+=1
            
        return output
    
    def decode(self, message_decode):
        output = ""
        value_to_insert = 1
        for item in message_decode:
            key = next(iter(item))
            value_to_add = ""
            if( self.table[key]):
                value_to_add = self.table[key] + item[key]
            else:
                value_to_add =  item[key]
    
            output = output + value_to_add 
            self.table[value_to_insert] = value_to_add
            value_to_insert += 1
        
        return output