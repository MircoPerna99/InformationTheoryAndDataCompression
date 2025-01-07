
class LZWCoder():
    def __init__(self, alphabet):
        self.init_codebook_encode(alphabet)
        print(self.codebook_encode)

    def init_codebook_encode(self, alphabet):
        self.codebook_encode = {}
        self.codebook_decode = {}
        i = 0
        while i < len(alphabet):
            self.codebook_encode[alphabet[i]] = i+1
            self.codebook_decode[i+1] = alphabet[i]
            i +=1
    
    def encode(self, text):
        value_to_add = len(self.codebook_encode)+1
        output = ""
        index_to_analize = 0
        while index_to_analize < len(text):
            test_to_analize = text[index_to_analize:]
            
            codeword = self.find_codeword(test_to_analize)
            if(self.should_add_codeword(test_to_analize, codeword)):
                self.add_codeword(value_to_add, codeword, test_to_analize)
            
            index_to_analize += len(codeword)
              
            output = self.update_output(codeword, output)
            
            value_to_add+=1

        return output
    
    def update_output(self, codeword, output):
        return output+str(self.codebook_encode[codeword])+" "
    
    def find_codeword(self, text):
        i = 1
        while(text and i <= len(text) and text[0:i] in self.codebook_encode):
            i+=1
        
        if(i != 1):
            i-=1
            
        return text[0:i]
    
    def add_codeword(self,value, prefix,text):
        codeword_to_add = text[0:len(prefix)+1]
        self.codebook_encode[codeword_to_add] = value
        
    def should_add_codeword(self, text, prefix):
        return len(text)>len(prefix)
    
    def decode(self, test_to_decode):
        list_to_decode = test_to_decode.split()
        key_to_add = len(self.codebook_decode)+1
        value_to_add = ""
        output = ""
        index = 0
        while index < len(list_to_decode):
            code_to_analize =  int(list_to_decode[index])

            if(not code_to_analize in self.codebook_decode):
                self.add_codeword_not_existing(index,list_to_decode,key_to_add)

            
            output = output + self.codebook_decode[code_to_analize] 
             
            if(value_to_add != ""):
                self.codebook_decode[key_to_add]=value_to_add+self.codebook_decode[code_to_analize][0]
                key_to_add+=1
        
            value_to_add = self.codebook_decode[code_to_analize]
            index+=1
            
        return output
    
    def add_codeword_not_existing(self, index, list_item, key_to_add):
            previous_codeword = self.codebook_decode[int(list_item[index-1])]
            self.codebook_decode[key_to_add]= previous_codeword + previous_codeword[0]

    
    

# coder = LZWCoder(['a','b','c']) 
# value = coder.encode('bcababbc')  
# print(value)
# print(coder.Decode(value))

# coder = LZWCoder(['A']) 
# value = coder.encode('AAAAAA')  
# print(value)
# print(coder.Decode(value))
        
    
# coder = LZWCoder(['N', 'e', 'l', ' ', 'm', 'z', 'o', 'd', 'c', 'a', 'i', 'n', 's', 't', 'r', 'v', 
#  'p', 'u', ',', 'h', 'é', '.', 'A', 'q', 'è', 'g', 'f']
# ) 
# value = coder.encode('Nel mezzo del cammin di nostra vita mi ritrovai per una selva oscura, ché la diritta via era smarrita. Ahi quanto a dir qual era è cosa dura esta selva selvaggia e aspra e forte.')  
# print(value)
# print(coder.Decode(value))