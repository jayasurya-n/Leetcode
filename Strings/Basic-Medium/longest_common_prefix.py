class Solution:
    def longestCommonPrefix(self, str: list[str]) -> str:
        prefix = ""
        for index in range(len(str[0])):
            ele = str[0][index]
            for i in range(len(str)):
                if(index==len(str[i]) or ele!=str[i][index]):
                    return prefix
            prefix+= str[0][index]
        return prefix
            





s = list(map(str,input().strip().split()))
print(Solution().longestCommonPrefix(s))