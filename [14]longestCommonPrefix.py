class Solution:
    #flower, flow, flight

    def longestCommonPrefix(self, strs):
        
        def safelyGetFromThing(index, thing):
            if(index < len(thing)): 
                return thing[index]
            else: 
                return None
            
        result = ""
        letter_index = 0;
        first_string = safelyGetFromThing(0, strs)
        guide_letter = safelyGetFromThing(letter_index,first_string)
        good_so_far = first_string is not None and guide_letter is not None;
        while good_so_far:
            for this_string in strs:
                this_letter = safelyGetFromThing(letter_index,this_string)
                if this_letter != guide_letter:
                    good_so_far = False
            if good_so_far:
                letter_index += 1 
                if letter_index < len(first_string):
                    guide_letter = first_string[letter_index]
                else:
                    good_so_far = False
                    
        return first_string[:letter_index]
    
