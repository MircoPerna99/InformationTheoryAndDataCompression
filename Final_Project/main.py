from Final_Project.Thue_Morse_Word import ThueMorseWord
from CF_Grammar.re_pair import RePairCreator

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


for i in range(10):
    TM_word = ThueMorseWord().get_TM_word(i)

    repair_creator =  RePairCreator()
    repair_creator.apply(TM_word)


    repair_creator.print_grammar()




