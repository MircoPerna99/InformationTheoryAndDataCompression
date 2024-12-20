import math
from Arithmetic_Code.ArithmeticCode  import ArithmeticCode

class DynamicArithmeticCode(ArithmeticCode):
        def __init__(self, symbolsFrequnecy):
            self.symbolsFrequnecy = symbolsFrequnecy
            super().__init__(self.CalculateProbabilities())
            self.symbolsProbabilities = {}
            self.lenMessage = 0
         
            
        def CalculateProbabilities(self):
            symbolsProbabilities = {}
            amountItem = sum(self.symbolsFrequnecy.values())
            for symbol in self.symbolsFrequnecy:
                symbolsProbabilities[symbol] = self.symbolsFrequnecy[symbol]/ amountItem
            
            return symbolsProbabilities
        
        def ChangeFrequencyAndProbabilities(self, symbol):
             self.symbolsFrequnecy[symbol] +=1
             self.source = self.CalculateProbabilities()
             self.CalculateCumulativeProbabilitiesOfTheSource()
         
        def ResetFrequencyAndProbabilities(self):
            for key in self.symbolsFrequnecy.keys():
                    self.symbolsFrequnecy[key] = 1
            self.source = self.CalculateProbabilities()
            self.CalculateCumulativeProbabilitiesOfTheSource()   

                 
        def EncodeMessage(self, message):
            self.lenMessage = len(message)
            high = 1
            low = 0
            for i in  range(0, len(message)):
                oldHigh = high
                high = oldHigh*self.source[message[i]]
                low = low + oldHigh*self.cumulativeProbabilities[message[i]]
                self.ChangeFrequencyAndProbabilities(message[i])
                
            self.ResetFrequencyAndProbabilities()
            return low
        
        def DecodeMessage(self, encodedMessage):
            high = 1
            low = 0
            decodedMessage = ""
            for i in range(self.lenMessage):
                charToAdd = self.DecodeSymbol(encodedMessage, low, low+high, i+1)
                decodedMessage += charToAdd
                oldHigh = high
                high = oldHigh*self.source[charToAdd]
                low = low + oldHigh*self.cumulativeProbabilities[charToAdd]
                self.ChangeFrequencyAndProbabilities(charToAdd)
            return decodedMessage
        

# dic = {'a': 1, 'b':1}
# prova =  DynamicArithmeticCode(dic)
# codedMessage = prova.EncodeMessage('abb')
# print("encode message:",codedMessage)
# dic = {'a': 2, 'b':1}
# prova2 =  DynamicArithmeticCode(dic)
# print("decode message:" ,prova2.DecodeMessage(codedMessage, 3) )
             
        
            
            
        