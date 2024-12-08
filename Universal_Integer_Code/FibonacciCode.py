

class FibonacciCode():
    def __init__(self):
        self.tracker = {2:1, 3:2}
    
    def Encode(self, value):
        fibonacciValue = self.CalculateFibonacci(value)
        valueToReturn = ''
        while(fibonacciValue>1):
            if((valueToReturn == '' or valueToReturn[0] == '0') and self.tracker[fibonacciValue]<= value):
                    value -= self.tracker[fibonacciValue]
                    valueToReturn = '1'+valueToReturn
            else:
                    valueToReturn = '0'+valueToReturn
            
            fibonacciValue -=1 
                    
             
        return valueToReturn+'1'
    
    def CalculateFibonacci(self, value):
        fibonacciValue = self.tracker[2]
        i = 2
        while(self.tracker[i] < value):
            i+=1
            if(not i in self.tracker):
                fibonacciValue = self.GetFibonacciVelue(i-1)+ self.GetFibonacciVelue(i-2)
                self.tracker[i] = fibonacciValue

        if(self.tracker[i] > value):
            i -=1
        
        return i
    
    def GetFibonacciVelue(self, value):
        if(not value in self.tracker):
            self.tracker[value] = self.GetFibonacciVelue(value-1) + self.GetFibonacciVelue(value-2)
                
        return self.tracker[value]
             
    
    def Decode(self, value):
        endPoint = len(value)-1
        i = 0
        valueToReturn = 0
        while(i< endPoint):
            valueToReturn = int(value[i])*self.GetFibonacciVelue(i+2)+valueToReturn
            i += 1
        return valueToReturn

encoder = FibonacciCode()
for i in range(1,10):
    print(i)
    valueEncod = encoder.Encode(i)
    print(valueEncod)
    print(encoder.Decode(valueEncod))

    