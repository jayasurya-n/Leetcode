import math, heapq, bisect, random, sys
from collections import deque, defaultdict

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))
modinv = lambda a,mod:pow(a,mod-2,mod)

class Solution:
    def findXSum(self, nums, k: int, x: int):
        n = len(nums)
        ans = []

        hash = defaultdict(int)
        for i in range(k-1):
            hash[nums[i]]+=1
        
        for i in range(k-1,n):
            hash[nums[i]]+=1
            if(i>=k):hash[nums[i-k]]-=1

            temp = sorted(hash.items(),key=lambda x:(-x[1],-x[0]))
            tsum = 0
            for j in range(min(x,len(temp))):
                tsum+=temp[j][0]*temp[j][1]
            ans.append(tsum)

        return ans
    
# time complexity: O(n*klogk)
# space complexity: O(k)
if __name__ == "__main__":
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)