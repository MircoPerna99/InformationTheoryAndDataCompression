import math

class Entropy:    
    def __init__(self, probabilities):
        self.probabilities = probabilities
        self.entropyValue = self.CalculateEntropy()
        
    def CalculateEntropy(self):
        entropyCalculated = 0
        for probability in  self.probabilities:
            entropyCalculated = entropyCalculated + probability*math.log2(1/probability)
    
        return entropyCalculated
        

prova = Entropy([1/3,1/3,1/3])

print(prova.entropyValue)