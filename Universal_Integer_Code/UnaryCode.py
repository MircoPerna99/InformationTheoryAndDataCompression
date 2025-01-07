class UnaryCoder():
    def encode(self, value):
        value_encode = '1'
        for i in range(value):
            value_encode = '0'+value_encode
        
        return value_encode
    
    def decode(self, value):
        value_decoded = 0
        while(value[value_decoded] != '1'):
            value_decoded+=1
        return value_decoded
