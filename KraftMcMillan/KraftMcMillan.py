from Entropy.Entropy import Entropy

class KrafMcMillan():
    def apply(self, amount_of_symbols, codewords_length):
        value = sum([amount_of_symbols**(-length) for length in codewords_length])
        return value <= 1

def calculate_average_code_length(probabilities, length):
    average_code_length = 0
    for i in range(probabilities):
        average_code_length += probabilities[i]*length[i]
    
    return average_code_length

def calculate_code_efficiency(probabilities,length, base=2):
    entropy_value = Entropy().calculate_entropy(probabilities,base)
    average_code_length = calculate_average_code_length(probabilities, length)
    return entropy_value/average_code_length
    
def calculate_redundacy_of_code(probabilities,length,base=2):
    code_efficiency = calculate_code_efficiency(probabilities,length,base)
    return 1-code_efficiency

