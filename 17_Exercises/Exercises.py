from Arithmetic_Code.DynamicArithmeticCode import DynamicArithmeticCode
from SardinasPatterson.SardinasPatterson import SardinasPatterson
from Huffman.Huffman import Huffman
from Universal_Integer_Code.Gamma import GammaCoder
from KraftMcMillan.KraftMcMillan import KrafMcMillan
from BurrowsWheelerTransform.BurrowsWheelerTransform import BWT
from LZ.LZ77 import LZ77
from LZ.LZ78 import LZ78Coder

#Determine if the following code {01, 011, 1101, 11011, 11101} is UD
#We determine if the following code {01, 011, 1101, 11011, 11101} is UD 
#using the algorithm Sardinas-Patterson algorithm
trial = SardinasPatterson()
listOfStrings = ["01", "011", "1101", "11011", "11101"]
print(trial.Apply(listOfStrings).name)

#Given an input text in which the characters in the alphabet have the following
#frequencies: A: 10 B: 15 C: 30 D: 20 E: 25, construct the Huffman code.
source = {"A":10/100, "B": 15/100, "C": 30/100 , "D": 20/100,  "E": 25/100}
huffmanCoder = Huffman(source)
print(huffmanCoder.ApplyEncode())

#Given the text abbcccdddd, which is its arithmetic coding?
dic = {'a': 1, 'b':1, 'c':1, 'd':1}
acCoder = DynamicArithmeticCode(dic)
messageEncoded = acCoder.EncodeMessage('abbcccdddd')
print(messageEncoded)
print(acCoder.DecodeMessage(messageEncoded))

#Given a sequence of integers {10, 5, 8, 3, 12}, which is the gamma encoding?
sequence = [10,5,8,3,12]
sequenceEncoded = []
for item in sequence:
    sequenceEncoded.append(GammaCoder().Encode(item))
    
print(sequenceEncoded)

#Consider a set of source symbols S = {A, B, C, D}. 
#Is it possible to construct a binary prefix code with corresponding codeword lengths L = {2, 2, 3, 3}?
#Let us consider now a set of source symbols S = {A, B, C, D, E} with corresponding codeword lengths L = {2, 2, 2, 3, 3}.
print("Is it possible to construct a binary prefix code with corresponding codeword lengths L = {2, 2, 3, 3} and a set of source symbols S = {A, B, C, D}?")
isItPossible = KrafMcMillan().Apply(2, [2,2,3,3])
if(isItPossible):
    print("It is possible" )
else: 
    print("It is not possible")

print("Is it possible to construct a binary prefix with a set of source symbols S = {A, B, C, D, E} with corresponding codeword lengths L = {2, 2, 2, 3, 3}")
isItPossible = KrafMcMillan().Apply(2, [2,2,2,3,3])
if(isItPossible):
    print("It is possible" )
else: 
    print("It is not possible")
    
#Compute BWT(banana)
value = BWT().Trasform("banana")
print(value.trasformedText)
print(BWT().Reverse(value.trasformedText, value.index))

#Compute LZ77 parsing of the string abcdeabcdeabcde
coder = LZ77()
coder.Encode("abcdeabcdeabcde") 
print(coder.Decode()) 

#Compute LZ78 parsing of the string abcdeabcdeabcde
coderLZ78 = LZ78Coder()
resultLZ78 = coderLZ78.Encode("abcdeabcdeabcde")
print(resultLZ78)
print(LZ78Coder().Decode(resultLZ78))