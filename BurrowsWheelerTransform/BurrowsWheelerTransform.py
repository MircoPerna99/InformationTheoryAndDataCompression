from Utilities.SuffixArray import SuffixArray

class   BWTResult():
    def __init__(self, trasformedText, index):
        self.trasformedText = trasformedText
        self.index = index

class BWT():
    def Rotate(self, text):
        return text[-1]+text[:-1]
    
    def SortText(self, text):
        return ''.join(sorted(text))
    
    def TakeTrasformedText(self, list):
         valueToReturn = ""
         
         for item in list:
             valueToReturn = valueToReturn + item[-1]
             
         return valueToReturn
    
    def Trasform(self, text):
        sizeText = len(text)
        listOfTexts = [text]
        
        for i in range(1, sizeText):
            listOfTexts.append(self.Rotate(listOfTexts[-1]))
        
        listOfTexts.sort()
                                
        return  BWTResult(self.TakeTrasformedText(listOfTexts), listOfTexts.index(text))
    
        
    def TrasformWithSA(self, text):
    
        if(text[-1] != '$'):
            text += '$'
    
        suffixArray = SuffixArray().SA_IS(text)
        bwt = self.GetTrasformedText(suffixArray, text)
        index = self.GetIndexOriginalText(suffixArray)
        return  BWTResult(bwt, index)

    def GetTrasformedText(self, suffixArray, text):
        output = ""
        
        for i in range(len(text)):
            charToAdd = ""
            if(suffixArray[i] == 0):
                charToAdd = '$'
            else:
                charToAdd = text[suffixArray[i]-1]
            
            output =output + charToAdd 
        
        return output
    
    def GetIndexOriginalText(self, suffixArray):
        for i in range(suffixArray):
            if(suffixArray[i] == 0):
                return 0
        
        return -1
        
    def ComposeRotation(self, text, list):
        for i in range(len(text)):
            list[i] = text[i]+list[i]
    
    def Reverse(self,  text, index):
        sortedText = list(text)
        sortedText.sort()
        
        for i in range(len(text)-1):
            self.ComposeRotation(text, sortedText)
            sortedText.sort()
        
        return sortedText[index]
    