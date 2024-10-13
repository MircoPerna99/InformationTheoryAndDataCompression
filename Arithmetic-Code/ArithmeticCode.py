import math

class ArithmeticCode():
    def __init__(self, source):
            self.source = source
            self.cumulativeProbabilities = {}
            self.CalculateCumulativeProbabilitiesOfTheSource()
            
    def Code(self, text):
        return True

    def CalculateCumulativeProbabilities(self, symbol):
            cumulativeProbavilities = 0
            keys = list(self.source.keys())
            for i in range(keys.index(symbol)):
                cumulativeProbavilities += self.source[keys[i]]
            
            return cumulativeProbavilities

    def CalculateCumulativeProbabilitiesOfTheSource(self):
        for key in  self.source:
            self.cumulativeProbabilities[key] = self.CalculateCumulativeProbabilities(key)
            
    def Truncate(self, value, amountOfDecimal):
        return math.floor(value * 10**amountOfDecimal) / 10**amountOfDecimal
    
    def EncodeMessage(self, message):
        high = 1
        low = 0
        for i in  range(0, len(message)):
            oldHigh = high
            high = oldHigh*self.source[message[i]]
            low = low + oldHigh*self.cumulativeProbabilities[message[i]]

        return low

    def IsValueInsideRange(self, value, low, high):
        return value>=low and value < high

    def DecodeSymbol(self, value, low, high, amountOfDecimal):
        range = high-low
        lowToUse = low
        keys = list(self.source.keys())
        i = 0
        while( not self.IsValueInsideRange(value,lowToUse,(lowToUse + range*self.source[keys[i]]))):
            lowToUse = (lowToUse + range*self.source[keys[i]])
            i +=1
        
        return keys[i]
        

    def DecodeMessage(self, encodedMessage, lenMessage):
        high = 1
        low = 0
        decodedMessage = ""
        for i in range(lenMessage):
            charToAdd = self.DecodeSymbol(encodedMessage, low, low+high, i+1)
            decodedMessage += charToAdd
            oldHigh = high
            high = oldHigh*self.source[charToAdd]
            low = low + oldHigh*self.cumulativeProbabilities[charToAdd]
        return decodedMessage



dic = {'a': 0.5, 'b':0.25, 'c':0.25}
prova =  ArithmeticCode(dic)

print(prova.cumulativeProbabilities)
print("encode message:",prova.EncodeMessage('abac'))
print(prova.DecodeMessage(prova.EncodeMessage('abac'), 4))


# dic1 = {'a': 0.4, 'b':0.5, 'c':0.1}
# prova1 =  ArithmeticCode(dic1)

# print(prova1.cumulativeProbabilities)
# print(prova1.EncodeMessage('bbbc'))

# # dic2 = {'s': 0.5, 'w':0.1, 'i':0.2, 'm':0.1, '_':0.1}
dic2 = {'A': 0.2, 'B':0.5, 'C':0.3}
prova2 =  ArithmeticCode(dic2)

print(prova2.cumulativeProbabilities)
print(prova2.EncodeMessage('AABBAACCCBB'))
print(prova2.DecodeMessage(prova2.EncodeMessage('AABBAACCCBB'), len('AABBAACCCBB')))