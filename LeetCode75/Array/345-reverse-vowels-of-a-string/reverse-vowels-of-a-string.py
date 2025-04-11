class Solution:
    def reverseVowels(self, s: str) -> str:

        vowels = []
        s = list(s)  # Convert string to list

        for char in s:
            if char.lower() in 'aeiou':
                vowels.append(char)

        for i in range(len(s)):
            if s[i].lower() in 'aeiou':
                s[i] = vowels.pop()  # replace with last vowel

        return ''.join(s)
        
