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
    
    
    def ComposeRotation(self, text, list):
        for i in range(len(text)):
            list[i] = text[i]+list[i]
    
    #TODO: Not works for abracadabra
    def Reverse(self,  text, index):
        sortedText = list(text)
        sortedText.sort()
        
        for i in range(len(text)-1):
            self.ComposeRotation(text, sortedText)
            sortedText.sort()
        
        return sortedText[index]
    
value = BWT().Trasform("banana")
print(BWT().Reverse(value.trasformedText, value.index))

value = BWT().Trasform("abracadabra")
print(BWT().Reverse(value.trasformedText, value.index))