class NodeLZ78():
    def __init__(self, value, char):
        self.value = value
        self.char = char
        self.children = []

    def IsLeaf(self):
        return not self.children
    
    def DefineNextNodeFromChar(self, char):
        for node in self.children:
            if node.char == char:
                return node

        return None
    
    
    def AddNode(self, newNode):
        self.children.append(newNode)
        
        
class LZ78Coder():
    def __init__(self):
        self.tree = NodeLZ78(0, '')
        self.table = {0:None}
        
    def Encode(self, message):
        seeTree = self.tree
        i = 0
        nextValue = 1
        stringEncode = ""
        output = []
        while (i < len(message)):
            nextNode = seeTree.DefineNextNodeFromChar(message[i])
            if(not nextNode):
                seeTree.AddNode(NodeLZ78(nextValue,message[i]))
                stringEncode = stringEncode + message[i]
                self.table[nextValue]= stringEncode
                nextValue += 1
                output.append({seeTree.value:message[i]})
                seeTree = self.tree
                stringEncode = ""
            else:
                seeTree = nextNode
                stringEncode = stringEncode + message[i]
            
            i+=1
            
        return output
    
    def Decode(self, messageDecode):
        output = ""
        valueToInsert = 1
        for item in messageDecode:
            key = next(iter(item))
            valueToAdd = ""
            if( self.table[key]):
                valueToAdd = self.table[key] + item[key]
            else:
                valueToAdd =  item[key]
    
            output = output + valueToAdd 
            self.table[valueToInsert] = valueToAdd
            valueToInsert += 1
        
        return output