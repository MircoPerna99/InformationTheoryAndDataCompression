class UnaryCoder():
    def Encode(self, value):
        valueToReturn = '1'
        for i in range(value):
            valueToReturn = '0'+valueToReturn
        
        return valueToReturn
    
    def Decode(self, value):
        valueToReturn = 0
        while(value[valueToReturn] != '1'):
            valueToReturn+=1
        return valueToReturn
