import math

def CalculateFrequencyOfCharsOnAText(nameFile):
        dictionary = {}
        file = open(nameFile, "r")
        amountOfChars = 0
        for line in file:
            for char in line:
                amountOfChars = amountOfChars+1
                if not dictionary or not char in dictionary:
                    dictionary[char] = 1
                else:
                    dictionary[char] = dictionary[char]+1
        
        for key in dictionary:
            dictionary[key] = dictionary[key]/amountOfChars
        
        file.close()
        
        return dictionary

class Entropy:    
    def CalculateEntropy(self, probabilities, base = 2):
        entropyCalculated = 0
        for probability in  probabilities:
            entropyCalculated = entropyCalculated + probability*math.log(1/probability, base)
    
        return entropyCalculated
    
    def CalculateEntropyOfAText(self, nameFile):
        dictionary = CalculateFrequencyOfCharsOnAText(nameFile)
        return self.CalculateEntropy(dictionary.values())