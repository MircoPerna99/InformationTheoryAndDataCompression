import math

class Entropy:    
    def CalculateEntropy(self, probabilities):
        entropyCalculated = 0
        for probability in  probabilities:
            entropyCalculated = entropyCalculated + probability*math.log2(1/probability)
    
        return entropyCalculated
    
    def CalculateFrequencyOfCharsOnAText(self, nameFile):
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
        
        return dictionary
    
    def CalculateEntropyOfAText(self, nameFile):
        dictionary = self.CalculateFrequencyOfCharsOnAText(nameFile)
        return self.CalculateEntropy(dictionary.values())
        
    

        

trial = Entropy()

print(trial.CalculateEntropy([1/3,1/3,1/3]))
print(trial.CalculateEntropyOfAText("Prova.txt"))