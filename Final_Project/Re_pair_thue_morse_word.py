from Final_Project.Thue_Morse_Word import ThueMorseWord
from CF_Grammar.re_pair import RePairCreator
from Final_Project.CNF_analyzer import *

def apply_grammar(grammar, text):
    for key in grammar.keys():
        if(grammar[key] != 'S' and grammar[key] != 'a' and  grammar[key] != 'b' ):
            text = text.replace(key, grammar[key])
    
    return text
    
def get_new_grammar(TM_word, grammar:dict):
        repair_creator =  RePairCreator()
        repair_creator.set_index_value(len(grammar.keys()))
        repair_creator.apply_for_thue_morse_word(TM_word)
        grammar.update(repair_creator.grammar)
        return grammar
        
def get_CF_grammar(order):
    if(order < 1):
        return {
                'a':'X0',
                'b':'X1',
                'X0X1':'S'
                }
    else:
        grammar = get_CF_grammar(order-2)
        grammar.popitem()
        TM_word = apply_grammar(grammar,  ThueMorseWord().get_TM_word_recursive_with_grammar(order))
        return get_new_grammar(TM_word, grammar)
        
def print_grammar(grammar):
    for key in grammar.keys():
        print(grammar[key],'->',key)   
        