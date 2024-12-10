from LZ.LZ77 import *

class Codeword():
    def __init__(self, distance, value):
        self.distance = distance
        self.value = value

class LZSS(LZ77):
        def __init__(self): 
            super().__init__()        
            
        def Encode(self, text):
            self.InitBuffers(text)
            self.ExecuteEncode()
            for value in self.encodeText:
                print(value.distance, value.value)       
        
        def ExecuteEncode(self):
            while(self.lookAheadBuffer):
                print(self.searchBuffer, "|", self.lookAheadBuffer)
                prefix = self.FindLongestPrefix()
                newCodeWord = self.CalculateCodeWord(prefix)
                self.encodeText.append(newCodeWord)
                self.UpdateBuffers(prefix.length)
            
            print(self.searchBuffer, "|", self.lookAheadBuffer)
            
        def UpdateBuffers(self, length):
            endpoint = 1
            if(length != 0):
                endpoint = length
            self.UpdateSearchBuffer(endpoint)    
            self.lookAheadBuffer =  self.lookAheadBuffer[endpoint:]  
        
        def UpdateSearchBuffer(self, endpoint):   
            self.searchBuffer =  self.searchBuffer + self.lookAheadBuffer[0:endpoint]
            lenSearchBuffer = len(self.searchBuffer)
            if( lenSearchBuffer > self.lengthWindow):
                self.searchBuffer =   self.searchBuffer[(lenSearchBuffer-self.lengthWindow):lenSearchBuffer]
        
        def CalculateCodeWord(self, prefix):
            newCodeword = Codeword(0, 0)
            if(prefix.length == 0):
                newCodeword.value = self.lookAheadBuffer[0]
            else:
                newCodeword.distance = prefix.distance
                newCodeword.value = prefix.length
            
            return newCodeword
        
        def DecodeCodeWord(self, prefix, text):
            if(prefix.distance == 0):
                text = text + prefix.value
            else:
                lenText = len(text)
                endIndex = lenText - (prefix.distance-prefix.value)
                startIndex = endIndex - prefix.value            
                text = text + text[startIndex:endIndex]

            return text
        
coder = LZSS()
coder.Encode("aabbabab")   
print(coder.Decode())
        
