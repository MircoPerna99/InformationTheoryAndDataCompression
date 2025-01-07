from Utilities.SuffixArray import SuffixArray

class   BWTResult():
    def __init__(self, trasformed_text, index):
        self.trasformed_text = trasformed_text
        self.index = index

class BWT():
    def rotate(self, text):
        return text[-1]+text[:-1]
    
    def sort_text(self, text):
        return ''.join(sorted(text))
    
    def take_trasformed_text(self, list):
         value_to_return = ""
         
         for item in list:
             value_to_return = value_to_return + item[-1]
             
         return value_to_return
    
    def trasform(self, text):
        size_text = len(text)
        list_of_texts = [text]
        
        for i in range(1, size_text):
            list_of_texts.append(self.rotate(list_of_texts[-1]))
        
        list_of_texts.sort()
                                
        return  BWTResult(self.take_trasformed_text(list_of_texts), list_of_texts.index(text))
    
        
    def trasform_with_SA(self, text):
    
        if(text[-1] != '$'):
            text += '$'
    
        suffix_array = SuffixArray().SA_IS(text)
        bwt = self.get_trasformed_text(suffix_array, text)
        index = self.get_index_original_text(suffix_array)
        return  BWTResult(bwt, index)

    def get_trasformed_text(self, suffix_array, text):
        output = ""
        
        for i in range(len(text)):
            char_to_add = ""
            if(suffix_array[i] == 0):
                char_to_add = '$'
            else:
                char_to_add = text[suffix_array[i]-1]
            
            output =output + char_to_add 
        
        return output
    
    def get_index_original_text(self, suffix_array):
        for i in range(suffix_array):
            if(suffix_array[i] == 0):
                return 0
        
        return -1
        
    def compose_rotation(self, text, list):
        for i in range(len(text)):
            list[i] = text[i]+list[i]
    
    def reverse(self,  text, index):
        sorted_text = list(text)
        sorted_text.sort()
        
        for i in range(len(text)-1):
            self.compose_rotation(text, sorted_text)
            sorted_text.sort()
        
        return sorted_text[index]
    