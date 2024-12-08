import math
from Universal_Integer_Code.UnaryCode import UnaryCoder

class RiceCoder():
    def Encode(self, value, base = 2):
        module = 2**base
        quotient = value//module
        remainder = value%module
        quotientString = UnaryCoder().Encode(quotient+1)
        return quotientString + self.DefineRemainderBin(remainder, base)
    
    def DefineRemainderBin(self, remainder, base):
        remainderBin = str(bin(remainder))[2:]
        while(len(remainderBin)<base):
            remainderBin = '0'+remainderBin
        
        print(remainderBin)
        return remainderBin
    
    def Decoder(self, value, base=2):
        module = 2**base
        quotient = UnaryCoder().Decode(value[:len(value)-base])-1
        valueToReturn = quotient*module
        valueToReturn += int(value[len(value)-base:], base=2)
        return valueToReturn

        