import math
class GammaCoder():
    def encode(self, value):
        bin_value = '%s'+str(bin(value))[2:]
        amount_zero = math.trunc(math.log2(value))
        return bin_value % ('0'*amount_zero)
    
    def decoder(self, value):
        i = 0
        while(i < len(value)-1 and value[i] == '0'):
            i+=1
        
        value_to_return = int(value[i:], base=2)
        return value_to_return
