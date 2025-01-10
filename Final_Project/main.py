from Final_Project.Thue_Morse_Word import ThueMorseWord
from CF_Grammar.re_pair import RePairCreator
from Final_Project.CNF_analyzer import *

def take_order():
    try:
        num = int(input("Enter an the order of Thue-Morse: "))
        return num
    except ValueError:
        print("Invalid input. Please enter an integer.")


order = take_order()
TM_word = ThueMorseWord().get_TM_word(order)
print(f"The Thue-Morse word of order {order} is : {TM_word}")

repair_creator =  RePairCreator()
repair_creator.apply(TM_word)

print(f"This is the CNF grammar for the Thue-Morse word of order {order} using Re-Pair in Chomsky normal form: ")
repair_creator.print_grammar()


print("The analysis of the first twenty Thue-Morse words")  
analyzer = CFAnalyzer()
for i in range(20):
    TM_word = ThueMorseWord().get_TM_word(i)
    repair_creator =  RePairCreator()
    repair_creator.apply(TM_word)
    analyzer.add_grammar(repair_creator.grammar)
 
print(f"The size of  grammar of the first twenty Thue-Morse words are {analyzer.sizes}")   
print(f"The average discrepancy between the grammar size is {analyzer.calculate_average_discrepancy()}")






