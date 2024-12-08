import math
from Universal_Integer_Code.Gamma import GammaCoder

class DeltaCoder():
    def Encode(self, value):
        binValue = str(bin(value))[2:]
        valuteToConcat = math.trunc(math.log2(value))+1
        lengthGammaEncode = GammaCoder().Encode(valuteToConcat)
        return lengthGammaEncode+ binValue[1:]
    

    def Decoder(self, value):
        amountZero = self.LengthGamma(value)
        endGammaCode = 2*amountZero+1
        lenBin = int(value[amountZero:endGammaCode], base=2)
        valueToReturn = int('1'+value[len(value)-lenBin+1:len(value)], base=2)
        return valueToReturn
        
    def LengthGamma(self, value):
        i = 0
        while(i < len(value)-1 and value[i] == '0'):
            i += 1
        return i

for i in range(1, 10):
    value = DeltaCoder().Encode(i)
    print(value)
    print(DeltaCoder().Decoder(value))
