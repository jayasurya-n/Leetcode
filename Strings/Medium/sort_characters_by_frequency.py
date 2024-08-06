class Solution:
    def frequencySort(self, s: str) -> str:
        freq = dict()
        for i in s:
            freq[i] = freq.setdefault(i,0)+1
        freq = dict(sorted(freq.items(),key = lambda item:(-item[1],item[0])))
        newString = "".join(key*value for key,value in freq.items())
        return newString


s = input()
print(Solution().frequencySort(s))