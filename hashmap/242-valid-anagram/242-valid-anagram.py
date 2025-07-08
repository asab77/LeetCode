# if length of s and t are not equal return false

# Create an empty dictionary as s_count

# loop to populate the s_count dictionary using s string 
# increasing the value of the keys in the s_count 

# loop for t string and decrease the value of the s_count dictionary if the character is shared between 
# if value is < 0 return false

# return true

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        s_count = {} #Empty dic to keep track 

        for char in s:
            if char not in s_count:
                s_count[char] = 1
            else:
                s_count[char] += 1

        for char1 in t:
            if char1 not in s_count:
                return False
            else:
                s_count[char1] -= 1

                if s_count[char1] < 0:
                    return False

        return True
        
