import re
class Pair():
    def __init__(self):
        self.frequency = 0
        self.pair = ''

class RePairCreator():
    def __init__(self):
        self.grammar={}
        self.index_value = 0
        self.array_chars = []
        
    def set_index_value(self, value):
        self.index_value = value
        
    def apply_for_thue_morse_word(self, text):
        lista = text.split("X")[1:]
        self.array_chars  = [f"X{item}" for item in lista] 
            
        pair_to_remove = Pair()        
        pair_to_remove = self.get_most_common_pair()
        
        while(pair_to_remove.frequency > 1):
            self.add_rule(pair_to_remove.pair)
            self.replace_pair(pair_to_remove.pair)      
            pair_to_remove = self.get_most_common_pair()
              
        final_right_rule = self.from_array_to_text()
        self.grammar[final_right_rule] = 'S'
    
        
    def apply(self, text, is_chomsky_normal_form = True):
        self.array_chars = self.from_text_to_array(text)

        if(is_chomsky_normal_form):
            text =self.init_chomsky_normal_form()
            
        pair_to_remove = Pair()        
        pair_to_remove = self.get_most_common_pair()
        
        while(pair_to_remove.frequency > 1):
            self.add_rule(pair_to_remove.pair)
            self.replace_pair(pair_to_remove.pair)      
            pair_to_remove = self.get_most_common_pair()
              
        final_right_rule = self.from_array_to_text()
        self.grammar[final_right_rule] = 'S'
    
    def replace_pair(self, pair_to_remove):
            new_array = []
            i = 0
            while(i+1 < len(self.array_chars)):
                pair = self.array_chars[i]+self.array_chars[i+1]
                if(pair_to_remove != pair):
                    new_array.append(self.array_chars[i])
                else:
                    new_array.append( self.grammar[pair_to_remove])
                    i+=1

                i+=1
                
            if(i == len(self.array_chars)-1):
                new_array.append(self.array_chars[i])
                    
            self.array_chars = new_array
    
    def from_array_to_text(self):
        return ''.join(self.array_chars)
        
    def  from_text_to_array(self, text):
            return list(text)
        
    def print_grammar(self):
        for key in self.grammar.keys():
            print(self.grammar[key],'->',key)      
     
    def get_most_common_pair(self):
        pairs = {}
        pair_to_return = Pair()
        i = 0
        while(i+1 < len(self.array_chars)):
            pair = self.array_chars[i]+self.array_chars[i+1]
            if( pair in pairs):
                pairs[pair] +=1
            else:
                pairs[pair] = 1

            if(pairs[pair]  > pair_to_return.frequency):
                pair_to_return.frequency = pairs[pair]
                pair_to_return.pair = pair
            
            i+=1

        return pair_to_return
    
    def init_chomsky_normal_form(self):
            self.init_dictionary_grammar()
            for i in range(len(self.array_chars)):
                self.array_chars[i] = self.grammar[self.array_chars[i]]
    
    def init_dictionary_grammar(self):
            for char in self.array_chars:
                if(not char in self.grammar):
                    self.add_rule(char) 

    def add_rule(self, right_value):
            left_value = self.define_left_symbol_from_char()
            self.grammar[right_value] = left_value
        
    def define_left_symbol_from_char(self, char = 'X'):
            new_symbol = char+str(self.index_value)
            self.index_value +=1
            return new_symbol
        
    def reverse(self):
        output = ""
        for key in reversed(self.grammar.keys()):
            if(output == ""):
                output += str(key)
            else:
                output = output.replace(self.grammar[key], key)
        
        return output