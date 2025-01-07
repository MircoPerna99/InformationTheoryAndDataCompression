class SuffixArray(): 
    def SA_IS(self, text):     
        self.init_text_to_use(text)
        self.set_text_length()
        self.set_suffix_array_type()
        self.set_LMS_positions()
        saLms = self.induce_sort(self.lms_positions)
        shorted_string = self.get_shortened_string(saLms)
        lms_ordered = self.get_ordered_LMS(shorted_string, saLms)
        return self.induce_sort(lms_ordered)   
        
    def get_ordered_LMS(self, shorted_string, saLMS):
        lms_ordered = []
        if(len(set(shorted_string)) < len(shorted_string)):
            ssSa = SuffixArray().SA_IS(shorted_string)
            lms_ordered = [self.lms_positions[i] for i in ssSa]
        else:
            for i in saLMS:
                if(self.isLms[i]):
                    lms_ordered.append(i)
                    
        return lms_ordered
    
    def init_text_to_use(self, text):
        if(text[-1] != '$'):
            text += '$'
        
        self.text_to_use = text
    
    def set_text_length(self):
        self.text_length =  len(self.text_to_use)
        
    def set_suffix_array_type(self):
        self.suffix_array_type = [False]* self.text_length
        self.suffix_array_type[self.text_length-1] = True
        for i in range(self.text_length-2, -1, -1):
            self.suffix_array_type[i] = self.define_type(i)
         
    def define_type(self, index):
        if(self.text_to_use[index] == self.text_to_use[index+1]):
            return  self.suffix_array_type[index+1]
        else:
            return self.text_to_use[index] < self.text_to_use[index+1]
    
    
    def set_LMS_positions(self):
        self.lms_positions = []
        self.isLms = [False]*self.text_length
        for i in range(1, len(self.text_to_use)):
            if( not self.suffix_array_type[i-1] and  self.suffix_array_type[i]):
                self.lms_positions.append(i)
                self.isLms[i] = True
           
    def induce_sort(self, lms_positions): 
        size_text = len(self.text_to_use)  
        sa = [-1] * size_text
        buckets = self.get_bucket_sizes()
        
        tails = self.get_bucket_tails(buckets)
        for pos in reversed(lms_positions):
            bucket = self.text_to_use[pos]
            tails[bucket] -= 1
            sa[tails[bucket]] = pos
        
        heads = self.get_bucket_heads(buckets)
        for i in range(size_text):
            pos = sa[i]
            if pos > 0 and not self.suffix_array_type[pos - 1]:
                bucket = self.text_to_use[pos - 1]
                if(heads[bucket] < len(sa)):
                    sa[heads[bucket]] = pos - 1
                    heads[bucket] += 1
        
        
        # Induce S-type suffixes
        tails = self.get_bucket_tails(buckets)
        for i in range(size_text - 1, -1, -1):
            pos = sa[i]
            if pos > 0 and self.suffix_array_type[pos - 1]:
                bucket = self.text_to_use[pos - 1]
                tails[bucket] -= 1
                sa[tails[bucket]] = pos - 1
        return sa  
                
    def get_bucket_sizes(self):
        alphabet_occurences = [0] * 255
        for c in self.text_to_use: 
            alphabet_occurences[ord(c)] += 1
        
        buckets = {chr(i): val for i, val in enumerate(alphabet_occurences) if val != 0}
        return buckets

    def get_bucket_heads(self, buckets):
        heads = {}
        sum = 0
        for key in buckets.keys():
            heads[key] = sum
            sum += buckets[key]
        return heads

    def get_bucket_tails(self, buckets):
        tails = {}
        sum = 0
        for key in buckets.keys():
            sum += buckets[key]
            tails[key] = sum
        return tails
    
    def get_shortened_string(self, saLms):
        prev_LMS = -1
        LMS_names = [-1] * self.text_length
        new_name = 0
        for i in saLms:
                if  self.isLms[i]:
                    if prev_LMS == -1:
                        new_name += 1
                    else:
                        j = prev_LMS
                        k = i
                        while j < self.text_length and k < self.text_length and self.text_to_use[j] == self.text_to_use[k] and self.isLms[j] ==  self.isLms[k]:
                            j += 1
                            k += 1
                        if j == self.text_length or k == self.text_length or self.text_to_use[j] != self.text_to_use[k]:
                            new_name += 1
                    LMS_names[i] = new_name - 1
                    prev_LMS = i
              
        return ''.join(self.from_int_to_char_shortened_string(name) for name in LMS_names if name != -1)
    
    def from_int_to_char_shortened_string(self,  value):
        if(value == 0):
            return '$'
        else:
           return chr(value + 96)

# text = 'banaananaanana'
# print(SuffixArray().SA_IS(text))

# text = 'aaaa'
# print(SuffixArray().SA_IS(text))

# text = 'banana'
# print(SuffixArray().SA_IS(text))

# text = 'abcab'
# print(SuffixArray().SA_IS(text))

# text = 'mississippi'
# print(SuffixArray().SA_IS(text))
