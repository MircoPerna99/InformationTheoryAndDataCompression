from Entropy.Entropy import *
from KraftMcMillan.KraftMcMillan import *
from Huffman.Huffman import *

class Source():
    def __init__(self, probabilities, code, base=2, pathText = ""):
        if pathText :
            self.pathText = pathText
            self.CreateSourceFromText(pathText)
            self.probabilities = self.discreteSource.values()
        else:
            self.probabilities = probabilities
            
        self.code = code
        self.base = base
        self.lengths = [len(string) for string in code]
        self.CheckProbabilities()
        
    def CreateSourceFromText(self, pathText):
        self.discreteSource = CalculateFrequencyOfCharsOnAText(pathText)
    
    def CheckBase(self):
        if not(self.base > 2 and isinstance(self.base, int)):
            raise ValueError("Base must be greater than 1 and it must be a integer")
    
    def CheckProbabilities(self):
        if not(all(isinstance(p, (int, float)) and 0 <= p <= 1 for p in self.probabilities) and sum(self.probabilities) == 1):
               raise ValueError("The probabilities must be integer or float and the sum must be equal to 1")
    
    def CheckCode(self):
        if self.code and len(self.code) == len(self.probabilities):
            raise ValueError("Code and probabilities must have the same length")
                     
    def GetEntropy(self):
        return Entropy().CalculateEntropy(self.probabilities, self.base)
    
    def GetAverageCodeLength(self):
        self.CheckCode()
        return CalculateAverageCodeLength(self.probabilities,self.lengths)
    
    def GetCodeEfficiency(self):
        self.CheckCode()
        self.CheckBase()
        return CalculateCodeEfficiency(self.probabilities, self.lengths, self.base)
    
    def GetRedundacyOfACode(self):
        self.CheckCode()
        self.CheckBase()
        return CalculateRedundacyOfACode(self.probabilities, self.lengths, self.base)
    
    def ExecuteKrafMcMillan(self, amountOfSymbols = 2):
        self.CheckCode()
        return KrafMcMillan().Apply(amountOfSymbols, self.lengths)
    
    def ApplyHuffman(self):
        huffman = Huffman(self.discreteSource)
        table = huffman.Apply()
        
        file = open(self.pathText, "r")
        newFile = file.read()
        
        for code in table:
            newFile= newFile.replace(code, table[code])
            
        file.close()
        
        print(newFile)

source1 = Source([], [], pathText="Prova.txt")
source1.ApplyHuffman()


        
    