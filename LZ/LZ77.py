class Prefix():
        def __init__(self, distance, length):
            self.distance = distance
            self.length = length
            self.next_char = ""
            
class LZ77():
    def __init__(self):
            self.init_buffers()
            self.encode_text = []
            self.length_window = 5
    
    def encode(self, text, length_window = 5):
        self.length_window = length_window
        self.init_buffers(text)
        self.execute_encode()
        for value in self.encode_text:
            print(value.distance, value.length, value.next_char)
    
    def init_buffers(self, text = ""):
        self.search_buffer = ""
        self.look_ahead_buffer = text
    
    def execute_encode(self):
        while(self.look_ahead_buffer):
            print(self.search_buffer, "|", self.look_ahead_buffer)
            prefix = self.find_longest_prefix()
            self.calculate_char(prefix)
            self.encode_text.append(prefix)
            self.update_buffers(prefix.length)
        
        print(self.search_buffer, "|", self.look_ahead_buffer)
            
    def update_buffers(self, length):
        self.update_search_buffer(length)       
        self.look_ahead_buffer =  self.look_ahead_buffer[length+1:]     
        
    def update_search_buffer(self, length):   
            self.search_buffer =  self.search_buffer + self.look_ahead_buffer[0:length+1]
            len_search_buffer = len(self.search_buffer)
            if( len_search_buffer > self.length_window):
                self.search_buffer =   self.search_buffer[(len_search_buffer-self.length_window):len_search_buffer]
            
    def calculate_char(self,prefix):
        if(prefix.length == 0):
            prefix.next_char = self.look_ahead_buffer[0]
        elif(prefix.length >=  len(self.look_ahead_buffer)):
            prefix.next_char = ""
        else:
            prefix.next_char = self.look_ahead_buffer[prefix.length]
             
    def find_longest_prefix(self):
        longest_prefix = Prefix(0,0)
        i = 0
        len_search_buffer = len(self.search_buffer)
        while(i < len_search_buffer):
            newPrefix = self.define_prefix(i)
            longest_prefix = self.define_longest_prefix(longest_prefix,newPrefix)
            i +=1
        return longest_prefix
    
    def define_prefix(self, index):
        j = 0
        i = index
        
        while(not self.is_index_out_of_range(i, self.search_buffer) and not self.is_index_out_of_range(j, self.look_ahead_buffer) and self.search_buffer[i] == self.look_ahead_buffer[j]):
            i+=1
            j+=1
        
        distance = self.define_distance_between_index(index, j)
        return Prefix(distance, j)
    
    def is_index_out_of_range(self, index, string):
        return index >= len(string)
    
    def define_distance_between_index(self, index_search_buffer, length):
        if(length == 0):
            return 0
        else:
            return len(self.search_buffer[index_search_buffer+length:]) + length
        
    def define_longest_prefix(self,oldPrefix, newPrefix):
        if(oldPrefix.length < newPrefix.length):
            return newPrefix
        elif(oldPrefix.length > newPrefix.length):
            return oldPrefix
        else:
            return self.define_near_prefix(oldPrefix, newPrefix)
   
    def define_near_prefix(self,old_prefix, new_prefix):
            if(old_prefix.distance > new_prefix.distance):
                return new_prefix
            else:
                return old_prefix
    
    def decode(self):
        return self.execute_decode(self.encode_text)
    
    def execute_decode(self, encode_text):
        text = ""
        for item in encode_text:
          text =  self.decode_code_word(item, text)
        return text
        
    def decode_code_word(self, prefix, text):
        if(prefix.distance == 0 and prefix.length == 0):
            text = text + prefix.next_char
        else:
           len_text = len(text)
           end_index = len_text - (prefix.distance-prefix.length)
           start_index = end_index - prefix.length            
           text = text + text[start_index:end_index] + prefix.next_char

        return text
            
# coder = LZ77()
# coder.encode("babbababbaabbaabaabaaa") 
# print(coder.decode())  
# LZ77().encode("AAAAAAA")     


# coder = LZ77()
# coder.encode("ABCDEABFABCDE") 
# print(coder.decode()) 


# coder = LZ77()
# coder.encode("ABCDEFG") 
# print(coder.decode())  


coder = LZ77()
coder.encode("ABABCCDABABCCD") 
print(coder.decode())   
        