class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:

        dic ={}

        for char in s:
            if char in dic:
                dic[char] += 1
            
            else:
                dic[char] = 1
            
        
        value_list = list(dic.values())
        first_val = value_list[0]

        for value in value_list:
            if value != first_val:
                return False
        
        return True

        
