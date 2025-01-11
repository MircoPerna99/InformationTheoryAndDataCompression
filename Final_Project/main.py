from Final_Project.Thue_Morse_Word import ThueMorseWord 
from Final_Project.CNF_analyzer import *
from Final_Project.Re_pair_thue_morse_word import *

def take_order():
    try:
        num = int(input("Enter an the order of Thue-Morse: "))
        return num
    except ValueError:
        print("Invalid input. Please enter an integer.")

order = take_order()
TM_word = ThueMorseWord().get_TM_word_recursive(order)
print(f"The Thue-Morse word of order {order} is : {TM_word}")


print(f"This is the CNF grammar for the Thue-Morse word of order {order} using Re-Pair in Chomsky normal form: ")
grammar = get_CF_grammar(order)
print_grammar(grammar)

print("The analysis of the first twenty Thue-Morse words")  
analyzer = CFAnalyzer()
for i in range(30):
    grammar = get_CF_grammar(i)
    analyzer.add_grammar(grammar)
 
print(f"The size of  grammar of the first twenty Thue-Morse words are {analyzer.sizes}")   
print(f"The average discrepancy between the grammar size is {analyzer.calculate_average_discrepancy()}")






