from Entropy.Entropy import *
from KraftMcMillan.KraftMcMillan import *
from Huffman.Huffman import *
from SardinasPatterson.SardinasPatterson import * 

class Source():
    def __init__(self, probabilities, code, base=2, path_text = ""):
        if path_text :
            self.path_text = path_text
            self.create_source_from_text(path_text)
            self.probabilities = self.discrete_source.values()
        else:
            self.probabilities = probabilities
            
        self.code = code
        self.base = base
        self.lengths = [len(string) for string in code]
        self.check_probabilities()
        
    def create_source_from_text(self, path_text):
        self.discrete_source = calculate_frequency_of_chars_on_text(path_text)
    
    def check_base(self):
        if not(self.base > 2 and isinstance(self.base, int)):
            raise ValueError("Base must be greater than 1 and it must be a integer")
    
    def check_probabilities(self):
        if not(all(isinstance(p, (int, float)) and 0 <= p <= 1 for p in self.probabilities) and sum(self.probabilities) == 1):
               raise ValueError("The probabilities must be integer or float and the sum must be equal to 1")
    
    def check_code(self):
        if self.code and len(self.code) == len(self.probabilities):
            raise ValueError("Code and probabilities must have the same length")
                     
    def get_entropy(self):
        return Entropy().calculate_entropy(self.probabilities, self.base)
    
    def get_average_code_length(self):
        self.check_code()
        return calculate_average_code_length(self.probabilities,self.lengths)
    
    def get_code_efficiency(self):
        self.check_code()
        self.check_base()
        return calculate_code_efficiency(self.probabilities, self.lengths, self.base)
    
    def get_redundacy_of_code(self):
        self.check_code()
        self.check_base()
        return calculate_redundacy_of_code(self.probabilities, self.lengths, self.base)
    
    def execute_KrafMcMillan(self, amountOfSymbols = 2):
        self.check_code()
        return KrafMcMillan().apply(amountOfSymbols, self.lengths)
    
    def apply_huffman_encode(self):
        huffman = Huffman(self.discrete_source)
        table = huffman.apply_encode()
        print(table)
        file = open(self.path_text, "r")
        newFile = file.read()
        
        for code in table:
            newFile= newFile.replace(code, table[code])
            
        file.close()
        
        print(newFile)
        return newFile

    def apply_huffman_decode(self, message):
        huffman = Huffman(self.discrete_source)
        return huffman.ApplyDecode(message)
    

source1 = Source([], [], path_text="Prova.txt")
message = source1.apply_huffman_encode()
print(message)
print(source1.apply_huffman_decode(message))



        
    