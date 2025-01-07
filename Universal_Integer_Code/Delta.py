import math
from Universal_Integer_Code.Gamma import GammaCoder

class DeltaCoder():
    def encode(self, value):
        bin_value = str(bin(value))[2:]
        valute_to_concat = math.trunc(math.log2(value))+1
        length_gamma_encode = GammaCoder().encode(valute_to_concat)
        return length_gamma_encode+ bin_value[1:]
    

    def decoder(self, value):
        amount_zero = self.length_gamma(value)
        end_gamma_code = 2*amount_zero+1
        len_bin = int(value[amount_zero:end_gamma_code], base=2)
        value_to_return = int('1'+value[len(value)-len_bin+1:len(value)], base=2)
        return value_to_return
        
    def length_gamma(self, value):
        i = 0
        while(i < len(value)-1 and value[i] == '0'):
            i += 1
        return i

for i in range(1, 10):
    value = DeltaCoder().encode(i)
    print(value)
    print(DeltaCoder().decoder(value))
