class Prefix():
        def __init__(self, distance, length):
            self.distance = distance
            self.length = length
            self.nextChar = ""
            

class LZ77():
    def __init__(self):
            self.InitBuffers()
            self.encodeText = []
    
    def Encode(self, text):
        self.InitBuffers(text)
        self.ExecuteEncode()
        for value in self.encodeText:
            print(value.distance, value.length, value.nextChar)
    
    def InitBuffers(self, text = ""):
        self.searchBuffer = ""
        self.lookAheadBuffer = text
    
    def ExecuteEncode(self):
        while(self.lookAheadBuffer):
            print(self.searchBuffer, "|", self.lookAheadBuffer)
            prefix = self.FindLongestPrefix()
            self.CalculateChar(prefix)
            self.encodeText.append(prefix)
            self.UpdateBuffers(prefix.length)
        
        print(self.searchBuffer, "|", self.lookAheadBuffer)
            
    def UpdateBuffers(self, length):
        self.searchBuffer =  self.searchBuffer + self.lookAheadBuffer[0:length+1]     
        self.lookAheadBuffer =  self.lookAheadBuffer[length+1:]            
            
    def CalculateChar(self,prefix):
        if(prefix.length == 0):
            prefix.nextChar = self.lookAheadBuffer[0]
        elif(prefix.length >=  len(self.lookAheadBuffer)):
            prefix.nextChar = ""
        else:
            prefix.nextChar = self.lookAheadBuffer[prefix.length]
             
    def FindLongestPrefix(self):
        longestPrefix = Prefix(0,0)
        i = 0
        lengthSearchBuffer = len(self.searchBuffer)
        while(i < lengthSearchBuffer):
            newPrefix = self.DefinePrefix(i)
            longestPrefix = self.DefineLongestPrefix(longestPrefix,newPrefix)
            i +=1
        return longestPrefix
    
    def DefinePrefix(self, index):
        j = 0
        i = index
        
        while(not self.IsIndexOutOfRange(i, self.searchBuffer) and not self.IsIndexOutOfRange(j, self.lookAheadBuffer) and self.searchBuffer[i] == self.lookAheadBuffer[j]):
            i+=1
            j+=1
        
        distance = self.DefineDistanceBetweenIndex(index, j)
        return Prefix(distance, j)
    
    def IsIndexOutOfRange(self, index, string):
        return index >= len(string)
    
    def DefineDistanceBetweenIndex(self, indexSearchBuffer, length):
        if(length == 0):
            return 0
        else:
            return len(self.searchBuffer[indexSearchBuffer+length:]) + length
        
    
    def DefineLongestPrefix(self,oldPrefix, newPrefix):
        if(oldPrefix.length < newPrefix.length):
            return newPrefix
        elif(oldPrefix.length > newPrefix.length):
            return oldPrefix
        else:
            return self.DefineNearPrefix(oldPrefix, newPrefix)
   
    def DefineNearPrefix(self,oldPrefix, newPrefix):
            if(oldPrefix.distance > newPrefix.distance):
                return newPrefix
            else:
                return oldPrefix
    
    
    def Decode(self):
        return self.ExecuteDecode(self.encodeText)
    
    def ExecuteDecode(self, encodeText):
        text = ""
        for item in encodeText:
          text =  self.DecodeCodeWord(item, text)
        return text
        
    def DecodeCodeWord(self, prefix, text):
        if(prefix.distance == 0 and prefix.length == 0):
            text = text + prefix.nextChar
        else:
           lenText = len(text)
           endIndex = lenText - (prefix.distance-prefix.length)
           startIndex = endIndex - prefix.length            
           text = text + text[startIndex:endIndex] + prefix.nextChar
           
    
        
        return text
            
coder = LZ77()
coder.Encode("babbababbaabbaabaabaaa") 
print(coder.Decode())  
LZ77().Encode("AAAAAAA")     


coder = LZ77()
coder.Encode("ABCDEABFABCDE") 
print(coder.Decode())  
        