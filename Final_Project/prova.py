from Final_Project.Re_pair_thue_morse_word import *
from Final_Project.Thue_Morse_Word import ThueMorseWord
from CF_Grammar.re_pair import RePairCreator
from Final_Project.CNF_analyzer import *



# TM_word1 = ThueMorseWord().get_TM_word(9)
# print(TM_word1)
# repair_creator =  RePairCreator()
# repair_creator.apply(TM_word1)
# repair_creator.print_grammar()

def reverse(grammar):
        output = ""
        for idx, key in enumerate(reversed(grammar.keys())):
            if(output == ""):
                output += str(key)
            else:
                if(idx < 7):
                    output = output.replace(grammar[key], key)
        
        return output
    
def apply_grammar_prova(grammar, text):
    for idx, key in enumerate(grammar.keys()):
        if(grammar[key] != 'S' and idx < 3):
            text = text.replace(key, grammar[key])
    return text
    
grammar1 = get_CF_grammar(10)
print_grammar(grammar1)


# grammar1 = get_CF_grammar_previous_number(5)
# print_grammar(grammar1)







# TM_word1 = ThueMorseWord().get_TM_word_recursive(7)
# TM_word2 = ThueMorseWord().get_TM_word_recursive(9)
# print(TM_word2.count(TM_word1))

# TM_word1 = ThueMorseWord().get_TM_word_recursive(9)
# TM_word2 = ThueMorseWord().get_TM_word_recursive(11)
# print(TM_word2.count(TM_word1))


# TM_word1 = ThueMorseWord().get_TM_word_recursive(11)
# TM_word2 = ThueMorseWord().get_TM_word_recursive(13)
# print(TM_word2.count(TM_word1))



# TM_word1 = ThueMorseWord().get_TM_word_recursive(6)
# TM_word2 = ThueMorseWord().get_TM_word_recursive(8)
# print(TM_word2.count(TM_word1))

# TM_word1 = ThueMorseWord().get_TM_word_recursive(8)
# TM_word2 = ThueMorseWord().get_TM_word_recursive(10)
# print(TM_word2.count(TM_word1))

