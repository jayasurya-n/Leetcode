from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def wordBreak(s, dictionary):
        n = len(s)
        dp = dict()
        
        def rec(ind):
            if(ind>=n):return [""]
            if(ind in dp):return dp[ind]

            ans = []
            for i in range(ind,n):
                word = s[ind:i+1]
                if(word in dictionary):
                    sentences = rec(i+1)
                    for l in sentences:
                        if(l):ans.append(word+" "+l)
                        else:ans.append(word)
            dp[ind] = ans
            return ans
        
        return rec(0)
    
    # def wordBreak(s, dictionary):
    # n = len(s)
    # ans = []
    
    # def rec(ind,temp):
    #     if(ind>=n):
    #         ans.append(" ".join(temp))
    #         return 

    #     for i in range(ind,n):
    #         word = s[ind:i+1]
    #         if(word in dictionary):
    #             temp.append(word)
    #             rec(i+1,temp)
    #             temp.pop()
    # rec(0,[])
    # return ans

# time complexity: O(m*n^2),O(m*2^n)
# space complexity: O(n^2),O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))