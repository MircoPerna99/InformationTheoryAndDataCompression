import math
from Universal_Integer_Code.UnaryCode import UnaryCoder

class RiceCoder():
    def encode(self, value, base = 2):
        module = 2**base
        quotient = value//module
        remainder = value%module
        quotient_string = UnaryCoder().Encode(quotient+1)
        return quotient_string + self.define_remainder_bin(remainder, base)
    
    def define_remainder_bin(self, remainder, base):
        remainder_bin = str(bin(remainder))[2:]
        while(len(remainder_bin)<base):
            remainder_bin = '0'+remainder_bin
        
        return remainder_bin
    
    def decoder(self, value, base=2):
        module = 2**base
        quotient = UnaryCoder().decode(value[:len(value)-base])-1
        value_to_return = quotient*module
        value_to_return += int(value[len(value)-base:], base=2)
        return value_to_return

        