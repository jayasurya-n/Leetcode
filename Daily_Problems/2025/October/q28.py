import math, heapq, bisect, random, sys
from collections import deque, defaultdict

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))
modinv = lambda a,mod:pow(a,mod-2,mod)

class Solution:
    def countValidSelections(self, nums) -> int:
        n = len(nums)
        right = total = sum(nums)
        left = ans = 0
        for i in range(n):
            if(nums[i]==0):
                if(left==right):ans+=2
                elif(left==right+1):ans+=1
                elif(left+1==right):ans+=1
            
            left+=nums[i]
            right-=nums[i]
        
        return ans

# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)