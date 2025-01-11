
class ThueMorseWord:

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
    
    def get_TM_word_recursive(self, order):
        word = ""
        if(order == 0):
            return 'a'
        elif(order == 1):
            return 'ab'
        else:
            word = self.get_TM_word_recursive(order-1)
            length_word = self.get_length_TM_word(order-1)
            index = int(length_word/2)
            word_part_one = word[:index]
            word_part_two = word[index:]
            word = word+word_part_two+word_part_one
            return word
    
    def get_TM_word_recursive_with_grammar(self, order):
        word = ""
        if(order == 0):
            return 'X0'
        elif(order == 1):
            return 'X0X1'
        else:
            word = self.get_TM_word_recursive_with_grammar(order-1)
            length_word = self.get_length_TM_word(order-1)
            index = 2*int(length_word/2)
            word_part_one = word[:index]
            word_part_two = word[index:]
            word = word+word_part_two+word_part_one
            return word
    
    
    def get_length_TM_word(self, order):
        return 2**order

    


    
    