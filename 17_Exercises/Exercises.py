from Arithmetic_Code.DynamicArithmeticCode import DynamicArithmeticCode
from SardinasPatterson.SardinasPatterson import SardinasPatterson
from Huffman.Huffman import Huffman
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