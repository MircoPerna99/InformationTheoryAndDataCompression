from Final_Project.Thue_Morse_Word import ThueMorseWord
from CF_Grammar.re_pair import RePairCreator
from Final_Project.CNF_analyzer import *

def take_order():
    try:
        num = int(input("Enter an the order of Thue-Morse: "))
        return num
    except ValueError:
        print("Invalid input. Please enter an integer.")
        
def apply_grammar(grammar, text):
    for key in grammar.keys():
        if(grammar[key] != 'S'):
            text = text.replace(key, grammar[key])
    
    return text
    
        
def get_CF_grammar_previous_number(order):
    if(order <= 1):
        return {
                'a':'X0',
                'b':'X1'
                }
    else:
        grammar = get_CF_grammar_previous_number(order-2)
        if(order-2 > 1):
            grammar.popitem()
        TM_word = ThueMorseWord().get_TM_word_recursive(order)
        TM_word = apply_grammar(grammar, TM_word)
        repair_creator =  RePairCreator()
        repair_creator.set_index_value(len(grammar.keys()))
        repair_creator.apply_for_thue_morse_word(TM_word)
        grammar.update(repair_creator.grammar)
        return grammar
        
def print_grammar(grammar):
    for key in grammar.keys():
        print(grammar[key],'->',key)   
        
        


order = take_order()
grammar = get_CF_grammar_previous_number(order)
print_grammar(grammar)



