import math
class GammaCoder():
    def Encode(self, value):
        binValue = '%s'+str(bin(value))[2:]
        amountZero = math.trunc(math.log2(value))
        return binValue % ('0'*amountZero)
    
    def Decoder(self, value):
        i = 0
        while(i < len(value)-1 and value[i] == '0'):
            i+=1
        
        valueToReturn = int(value[i:], base=2)
        return valueToReturn
