import math

class ArithmeticCode():
    def __init__(self, source):
            self.source = source
            self.cumulative_probabilities = {}
            self.calculate_cumulative_probabilities_of_source()

    def calculate_cumulative_probabilities(self, symbol):
            cumulative_probability = 0
            keys = list(self.source.keys())
            for i in range(keys.index(symbol)):
                cumulative_probability += self.source[keys[i]]
            
            return cumulative_probability

    def calculate_cumulative_probabilities_of_source(self):
        for key in  self.source:
            self.cumulative_probabilities[key] = self.calculate_cumulative_probabilities(key)

    
    def encode_message(self, message):
        high = 1
        low = 0
        for i in  range(0, len(message)):
            old_high = high
            high = old_high*self.source[message[i]]
            low = low + old_high*self.cumulative_probabilities[message[i]]

        return low

    def is_value_inside_range(self, value, low, high):
        return value>=low and value < high

    def decode_symbol(self, value, low, high):
        range = high-low
        low_to_use = low
        keys = list(self.source.keys())
        i = 0
        while( not self.is_value_inside_range(value,low_to_use,(low_to_use + range*self.source[keys[i]]))):
            low_to_use = (low_to_use + range*self.source[keys[i]])
            i +=1
        
        return keys[i]
        

    def decode_message(self, encoded_message, len_message):
        high = 1
        low = 0
        decoded_message = ""
        for i in range(len_message):
            charToAdd = self.decode_symbol(encoded_message, low, low+high)
            decoded_message += charToAdd
            old_high = high
            high = old_high*self.source[charToAdd]
            low = low + old_high*self.cumulative_probabilities[charToAdd]
        return decoded_message



# dic = {'a': 0.5, 'b':0.25, 'c':0.25}
# prova =  ArithmeticCode(dic)

# print(prova.cumulative_probabilities)
# print("encode message:",prova.encode_message('abac'))
# print(prova.DecodeMessage(prova.encode_message('abac'), 4))


# dic1 = {'a': 0.4, 'b':0.5, 'c':0.1}
# prova1 =  ArithmeticCode(dic1)

# print(prova1.cumulative_probabilities)
# print(prova1.encode_message('bbbc'))
# print(prova1.DecodeMessage(prova1.encode_message('bbbc'), len('bbbc')))

# # # dic2 = {'s': 0.5, 'w':0.1, 'i':0.2, 'm':0.1, '_':0.1}
# dic2 = {'A': 0.2, 'B':0.5, 'C':0.3}
# prova2 =  ArithmeticCode(dic2)

# print(prova2.cumulative_probabilities)
# print(prova2.encode_message('AABBAACCCBB'))
# print(prova2.DecodeMessage(prova2.encode_message('AABBAACCCBB'), len('AABBAACCCBB')))