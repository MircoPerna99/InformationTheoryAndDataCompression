import re
class RePairCreator():
    def __init__(self):
        self.grammar={}
        self.index_value = 1
        
    def apply(self, text, is_chomsky_normal_form = True):
        if(is_chomsky_normal_form):
            text =self.init_chomsky_normal_form(text)
                             
        print(text)
        pairs = self.define_pairs(text)
        pair_to_remove = self.max_occurences_pair(pairs)
        while(pairs.count(pair_to_remove) >1):
            #print(pair_to_remove)
            new_symbol_to_add = self.define_left_symbol_from_char(self.index_value)
            self.index_value +=1
            self.grammar[pair_to_remove] = new_symbol_to_add
            text = text.replace(pair_to_remove,new_symbol_to_add)
            #print(text)
            pairs = self.define_pairs(text)
            pair_to_remove = self.max_occurences_pair(pairs)
        
        self.grammar[text] = 'S'
        self.print_grammar()
        
    def print_grammar(self):
        for key in self.grammar.keys():
            print(self.grammar[key],'->',key)
        
    def max_occurences_pair(self, pairs):
        pair_to_return = pairs[0]
        pair_to_return_occurences = pairs.count(pairs[0])
        for i in range(1,len(pairs)):
            occurences_new_pair = pairs.count(pairs[i])
            if(occurences_new_pair > pair_to_return_occurences):
                pair_to_return = pairs[i]
                pair_to_return_occurences = occurences_new_pair
        
        return pair_to_return
    
    def init_chomsky_normal_form(self, text):
        self.init_dictionary_grammar(text)
        for key in self.grammar:
            text = text.replace(key,self.grammar[key])
        return text
    
    def define_pairs(self, text):
        list_char = re.findall(r'X\d|.', text)
        list_to_return = []
        last_pair = ''
        i = 0
        while(i+1 < len(list_char)):
            pair = list_char[i]+list_char[i+1]
            if(last_pair != pair):
                list_to_return.append(pair)
                last_pair = pair
            i+=1
            
        return list_to_return
    
    def init_dictionary_grammar(self, text):
        for char in text:
            if(not char in self.grammar):
                value_to_add = self.define_left_symbol_from_char(self.index_value)
                self.grammar[char] = value_to_add
                self.index_value+=1
                
        print(self.grammar)    

        
    def define_left_symbol_from_char(self, index, char = 'X'):
        return char+str(index)
            
             

RePairCreator().apply('aaabcaabaaabcabdabd')  
RePairCreator().apply('aaabcaabaaabcabdabd', False)  