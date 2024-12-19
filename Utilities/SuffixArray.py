class SuffixArray():
    def __init__(self, text):
        self.text = text + '$'
        self.suffixArray = []
        self.suffixArrayTypes = []
        self.GenerateSuffixArray()
        self.DefineType()
        print(self.suffixArray)
        print(self.suffixArrayTypes)
        pass

    def GenerateSuffixArray(self):
       for i in range(len(self.text)):
            self.suffixArray.append(i)
            
    def GetSuffix(self, index):
        indexText = self.suffixArray[index]
        return self.text[indexText:]
    
    def PrintSuffixArray(self):
        for i in range(len(self.suffixArray)):
            print(self.GetSuffix(i))
            
    def DefineType(self):
        self.suffixArrayTypes.insert(0, "S") 
        for i in range(len(self.suffixArray)-2,-1, -1):
            currentSuffix = self.GetSuffix(i)
            nextSuffix = self.GetSuffix(i+1)
            if(currentSuffix>nextSuffix):
                self.suffixArrayTypes.insert(0, "L") 
                if(self.suffixArrayTypes[1] == 'S'):
                    self.suffixArrayTypes[1] = 'S*'
            elif(currentSuffix<nextSuffix):
                self.suffixArrayTypes.insert(0, "S") 
            else:
                self.suffixArrayTypes.insert(0, nextSuffix)
                
    def GetLMSFactors(self):
        indices = [i for i, x in enumerate(self.suffixArrayTypes) if x == "S*"]
        print(indices)
            
    
    
text = 'banana'
SuffixArray(text).PrintSuffixArray()

text = 'cbbcacbbcadacbadacb'
SuffixArray(text).GetLMSFactors()


