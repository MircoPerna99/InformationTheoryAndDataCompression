class Prefix():
        def __init__(self, index, length):
            self.index = index
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
            print(value.index, value.length, value.nextChar)
    
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
        else:
            return oldPrefix
   
    def DefineNearPrefix(self,oldPrefix, newPrefix):
            if(oldPrefix.index < newPrefix.index):
                return newPrefix
            else:
                return oldPrefix
    
        
            
# print("B")
# LZ77().Encode("B")
# print("BABB")
# LZ77().Encode("BABB")   
LZ77().Encode("babbababbaabbaabaabaaa")   
print("babbababbaabbaabaabaa")
LZ77().Encode("!@#$!@#$!")      
# print("abaababaabb")
LZ77().Encode("ABCDEFGABCDEF")   
        