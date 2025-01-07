from enum import Enum

class StateSardinasPatterson(Enum):
    UD = 1
    UD_PREFIX_CODE = 2
    UD_BOUNDED = 3
    UD_UNBOUNDED = 4
    NOT_UD = 5
    NONE = 6
    
class SardinasPatterson:
    def __init__(self):
        pass
    
    def intersection(self,lst1, lst2):
        return list(set(lst1) & set(lst2))
    
    def add_suffix_to_list(self, string, prefix, list):
        suffix = string.replace(prefix, "", 1)
        if suffix and not suffix in list:
            list.append(suffix)
    
    def is_not_UD(self, initial_set, current_set, set_of_sets):
        return set_of_sets and self.intersection(initial_set, current_set)
    
    def is_UD_and_prefix_code(self, current_set, set_of_sets):
        return not set_of_sets and not current_set
    
    def is_UD(self, current_set, set_of_sets):
        return set_of_sets and not current_set
    
    def is_unbounded_UD(self, current_set, set_of_sets):
        return set_of_sets and current_set in set_of_sets 
        
        
    def found_the_answer(self,initial_set, current_set, set_of_sets):
        if(self.is_not_UD(initial_set, current_set, set_of_sets)):
            return StateSardinasPatterson.NOT_UD
        elif(self.is_UD_and_prefix_code( current_set, set_of_sets)):
            return StateSardinasPatterson.UD_PREFIX_CODE
        elif(self.is_UD( current_set, set_of_sets)):
            return StateSardinasPatterson.UDs
        elif(self.is_unbounded_UD(current_set, set_of_sets)):
            return StateSardinasPatterson.UD_UNBOUNDED
        else:
            return StateSardinasPatterson.NONE
            
    def apply(self, initial_set):
        current_set = initial_set.copy()
        set_of_sets = []
        status = StateSardinasPatterson.NONE
        
        print(current_set)
        while(status == StateSardinasPatterson.NONE):
            new_set_to_add = []
            
            for string1 in current_set:
                for string2 in initial_set:
                    if(string2.startswith(string1)):
                        self.add_suffix_to_list(string2, string1, new_set_to_add)
                    elif(string1.startswith(string2)):
                        self.add_suffix_to_list(string1, string2, new_set_to_add)
            
            current_set = new_set_to_add.copy()
            status = self.found_the_answer(initial_set, current_set, set_of_sets)
            set_of_sets.append(current_set)
            print(current_set)
            
        return status