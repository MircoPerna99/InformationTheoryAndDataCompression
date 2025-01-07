from Arithmetic_Code.DynamicArithmeticCode import DynamicArithmeticCode
from SardinasPatterson.SardinasPatterson import SardinasPatterson
from Huffman.Huffman import Huffman
from Universal_Integer_Code.Gamma import GammaCoder
from KraftMcMillan.KraftMcMillan import KrafMcMillan
from BurrowsWheelerTransform.BurrowsWheelerTransform import BWT
from LZ.LZ77 import LZ77
from LZ.LZ78 import LZ78Coder
from LZ.LZW import LZWCoder

#Determine if the following code {01, 011, 1101, 11011, 11101} is UD
#We determine if the following code {01, 011, 1101, 11011, 11101} is UD 
#using the algorithm Sardinas-Patterson algorithm
print("\nDetermine if the following code {01, 011, 1101, 11011, 11101} is UD")
trial = SardinasPatterson()
list_of_strings = ["01", "011", "1101", "11011", "11101"]
print(trial.apply(list_of_strings).name)

#Given an input text in which the characters in the alphabet have the following
#frequencies: A: 10 B: 15 C: 30 D: 20 E: 25, construct the Huffman code.
print("\nGiven an input text in which the characters in the alphabet have the following\nfrequencies: A: 10 B: 15 C: 30 D: 20 E: 25, construct the Huffman code.")
source = {"A":10/100, "B": 15/100, "C": 30/100 , "D": 20/100,  "E": 25/100}
huffman_coder = Huffman(source)
print(huffman_coder.apply_encode())

#Given the text abbcccdddd, which is its arithmetic coding?
print("\nGiven the text abbcccdddd, which is its arithmetic coding?")
dic = {'a': 1, 'b':1, 'c':1, 'd':1}
acCoder = DynamicArithmeticCode(dic)
message_encoded = acCoder.encode_message('abbcccdddd')
print(message_encoded)
print(acCoder.decode_message(message_encoded))

#Given a sequence of integers {10, 5, 8, 3, 12}, which is the gamma encoding?
print("\nGiven a sequence of integers {10, 5, 8, 3, 12}, which is the gamma encoding?")
sequence = [10,5,8,3,12]
sequence_encoded = []
for item in sequence:
    sequence_encoded.append(GammaCoder().encode(item))
    
print(sequence_encoded)

#Consider a set of source symbols S = {A, B, C, D}. 
#Is it possible to construct a binary prefix code with corresponding codeword lengths L = {2, 2, 3, 3}?
#Let us consider now a set of source symbols S = {A, B, C, D, E} with corresponding codeword lengths L = {2, 2, 2, 3, 3}.
print("Is it possible to construct a binary prefix code with corresponding codeword lengths L = {2, 2, 3, 3} and a set of source symbols S = {A, B, C, D}?")
is_it_possible = KrafMcMillan().apply(2, [2,2,3,3])
if(is_it_possible):
    print("It is possible" )
else: 
    print("It is not possible")

print("Is it possible to construct a binary prefix with a set of source symbols S = {A, B, C, D, E} with corresponding codeword lengths L = {2, 2, 2, 3, 3}")
is_it_possible = KrafMcMillan().apply(2, [2,2,2,3,3])
if(is_it_possible):
    print("It is possible" )
else: 
    print("It is not possible")
    
#Compute BWT(banana)
print("\nCompute BWT(banana)")
value = BWT().trasform("banana")
print(value.trasformed_text)
print(BWT().reverse(value.trasformed_text, value.index))

#Compute LZ77 parsing of the string abcdeabcdeabcde
print("\nCompute LZ77 parsing of the string abcdeabcdeabcde")
coder = LZ77()
coder.encode("abcdeabcdeabcde") 
print(coder.decode()) 

#Apply the LZ77 algorithm to the text ‘aababbbabaababbbabbabb’
print("\nApply the LZ77 algorithm to the text ‘aababbbabaababbbabbabb’")
coder = LZ77()
coder.encode("aababbbabaababbbabbabb") 
print(coder.decode()) 

#Compute LZ78 parsing of the string abcdeabcdeabcde
print("\nCompute LZ78 parsing of the string abcdeabcdeabcde")
coderLZ78 = LZ78Coder()
resultLZ78 = coderLZ78.encode("abcdeabcdeabcde")
print(resultLZ78)
print(LZ78Coder().decode(resultLZ78))

#Apply the LZ78 algorithm to the text ‘barbara–bar’
print("\nApply the LZ78 algorithm to the text ‘barbara–bar")
coderLZ78 = LZ78Coder()
resultLZ78 = coderLZ78.encode("barbara–bar")
print(resultLZ78)
print(LZ78Coder().decode(resultLZ78))

#Apply the LZW algorithm to the text ‘aababbbabaababbbabbabb’
print("\nApply the LZW algorithm to the text ‘aababbbabaababbbabbabb’")
coderLZW = LZWCoder(['a','b'])
resultLZW = coderLZW.encode("aababbbabaababbbabbabb")
print(coderLZW.codebook_encode)
print(resultLZW)
print(coderLZW.decode(resultLZW))
print(coderLZW.codebook_decode)
