#TODO SCRIVERE CODICE

class LZWCoder():
    def __init__(self, alphabet):
        self.InitCodeBookEncode(alphabet)
        print(self.codebookEncode)

    def InitCodeBookEncode(self, alphabet):
        self.codebookEncode = {}
        self.codebookDecode = {}
        i = 0
        while i < len(alphabet):
            self.codebookEncode[alphabet[i]] = i+1
            self.codebookDecode[i+1] = alphabet[i]
            i +=1
    
    def Encode(self, text):
        valueToAdd = len(self.codebookEncode)+1
        output = ""
        indexToAnalize = 0
        while indexToAnalize < len(text):
            testToAnalize = text[indexToAnalize:]
            
            codeWord = self.FindCodeword(testToAnalize)
            if(self.ShouldAddCodeword(testToAnalize, codeWord)):
                self.AddCodeword(valueToAdd, codeWord, testToAnalize)
            
            indexToAnalize += len(codeWord)
              
            output = self.UpdateOutput(codeWord, output)
            
            valueToAdd+=1

        return output
    
    def UpdateOutput(self, codeWord, output):
        return output+str(self.codebookEncode[codeWord])+" "
    
    def FindCodeword(self, text):
        i = 1
        while(text and i <= len(text) and text[0:i] in self.codebookEncode):
            i+=1
        
        if(i != 1):
            i-=1
            
        return text[0:i]
    
    def AddCodeword(self,value, prefix,text):
        codeWordToAdd = text[0:len(prefix)+1]
        self.codebookEncode[codeWordToAdd] = value
        
    def ShouldAddCodeword(self, text, prefix):
        print(text,prefix) 
        return len(text)>len(prefix)
    
    def Decode(self, testToDecode):
        listToDecode = testToDecode.split()
        keyToAdd = len(self.codebookDecode)+1
        valueToAdd = ""
        output = ""
        index = 0
        while index < len(listToDecode):
            codeToAnalize =  int(listToDecode[index])

            if(not codeToAnalize in self.codebookDecode):
                self.AddCodewordNotExisting(index,listToDecode,keyToAdd)

            output = output + self.codebookDecode[codeToAnalize] 
             
            if(valueToAdd != ""):
                self.codebookDecode[keyToAdd]=valueToAdd+self.codebookDecode[codeToAnalize][0]
                keyToAdd+=1
        
            valueToAdd = self.codebookDecode[codeToAnalize]
            index+=1
            
        return output
    
    def AddCodewordNotExisting(self, index, listItem, keyToAdd):
            previousCodeword = self.codebookDecode[int(listItem[index])-1]
            self.codebookDecode[keyToAdd]= previousCodeword + previousCodeword[0]

    
    

coder = LZWCoder(['a','b','c']) 
value = coder.Encode('bcababbc')  
print(value)
print(coder.Decode(value))

coder = LZWCoder(['A']) 
value = coder.Encode('AAAAAA')  
print(value)
print(coder.Decode(value))
        
    
coder = LZWCoder(['T','O','B','E','R', 'N']) 
value = coder.Encode('TOBEORNOTTOBEORTOBEORNOT')  
print(value)
print(coder.Decode(value))