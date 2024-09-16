from enum import Enum

class StateSardinasPatterson(Enum):
    UD = 1
    NOT_UD = 2
    NONE = 3

class SardinasPatterson:
    def Intersection(self,lst1, lst2):
        return list(set(lst1) & set(lst2))
    
    def AddSuffixToList(self, string, prefix, list):
        suffix = string.replace(prefix, "")
        if suffix and not suffix in list:
            list.append(suffix)
        
    def FoundTheAnswer(self,initialSet, currentSet, setOfSets):
        if(setOfSets and self.Intersection(initialSet, currentSet)):
            return StateSardinasPatterson.NOT_UD
        elif(setOfSets and (not currentSet or currentSet in setOfSets ) ):
            return StateSardinasPatterson.UD
        else:
            return StateSardinasPatterson.NONE
            
    def ApplySardinasPatterson(self, strings):
        listStep = strings.copy()
        setOfLists = []
        status = StateSardinasPatterson.NONE
        print(listStep)
        while(status == StateSardinasPatterson.NONE):
            newList = []
            for string1 in listStep:
                for string2 in strings:
                    if(string2.startswith(string1)):
                        self.AddSuffixToList(string2, string1, newList)
                    elif(string1.startswith(string2)):
                        self.AddSuffixToList(string1, string2, newList)
            
            listStep = newList.copy()
            status = self.FoundTheAnswer(strings, listStep, setOfLists)
            setOfLists.append(listStep)
            print(listStep)
            
        return status
            
trial = SardinasPatterson()
listOfStrings = ["a", "c", "ad", "abb", "bad","deb","bbcde"]
print(trial.ApplySardinasPatterson(listOfStrings))