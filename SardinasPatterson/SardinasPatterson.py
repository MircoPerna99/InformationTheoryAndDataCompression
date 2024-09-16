from enum import Enum

class StateSardinasPatterson(Enum):
    UD = 1
    UD_PREFIX_CODE = 2
    UD_BOUNDED = 3
    UD_UNBOUNDED = 4
    NOT_UD = 5
    NONE = 6
    
class SardinasPatterson:
    def Intersection(self,lst1, lst2):
        return list(set(lst1) & set(lst2))
    
    def AddSuffixToList(self, string, prefix, list):
        suffix = string.replace(prefix, "", 1)
        if suffix and not suffix in list:
            list.append(suffix)
    
    def IsNotUD(self, initialSet, currentSet, setOfSets):
        return setOfSets and self.Intersection(initialSet, currentSet)
    
    def IsUDAndPrefixCode(self, currentSet, setOfSets):
        return not setOfSets and not currentSet
    
    def IsUD(self, currentSet, setOfSets):
        return setOfSets and not currentSet
    
    def IsUnboundedUD(self, currentSet, setOfSets):
        return setOfSets and currentSet in setOfSets 
        
        
    def FoundTheAnswer(self,initialSet, currentSet, setOfSets):
        if(self.IsNotUD(initialSet, currentSet, setOfSets)):
            return StateSardinasPatterson.NOT_UD
        elif(self.IsUDAndPrefixCode( currentSet, setOfSets)):
            return StateSardinasPatterson.UD_PREFIX_CODE
        elif(self.IsUD( currentSet, setOfSets)):
            return StateSardinasPatterson.UDs
        elif(self.IsUnboundedUD(currentSet, setOfSets)):
            return StateSardinasPatterson.UD_UNBOUNDED
        else:
            return StateSardinasPatterson.NONE
            
    def Apply(self, initialSet):
        currentSet = initialSet.copy()
        setOfSets = []
        status = StateSardinasPatterson.NONE
        
        print(currentSet)
        while(status == StateSardinasPatterson.NONE):
            newSetToAdd = []
            
            for string1 in currentSet:
                for string2 in initialSet:
                    if(string2.startswith(string1)):
                        self.AddSuffixToList(string2, string1, newSetToAdd)
                    elif(string1.startswith(string2)):
                        self.AddSuffixToList(string1, string2, newSetToAdd)
            
            currentSet = newSetToAdd.copy()
            status = self.FoundTheAnswer(initialSet, currentSet, setOfSets)
            setOfSets.append(currentSet)
            print(currentSet)
            
        return status
            
# trial = SardinasPatterson()
# listOfStrings = ["a", "c", "ad", "abb", "bad","deb","bbcde"]
# print(trial.ApplySardinasPatterson(listOfStrings).name)


# listOfStrings = ["abc", "abcd", "e", "dba", "bace","ceac","ceab", "eabd"]
# print(trial.ApplySardinasPatterson(listOfStrings).name)

# listOfStrings = ["010", "0001", "0110", "1100", "00011","00110","11110", "101011"]
# print(trial.ApplySardinasPatterson(listOfStrings).name)