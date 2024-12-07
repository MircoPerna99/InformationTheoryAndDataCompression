
#Determine if the following code {01, 011, 1101, 11011, 11101} is UD
#We determine if the following code {01, 011, 1101, 11011, 11101} is UD 
#using the algorithm Sardinas-Patterson algorithm

# some_file.py
import sys
# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, '/Users/mircoperna/Documents/Universita/Magistrale/INFORMATION THEORY AND DATA COMPRESSION/Esercizi/InformationTheoryAndDataCompression/SardinasPatterson')
from SardinasPatterson import SardinasPatterson


trial = SardinasPatterson()
listOfStrings = ["01", "011", "1101", "11011", "11101"]
print(trial.Apply(listOfStrings).name)