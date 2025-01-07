import math

def calculate_frequency_of_chars_on_text(name_file):
        dictionary = {}
        file = open(name_file, "r")
        amount_of_chars = 0
        for line in file:
            for char in line:
                amount_of_chars = amount_of_chars+1
                if not dictionary or not char in dictionary:
                    dictionary[char] = 1
                else:
                    dictionary[char] = dictionary[char]+1
        
        for key in dictionary:
            dictionary[key] = dictionary[key]/amount_of_chars
        
        file.close()
        
        return dictionary

class Entropy:    
    def calculate_entropy(self, probabilities, base = 2):
        entropy_calculated = 0
        for probability in  probabilities:
            entropy_calculated = entropy_calculated + probability*math.log(1/probability, base)
    
        return entropy_calculated
    
    def calculate_entropy_of_text(self, nameFile):
        dictionary = calculate_frequency_of_chars_on_text(nameFile)
        return self.calculate_entropy(dictionary.values())