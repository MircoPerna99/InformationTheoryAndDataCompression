from Huffman.Huffman import Huffman

class CanonicalHuffmanCoder():
    def __init__(self):
        self.num = []
        self.symb = []
        self.firstcode = []
        self.table = {}
        self.codebook = {}
        
    def Apply(self, source):
        huffmanTable = Huffman(source).ApplyEncode()
        print(huffmanTable)
        self.TakeSizeArray(huffmanTable)
        self.SetArrays(huffmanTable)
        self.SetFcArray()
        print(self.num)
        print(self.symb)
        print(self.firstcode)
        self.CreateCodebook()
        print(self.codebook)
                       
    def TakeSizeArray(self, huffmanTable):
        self.sizeArray = 0
        for value in huffmanTable.values():
            lenValue = len(value)
            if(self.sizeArray < lenValue):
                self.sizeArray = lenValue
        
    def InitArrays(self):
        self.num = [0]*(self.sizeArray+1)
        self.symb = [[] for i in range(self.sizeArray+1)]
        self.firstcode = [0]*(self.sizeArray+1)
        
    def SetArrays(self, huffmanTable):
        self.InitArrays()
        lastLen = 0
        keys = list(huffmanTable.keys())
        keys.sort()
        for key in keys:
                codeword = huffmanTable[key]
                lenCodeword = len(codeword)
                self.num[lenCodeword] +=1
                self.symb[lenCodeword].append(key)
              
    def SetFcArray(self):
        self.firstcode[self.sizeArray]  = 0   
        for i in  range(self.sizeArray-1, 0, -1):
             self.firstcode[i] = int((self.firstcode[i+1] +self.num[i+1])/2)
        self.firstcode[1]=2 
    
    def CreateCodebook(self):
        for iteratorList in range(len(self.symb)):
            list = self.symb[iteratorList]
            if(list):
                valueToAdd = 0
                for key in list:
                    self.codebook[key] =self.DefineCodeWord(iteratorList, valueToAdd)
                    valueToAdd +=1
    
    def DefineCodeWord(self, index, valueToAdd):
        value = str(bin(self.firstcode[index]+valueToAdd))[2:]
        lenValue = len(value)
        if(lenValue< index):
            value = '0'*(index-lenValue)+value
        
        return value
    
    def Encode(self, text):
        output  = ""
        for char in text:
            output += self.codebook[char]
        return output
    
    def Decode(self, textEncode):
        textDecode = ""
        while(textEncode != ""):
            l = 1
            v = textEncode[0:1]
            textEncode = textEncode[1:]
            while(int(v,2) < self.firstcode[l]):
                v = v+textEncode[0:1]
                textEncode = textEncode[1:]
                l+=1
                # print(int(v,2))
            
            vInt = int(v,2)

            textDecode += self.symb[l][vInt - self.firstcode[l]]
            
        return textDecode
        
        
    
source = {"A":10/100, "B": 15/100, "C": 30/100 , "D": 20/100,  "E": 25/100}

x = CanonicalHuffmanCoder()
x.Apply(source)
value = x.Encode('ABBCDE')
print(value)
print(x.Decode(value))