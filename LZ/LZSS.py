from LZ.LZ77 import *

class Codeword():
    def __init__(self, distance, value):
        self.distance = distance
        self.value = value

class LZSS(LZ77):
        def __init__(self): 
            super().__init__()        
            
        def Encode(self, text):
            self.init_buffers(text)
            self.execute_encode()
            for value in self.encode_text:
                print(value.distance, value.value)       
        
        def execute_encode(self):
            while(self.look_ahead_buffer):
                print(self.search_buffer, "|", self.look_ahead_buffer)
                prefix = self.find_longest_prefix()
                new_codeword = self.calculate_codeword(prefix)
                self.encode_text.append(new_codeword)
                self.update_buffers(prefix.length)
            
            print(self.search_buffer, "|", self.look_ahead_buffer)
            
        def update_buffers(self, length):
            end_point = 1
            if(length != 0):
                end_point = length
            self.update_search_buffer(end_point)    
            self.look_ahead_buffer =  self.look_ahead_buffer[end_point:]  
        
        def update_search_buffer(self, end_point):   
            self.search_buffer =  self.search_buffer + self.look_ahead_buffer[0:end_point]
            len_search_buffer = len(self.search_buffer)
            if( len_search_buffer > self.length_window):
                self.search_buffer =   self.search_buffer[(len_search_buffer-self.length_window):len_search_buffer]
        
        def calculate_codeword(self, prefix):
            new_codeword = Codeword(0, 0)
            if(prefix.length == 0):
                new_codeword.value = self.look_ahead_buffer[0]
            else:
                new_codeword.distance = prefix.distance
                new_codeword.value = prefix.length
            
            return new_codeword
        
        def decode_codeword(self, prefix, text):
            if(prefix.distance == 0):
                text = text + prefix.value
            else:
                len_text = len(text)
                end_index = len_text - (prefix.distance-prefix.value)
                start_index = end_index - prefix.value            
                text = text + text[start_index:end_index]

            return text
        
coder = LZSS()
coder.Encode("aabbabab")   
print(coder.Decode())
        
