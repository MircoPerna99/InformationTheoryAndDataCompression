
            
            
class CFAnalyzer():
        def __init__(self):
            self.sizes = []

        def add_grammar(self, grammar):
            new_size = self.calculate_size_grammar(grammar)
            self.sizes.append(new_size)
    
        
        def calculate_size_grammar(self,grammar):
            size_grammar = 0
            for right_value in grammar:
                size_grammar += sum(1 for char in right_value if char.isalpha())
                
            return size_grammar
        
        def calculate_average_discrepancy(self):
            discrepancies = [abs(self.sizes[i] - self.sizes[i + 1]) for i in range(len(self.sizes) - 1)]
            average_discrepancy = sum(discrepancies) / len(discrepancies)
            return average_discrepancy
            