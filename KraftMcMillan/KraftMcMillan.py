from Entropy.Entropy import Entropy

class KrafMcMillan():
    def Apply(self, amountOfSymbols, codewordsLength):
        value = sum([amountOfSymbols**(-length) for length in codewordsLength])
        return value <= 1

def CalculateAverageCodeLength(probabilities, length):
    averageCodeLength = 0
    for i in range(probabilities):
        averageCodeLength += probabilities[i]*length[i]
    
    return averageCodeLength

def CalculateCodeEfficiency(probabilities,length, base=2):
    entropyValue = Entropy().CalculateEntropy(probabilities,base)
    averageCodeLength = CalculateAverageCodeLength(probabilities, length)
    return entropyValue/averageCodeLength
    
def CalculateRedundacyOfACode(probabilities,length,base=2):
    codeEfficiency = CalculateCodeEfficiency(probabilities,length,base)
    return 1-codeEfficiency

