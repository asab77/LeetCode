class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = {}

        for num in arr:
            dic[num] = dic.get(num,0)+1
        
        freqs = list(dic.values())

        return len(freqs) == len(set(freqs))
