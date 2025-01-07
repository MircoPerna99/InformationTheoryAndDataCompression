class FibonacciCode():
    def __init__(self):
        self.tracker = {2:1, 3:2}
    
    def encode(self, value):
        fibonacci_value = self.calculate_fibonacci(value)
        value_encoded = ''
        while(fibonacci_value>1):
            if((value_encoded == '' or value_encoded[0] == '0') and self.tracker[fibonacci_value]<= value):
                    value -= self.tracker[fibonacci_value]
                    value_encoded = '1'+value_encoded
            else:
                    value_encoded = '0'+value_encoded
            
            fibonacci_value -=1 
                    
             
        return value_encoded+'1'
    
    def calculate_fibonacci(self, value):
        fibonacci_value = self.tracker[2]
        i = 2
        while(self.tracker[i] < value):
            i+=1
            if(not i in self.tracker):
                fibonacci_value = self.get_fibonacci_value(i-1)+ self.get_fibonacci_value(i-2)
                self.tracker[i] = fibonacci_value

        if(self.tracker[i] > value):
            i -=1
        
        return i
    
    def get_fibonacci_value(self, value):
        if(not value in self.tracker):
            self.tracker[value] = self.get_fibonacci_value(value-1) + self.get_fibonacci_value(value-2)
                
        return self.tracker[value]
             
    
    def decode(self, value):
        end_point = len(value)-1
        i = 0
        value_to_return = 0
        while(i< end_point):
            value_to_return = int(value[i])*self.get_fibonacci_value(i+2)+value_to_return
            i += 1
        return value_to_return

encoder = FibonacciCode()
for i in range(1,10):
    print(i)
    value_encode = encoder.encode(i)
    print(value_encode)
    print(encoder.decode(value_encode))

    