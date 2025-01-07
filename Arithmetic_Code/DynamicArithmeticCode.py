import math
from Arithmetic_Code.ArithmeticCode  import ArithmeticCode

class DynamicArithmeticCode(ArithmeticCode):
        def __init__(self, symbols_frequency):
            self.symbols_frequency = symbols_frequency
            super().__init__(self.calculate_probabilities())
            self.symbols_probabilities = {}
            self.len_message = 0
         
            
        def calculate_probabilities(self):
            symbols_probabilities = {}
            amount_item = sum(self.symbols_frequency.values())
            for symbol in self.symbols_frequency:
                symbols_probabilities[symbol] = self.symbols_frequency[symbol]/ amount_item
            
            return symbols_probabilities
        
        def change_frequency_and_probabilities(self, symbol):
             self.symbols_frequency[symbol] +=1
             self.source = self.calculate_probabilities()
             self.calculate_cumulative_probabilities_of_source()
         
        def reset_frequency_and_probabilities(self):
            for key in self.symbols_frequency.keys():
                    self.symbols_frequency[key] = 1
            self.source = self.calculate_probabilities()
            self.calculate_cumulative_probabilities_of_source()   

                 
        def encode_message(self, message):
            self.len_message = len(message)
            high = 1
            low = 0
            for i in  range(0, len(message)):
                old_high = high
                high = old_high*self.source[message[i]]
                low = low + old_high*self.cumulative_probabilities[message[i]]
                self.change_frequency_and_probabilities(message[i])
                
            self.reset_frequency_and_probabilities()
            return low
        
        def decode_message(self, encoded_message):
            high = 1
            low = 0
            decoded_message = ""
            for i in range(self.len_message):
                char_to_add = self.decode_symbol(encoded_message, low, low+high)
                decoded_message += char_to_add
                old_high = high
                high = old_high*self.source[char_to_add]
                low = low + old_high*self.cumulative_probabilities[char_to_add]
                self.change_frequency_and_probabilities(char_to_add)
            return decoded_message
        

# dic = {'a': 1, 'b':1}
# prova =  DynamicArithmeticCode(dic)
# codedMessage = prova.encode_message('abb')
# print("encode message:",codedMessage)
# dic = {'a': 2, 'b':1}
# prova2 =  DynamicArithmeticCode(dic)
# print("decode message:" ,prova2.decode_message(codedMessage, 3) )
             
        
            
            
        