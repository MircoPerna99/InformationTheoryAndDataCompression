class SuffixArray(): 
    def SA_IS(self, text):     
        self.InitTextToUser(text)
        self.SetTextLength()
        self.SetSuffixArrayType()
        self.SetLMSPositions()
        saLms = self.InduceSort(self.lmsPositions)
        shortedString = self.GetShortenedString(saLms)
        lmsOrdered = self.GetOrderedLMS(shortedString, saLms)
        return self.InduceSort(lmsOrdered)   
        
    def GetOrderedLMS(self, shortedString, saLMS):
        lmsOrdered = []
        if(len(set(shortedString)) < len(shortedString)):
            ssSa = SuffixArray().SA_IS(shortedString)
            lmsOrdered = [self.lmsPositions[i] for i in ssSa]
        else:
            for i in saLMS:
                if(self.isLms[i]):
                    lmsOrdered.append(i)
                    
        return lmsOrdered
    
    def InitTextToUser(self, text):
        if(text[-1] != '$'):
            text += '$'
        
        self.textToUse = text
    
    def SetTextLength(self):
        self.textLength =  len(self.textToUse)
        
    def SetSuffixArrayType(self):
        self.suffixArrayType = [False]* self.textLength
        self.suffixArrayType[self.textLength-1] = True
        for i in range(self.textLength-2, -1, -1):
            self.suffixArrayType[i] = self.DefineType(i)
         
    def DefineType(self, index):
        if(self.textToUse[index] == self.textToUse[index+1]):
            return  self.suffixArrayType[index+1]
        else:
            return self.textToUse[index] < self.textToUse[index+1]
    
    
    def SetLMSPositions(self):
        self.lmsPositions = []
        self.isLms = [False]*self.textLength
        for i in range(1, len(self.textToUse)):
            if( not self.suffixArrayType[i-1] and  self.suffixArrayType[i]):
                self.lmsPositions.append(i)
                self.isLms[i] = True
           
    def InduceSort(self, lmsPositions): 
        sizeText = len(self.textToUse)  
        sa = [-1] * sizeText
        buckets = self.GetBucketSizes()
        
        tails = self.GetBucketTails(buckets)
        for pos in reversed(lmsPositions):
            bucket = self.textToUse[pos]
            tails[bucket] -= 1
            sa[tails[bucket]] = pos
        
        heads = self.GetBucketHeads(buckets)
        for i in range(sizeText):
            pos = sa[i]
            if pos > 0 and not self.suffixArrayType[pos - 1]:
                bucket = self.textToUse[pos - 1]
                if(heads[bucket] < len(sa)):
                    sa[heads[bucket]] = pos - 1
                    heads[bucket] += 1
        
        
        # Induce S-type suffixes
        tails = self.GetBucketTails(buckets)
        for i in range(sizeText - 1, -1, -1):
            pos = sa[i]
            if pos > 0 and self.suffixArrayType[pos - 1]:
                bucket = self.textToUse[pos - 1]
                tails[bucket] -= 1
                sa[tails[bucket]] = pos - 1
        return sa  
                
    def GetBucketSizes(self):
        alphabetOccurences = [0] * 255
        for c in self.textToUse: 
            alphabetOccurences[ord(c)] += 1
        
        buckets = {chr(i): val for i, val in enumerate(alphabetOccurences) if val != 0}
        return buckets

    def GetBucketHeads(self, buckets):
        heads = {}
        sum = 0
        for key in buckets.keys():
            heads[key] = sum
            sum += buckets[key]
        return heads

    def GetBucketTails(self, buckets):
        tails = {}
        sum = 0
        for key in buckets.keys():
            sum += buckets[key]
            tails[key] = sum
        return tails
    
    def GetShortenedString(self, saLms):
        prevLms = -1
        lmsNames = [-1] * self.textLength
        newName = 0
        for i in saLms:
                if  self.isLms[i]:
                    if prevLms == -1:
                        newName += 1
                    else:
                        j = prevLms
                        k = i
                        while j < self.textLength and k < self.textLength and self.textToUse[j] == self.textToUse[k] and self.isLms[j] ==  self.isLms[k]:
                            j += 1
                            k += 1
                        if j == self.textLength or k == self.textLength or self.textToUse[j] != self.textToUse[k]:
                            newName += 1
                    lmsNames[i] = newName - 1
                    prevLms = i
              
        return ''.join(self.FromIntToCharShortenedString(name) for name in lmsNames if name != -1)
    
    def FromIntToCharShortenedString(self,  value):
        if(value == 0):
            return '$'
        else:
           return chr(value + 96)

text = 'banaananaanana'
print(SuffixArray().SA_IS(text))

text = 'aaaa'
print(SuffixArray().SA_IS(text))

text = 'banana'
print(SuffixArray().SA_IS(text))

text = 'abcab'
print(SuffixArray().SA_IS(text))

text = 'mississippi'
print(SuffixArray().SA_IS(text))
