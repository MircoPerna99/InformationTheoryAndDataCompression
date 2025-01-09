
class ThueMorseWord:
    #Method used to get the i char in the Thue-Morse word
    def get_TM_char(self, index):
        amount_of_ones = sum([1 for bit in bin(index)[2:] if bit == '1'])
        return self.define_char(amount_of_ones)
        
    def define_char(self, amount_of_ones):
        if(amount_of_ones % 2 == 0):
            return 'a'
        else:
            return 'b'
    
    def get_TM_word(self, order):
        word = ""
        length_word = self.get_length_TM_word(order)
        for i in range(0,length_word):
            word += self.get_TM_char(i)
        
        return word
    
    def get_length_TM_word(self, order):
        return 2**order
            
    
    


    
    