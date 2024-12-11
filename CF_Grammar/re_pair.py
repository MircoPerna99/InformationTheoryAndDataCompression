import re
class RePairCreator():
    def __init__(self):
        self.grammar={}
        self.indexValue = 1
        
    def Apply(self, text, isChomskyNormalForm = True):
        if(isChomskyNormalForm):
            text =self.InitisChomskyNormalForm(text)
                             
        print(text)
        pairs = self.DefinePairs(text)
        pairToRemove = self.MaxOccurencesPair(pairs)
        while(pairs.count(pairToRemove) >1):
            #print(pairToRemove)
            newSymbolToAdd = self.DefineLeftSymbolFromChar(self.indexValue)
            self.indexValue +=1
            self.grammar[pairToRemove] = newSymbolToAdd
            text = text.replace(pairToRemove,newSymbolToAdd)
            #print(text)
            pairs = self.DefinePairs(text)
            pairToRemove = self.MaxOccurencesPair(pairs)
        
        self.grammar[text] = 'S'
        self.PrintGrammar()
        
    def PrintGrammar(self):
        for key in self.grammar.keys():
            print(self.grammar[key],'->',key)
        
    def MaxOccurencesPair(self, pairs):
        pairToReturn = pairs[0]
        pairToReturnOccurences = pairs.count(pairs[0])
        for i in range(1,len(pairs)):
            occurencesNewPair = pairs.count(pairs[i])
            if(occurencesNewPair > pairToReturnOccurences):
                pairToReturn = pairs[i]
                pairToReturnOccurences = occurencesNewPair
        
        return pairToReturn
    
    def InitisChomskyNormalForm(self, text):
        self.InitDictionaryGrammar(text)
        for key in self.grammar:
            text = text.replace(key,self.grammar[key])
        return text
    
    def DefinePairs(self, text):
        listChar = re.findall(r'X\d|.', text)
        listToReturn = []
        lastPair = ''
        i = 0
        while(i+1 < len(listChar)):
            pair = listChar[i]+listChar[i+1]
            if(lastPair != pair):
                listToReturn.append(pair)
                lastPair = pair
            i+=1
            
        return listToReturn
    
    def InitDictionaryGrammar(self, text):
        for char in text:
            if(not char in self.grammar):
                valueToAdd = self.DefineLeftSymbolFromChar(self.indexValue)
                self.grammar[char] = valueToAdd
                self.indexValue+=1
                
        print(self.grammar)    

        
    def DefineLeftSymbolFromChar(self, index, char = 'X'):
        return char+str(index)
            
             

RePairCreator().Apply('aaabcaabaaabcabdabd')  
RePairCreator().Apply('aaabcaabaaabcabdabd', False)  