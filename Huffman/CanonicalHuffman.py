from Huffman.Huffman import Huffman

class CanonicalHuffmanCoder():
    def __init__(self):
        self.num = []
        self.symb = []
        self.firstcode = []
        self.table = {}
        self.codebook = {}
        
    def apply(self, source):
        huffman_table = Huffman(source).apply_encode()
        # print(huffmanTable)
        self.take_size_array(huffman_table)
        self.set_arrays(huffman_table)
        self.set_FC_array()
        # print(self.num)
        # print(self.symb)
        # print(self.firstcode)
        self.create_codebook()
        print(self.codebook)
                       
    def take_size_array(self, huffman_table):
        self.size_array = 0
        for value in huffman_table.values():
            len_value = len(value)
            if(self.size_array < len_value):
                self.size_array = len_value
        
    def init_arrays(self):
        self.num = [0]*(self.size_array+1)
        self.symb = [[] for i in range(self.size_array+1)]
        self.firstcode = [0]*(self.size_array+1)
        
    def set_arrays(self, huffman_table):
        self.init_arrays()
        keys = list(huffman_table.keys())
        keys.sort()
        for key in keys:
                codeword = huffman_table[key]
                len_codeword = len(codeword)
                self.num[len_codeword] +=1
                self.symb[len_codeword].append(key)
              
    def set_FC_array(self):
        self.firstcode[self.size_array]  = 0   
        for i in  range(self.size_array-1, 0, -1):
             self.firstcode[i] = int((self.firstcode[i+1] +self.num[i+1])/2)
        self.firstcode[1]=2 
    
    def create_codebook(self):
        for iterator_list in range(len(self.symb)):
            list = self.symb[iterator_list]
            if(list):
                value_to_add = 0
                for key in list:
                    self.codebook[key] =self.define_code_word(iterator_list, value_to_add)
                    value_to_add +=1
    
    def define_code_word(self, index, value_to_add):
        value = str(bin(self.firstcode[index]+value_to_add))[2:]
        len_value = len(value)
        if(len_value< index):
            value = '0'*(index-len_value)+value
        
        return value
    
    def encode(self, text):
        output  = ""
        for char in text:
            output += self.codebook[char]
        return output
    
    def decode(self, text_encode):
        text_decode = ""
        while(text_encode != ""):
            l = 1
            v = text_encode[0:1]
            text_encode = text_encode[1:]
            while(int(v,2) < self.firstcode[l]):
                v = v+text_encode[0:1]
                text_encode = text_encode[1:]
                l+=1            
            vInt = int(v,2)

            text_decode += self.symb[l][vInt - self.firstcode[l]]
            
        return text_decode
        
        
    
source = {"A":10/100, "B": 15/100, "C": 30/100 , "D": 20/100,  "E": 25/100}

x = CanonicalHuffmanCoder()
x.apply(source)
value = x.encode('ABBCDE')
print(value)
print(x.decode(value))