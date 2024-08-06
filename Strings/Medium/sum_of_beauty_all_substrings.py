class Solution:
    def beautySum(self, s: str) -> int:
        beauty = 0
        for i in range(len(s)):
            count = [0]*26
            for j in range(i,len(s)):
                count[ord(s[j]) - ord('a')] += 1
                maxCount = max(x for x in count if x>0)
                minCount = min(x for x in count if x>0)
                beauty += maxCount - minCount
        return beauty



s = input()
print(Solution().beautySum(s))